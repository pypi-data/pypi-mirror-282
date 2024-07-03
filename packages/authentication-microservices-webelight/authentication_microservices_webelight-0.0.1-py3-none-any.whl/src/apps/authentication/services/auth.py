import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import RedirectResponse

from apps.authentication.exceptions import MobileAlreadyVerified, CantUpdateMobile, \
    EmailAlreadyVerified, CantUpdateEmail, BothAreAlreadyVerified
from apps.authentication.models.authentication import AuthenticationModel
from config import settings
from core.auth import access, refresh
from core.common_helpers import generate_otp, create_tokens, verify_otp
from core.db import db_session
from core.exceptions import UserIsExist, InvalidPassword, UserIsNotFound
from core.types import OtpTypes, Providers
from core.utils.hash_url import Hash
from core.utils.hashing import verify_password, hash_password
from core.utils.redis import redis
from core.utils.schema import SuccessResponse


class AuthService:
    """
    Service with methods to set and get values.
    """

    def __init__(self, session: Annotated[AsyncSession, Depends(db_session)]) -> None:
        """
        Call method to inject db_session as a dependency.
        This method also calls a database connection which is injected here.

        :param session: an asynchronous database connection
        """
        self.session = session

    async def send_otp(self, phone_number: str = None, email: EmailStr = None):
        """
        Generates an OTP and sends it to the provided phone number or email.
        Creates a new user in the system with the provided contact details.

        Args:
            phone_number (str, optional): The phone number to send the OTP to. Defaults to None.
            email (EmailStr, optional): The email address to send the OTP to. Defaults to None.

        Returns:
            dict: A dictionary containing the access token, refresh token, and the generated OTP.

        Raises:
            HTTPException: If OTP generation fails.
        """

        if phone_number:
            new_user = AuthenticationModel.create(phone_number=phone_number, verified_user=True,
                                                  is_phone_verify=True)
            self.session.add(new_user)
            otp_type = OtpTypes.PHONE_NUMBER
            otp_num = await generate_otp(otp_type=otp_type, phone_number=phone_number)
            otp_data = otp_num["otp"]
            access_token = access.encode(payload={"phone_number": str(phone_number)},
                                         expire_period=int(settings.ACCESS_TOKEN_EXP))
            refresh_token = refresh.encode(payload={"phone_number": str(phone_number)},
                                           expire_period=int(settings.REFRESH_TOKEN_EXP))
            return {"access_token": access_token, "refresh_token": refresh_token, "otp": otp_data}

        if email:
            new_user = AuthenticationModel.create(email=email, verified_user=True, is_email_verify=True)
            self.session.add(new_user)
            otp_type = OtpTypes.EMAIL

            otp_num = await generate_otp(otp_type=otp_type, email=email)
            otp_data = otp_num["otp"]
            access_token = access.encode(payload={"email": str(email)},
                                         expire_period=int(settings.ACCESS_TOKEN_EXP))
            refresh_token = refresh.encode(payload={"email": str(email)},
                                           expire_period=int(settings.REFRESH_TOKEN_EXP))
            return {"access_token": access_token, "refresh_token": refresh_token, "otp": otp_data}

    async def verify_otp(self, otp: int, phone_number: str = None, email: EmailStr = None):
        """
            Verifies the provided OTP for the given phone number or email. Updates the user's verification status.

            Args:
                otp (int): The OTP to verify.
                phone_number (str, optional): The phone number to verify the OTP against. Defaults to None.
                email (EmailStr, optional): The email address to verify the OTP against. Defaults to None.

            Returns:
                dict: A dictionary containing new access and refresh tokens.

            Raises:
                HTTPException: If the OTP is invalid or verification fails.
        """

        if phone_number:
            phone = await self.session.scalar(select(AuthenticationModel)
                                              .where(AuthenticationModel.phone_number == phone_number))
            otp_verified = await verify_otp(otp_type=OtpTypes.PHONE_NUMBER, otp=otp, phone_number=phone_number)
            if not otp_verified:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid OTP")
            phone.is_phone_verify = True
            token_id = phone.id

        elif email:
            email_name = await self.session.scalar(
                select(AuthenticationModel).where(AuthenticationModel.email == email))
            otp_verified = await verify_otp(otp_type=OtpTypes.EMAIL, otp=otp, email=email)
            if not otp_verified:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid OTP")
            email_name.is_email_verify = True
            token_id = email_name.id

        else:
            raise

        return await create_tokens(_id=token_id)

    async def verify_phone_or_email_request(self, user: AuthenticationModel, phone_number: str = None,
                                            email: EmailStr = None):
        """
        Verifies the user's phone number or email. If the user has one verified contact, generates an OTP for the other contact.

        Args:
            user (AuthenticationModel): The user object.
            phone_number (str, optional): The phone number to verify. Defaults to None.
            email (EmailStr, optional): The email address to verify. Defaults to None.

        Returns:
            dict: A dictionary containing the generated OTP.

        Raises:
            HTTPException: If the user already has both contacts verified, or if the request is invalid.
        """
        if user.is_phone_verify and not user.is_email_verify:
            if email:
                user.email = email
                otp_num = await generate_otp(otp_type=OtpTypes.EMAIL, email=email)
                otp_data = otp_num["otp"]
                return {"otp": otp_data}
            elif user.phone_number == phone_number:
                raise MobileAlreadyVerified()
            else:
                raise CantUpdateMobile()

        if user.is_email_verify and not user.is_phone_verify:
            if phone_number:
                user.phone_number = phone_number
                otp_num = await generate_otp(otp_type=OtpTypes.PHONE_NUMBER, phone_number=phone_number)
                otp_data = otp_num["otp"]
                return {"otp": otp_data}
            elif user.email == email:
                raise EmailAlreadyVerified()
            else:
                raise CantUpdateEmail()

        if user.is_email_verify and user.is_phone_verify:
            raise BothAreAlreadyVerified()

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot generate OTP")

    async def phone_and_email_otp_verify(self, user: AuthenticationModel, otp: int, phone_number: str = None,
                                         email: EmailStr = None):
        """
        Verifies the OTP for the user's phone number or email and updates the verification status.

        Args:
            user (AuthenticationModel): The user object.
            otp (int): The OTP to verify.
            phone_number (str, optional): The phone number to verify the OTP against. Defaults to None.
            email (EmailStr, optional): The email address to verify the OTP against. Defaults to None.

        Returns:
            dict: A dictionary containing new access and refresh tokens.

        Raises:
            HTTPException: If the OTP is invalid or verification fails.
        """
        token_id = None
        if phone_number:
            otp_verified = await verify_otp(otp_type=OtpTypes.PHONE_NUMBER, otp=otp, phone_number=phone_number)
            if not otp_verified:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid OTP")
            user.is_phone_verify = True
            user.phone_number = phone_number

        elif email:
            otp_verified = await verify_otp(otp_type=OtpTypes.EMAIL, otp=otp, email=email)
            if not otp_verified:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid OTP")
            user.is_email_verify = True
            user.email = email

        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot generate OTP")
        return SuccessResponse()

    async def user_password(self, password: str, email: EmailStr = None):
        user = await self.session.scalar(select(AuthenticationModel).where(AuthenticationModel.email == email))
        if user:
            raise UserIsExist
        self.session.add(AuthenticationModel.create(
            email=email,
            password=await hash_password(password=password)
        ))
        return SuccessResponse()

    async def login_with_password(self, password: str, email: EmailStr = None):
        user = await self.session.scalar(select(AuthenticationModel).where(AuthenticationModel.email == email))
        if not user:
            raise UserIsNotFound
        if not await verify_password(password, user.password):
            raise InvalidPassword
        return SuccessResponse()

    async def forgot_password(self, email: EmailStr):
        user = await self.session.scalar(select(AuthenticationModel).where(AuthenticationModel.email == email))
        if not user:
            raise UserIsNotFound
        else:
            verification_token = secrets.token_urlsafe(32)

            key = Hash.make(email)
            exist_token = await redis.get(key)
            if exist_token:
                await redis.delete(exist_token)
            await redis.set(name=verification_token, value=user.email, ex=settings.ACCESS_TOKEN_EXP)
            await redis.set(name=key, value=verification_token, ex=settings.ACCESS_TOKEN_EXP)

            url = f"{settings.FORGET_PASSWORD_URL}?access-token={verification_token}"
            return {"url": url}

    async def verify_otp_password(self, token: str, new_password: str):
        email = await redis.get(token)
        email = email.decode("utf-8")

        user = await self.session.scalar(select(AuthenticationModel).where(AuthenticationModel.email == email))

        if user:
            user.password = await hash_password(password=new_password)
            await redis.delete(token)
            return SuccessResponse()
        else:
            raise UserIsNotFound()

    async def sso_user(self, token: str, provider: Providers, **kwargs) -> RedirectResponse:
        """
        Signup or Login user using social auth provider.

        :param token: id-token from provider
        :param provider: social auth provider - google, facebook, microsoft
        :return: redirect to frontend.
        """
        email = kwargs.get("email")
        if not email:
            return RedirectResponse(url=settings.ERROR_REDIRECT_URL)

        print(email)
