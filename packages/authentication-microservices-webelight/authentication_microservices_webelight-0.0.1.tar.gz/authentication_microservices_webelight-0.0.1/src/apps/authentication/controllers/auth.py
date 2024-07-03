import os
from typing import Annotated, Any

from fastapi import APIRouter, Depends, status, Response, Path, HTTPException
from fastapi_redis_cache import cache
from httpx import AsyncClient
from starlette.responses import RedirectResponse
from starlette.requests import Request

import constants
from apps import AuthenticationModel
from apps.authentication.schemas import OtpRequest, SendOtpResponse
from apps.authentication.schemas.request import (VerifyOTPRequest, PasswordSetup, EmailRequest
, ForgotPasswordVerifyRequest, SecondVerifyOTPRequest, SecondOtpRequest)
from apps.authentication.schemas.response import AccessResponse, ForgotPasswordResponse
from apps.authentication.services import AuthService
from config import settings, AppEnvironment
from core.auth import HasPermission
from core.types import RoleType, Providers

from core.utils.schema import BaseResponse, SuccessResponse
from core.utils.sso_client import SSOOAuthClient, AppleResolver

router_password_less = APIRouter(prefix="/authentication", tags=["User Authentication"])
router_email_password_login= APIRouter(prefix="/authentication", tags=["User Authentication"])
router_sso_login= APIRouter(prefix="/authentication", tags=["User Authentication"])

@router_password_less.post(
    "/registration", status_code=status.HTTP_201_CREATED, name="Create authentication",
    description="Create authentication", operation_id="create_user"
)
async def create_user(
        request: OtpRequest,
        service: Annotated[AuthService, Depends()]
) -> BaseResponse[SendOtpResponse]:
    """Create a new authentication.
    Args:
                    request (CreateUserRequest): The request object containing authentication information.
                    service (AuthService): The authentication service.
    """

    otp_response = await service.send_otp(**request.model_dump())

    return BaseResponse(data=otp_response)


@router_password_less.post(
    "/verify_otp",
    status_code=status.HTTP_200_OK,
    name="Verify email or phone by otp",
    description="Verify email or phone by otp",
    operation_id="verify_otp",
)
async def verify_otp(
        request: VerifyOTPRequest,
        service: Annotated[AuthService, Depends()],
) -> BaseResponse[AccessResponse]:
    otp_verify = await service.verify_otp(**request.model_dump())
    return BaseResponse(data=otp_verify)


@router_password_less.post(
    "/verify-phone-or-email-request",
    status_code=status.HTTP_200_OK,
    name="Verify another email or phone by otp",
    description="Verify another email or phone by otp",
    operation_id="second_verify",
)
async def verify_phone_or_email_request(
        request: SecondOtpRequest,
        service: Annotated[AuthService, Depends()],
        user: Annotated[AuthenticationModel, Depends(HasPermission(RoleType.USER))]
) -> BaseResponse[SendOtpResponse]:
    return BaseResponse(data=await service.verify_phone_or_email_request(**request.model_dump(), user=user))


@router_password_less.post(
    "/second_otp_verify",
    status_code=status.HTTP_200_OK,
    name="Verify another email or phone by another otp",
    description="Verify another email or phone by another otp",
    operation_id="second_otp_verify",
)
async def second_otp_verify(
        request: SecondVerifyOTPRequest,
        service: Annotated[AuthService, Depends()],
        user: Annotated[AuthenticationModel, Depends(HasPermission(RoleType.USER))]
) -> BaseResponse[SuccessResponse]:
    return BaseResponse(data=await service.phone_and_email_otp_verify(**request.model_dump(), user=user))


@router_email_password_login.post(
    "/password_setup",
    name="Create a Password",
    description="Create a Password",
    status_code=status.HTTP_201_CREATED,
    operation_id="password_setup"
)
async def create_password(
        request: PasswordSetup,
        service: Annotated[AuthService, Depends()]
) -> BaseResponse[SuccessResponse]:
    return BaseResponse(data=await service.user_password(**request.model_dump()))


@router_email_password_login.post(
    "/login_with_password",
    name="Login with password",
    status_code=status.HTTP_200_OK,
    description="Login with password",
    operation_id="login_with_password"
)
async def login_password(
        request: PasswordSetup,
        service: Annotated[AuthService, Depends()]
) -> BaseResponse[SuccessResponse]:
    return BaseResponse(data=await service.login_with_password(**request.model_dump()))


@router_email_password_login.post(
    "/forgate_password",
    name="Forgate password",
    status_code=status.HTTP_200_OK,
    description="Forgate password",
    operation_id="forgate_password"
)
async def forgate_password(
        request: EmailRequest,
        service: Annotated[AuthService, Depends()]
) -> BaseResponse[ForgotPasswordResponse]:
    return BaseResponse(data=await service.forgot_password(**request.model_dump()))


@router_email_password_login.post(
    "/password_otp_verify",
    name="Password otp Verify",
    status_code=status.HTTP_200_OK,
    description="Password otp Verify",
    operation_id="password_otp_verify"
)
async def password_verify_otp(
        request: ForgotPasswordVerifyRequest,
        service: Annotated[AuthService, Depends()]
) -> BaseResponse[SuccessResponse]:
    return BaseResponse(data=await service.verify_otp_password(**request.model_dump()))


@router_sso_login.get("/openid/login/{provider}")
async def login_by_provider(request: Request, provider: Annotated[Providers, Path()]) -> RedirectResponse:
    """
    login by provider
    """

    match provider:
        case provider.GOOGLE | provider.FACEBOOK:

            if settings.ENV == AppEnvironment.LOCAL:
                redirect_uri = str(request.url_for("auth", provider=provider.value))
            else:
                redirect_uri = f"{settings.SOCIAL_AUTH_REDIRECT_URL}/{settings.SOCIAL_AUTH_ENDPOINT}/{provider.value}"
            res = (
                await SSOOAuthClient(provider.value)
                .oauth.create_client(provider.value)
                .authorize_redirect(request, redirect_uri)
            )
            return res

        case provider.APPLE:
            if settings.ENV == AppEnvironment.LOCAL:
                redirect_uri = str(request.url_for("auth2", provider=provider.APPLE))
            else:
                redirect_uri = f"{settings.SOCIAL_AUTH_REDIRECT_URL}/{settings.SOCIAL_AUTH_ENDPOINT}/{provider.APPLE}"
            res = (
                await SSOOAuthClient(provider.APPLE)
                .oauth.create_client(provider.APPLE)
                .authorize_redirect(request, redirect_uri)
            )
            return res
        case _:
            return RedirectResponse(url=settings.UI_LOGIN_SCREEN)


@router_sso_login.get(
    "/{provider}",
    status_code=status.HTTP_200_OK,
    response_description="",
    name="auth",
    description="",
    include_in_schema=False,
)
async def auth(
        service: Annotated[AuthService, Depends()], request: Request, provider: Annotated[Providers, Path()]
) -> RedirectResponse:
    """
    get details by provider
    """

    match provider:
        case Providers.GOOGLE:
            user_data = {}
            token = (
                await SSOOAuthClient(provider.value).oauth.create_client(provider.value).authorize_access_token(request)
                )
            user_data.update(
                await SSOOAuthClient(provider.value)
                .oauth.create_client(provider.value)
                .parse_id_token(request, token)
            )
            if provider != Providers.FACEBOOK and provider != Providers.APPLE:
                user_data.update(
                    await SSOOAuthClient(provider.value).oauth.create_client(provider.value).userinfo(token=token)
                )
            return await service.sso_user(token=token.get("id_token"), provider=provider, **user_data)

        case Providers.FACEBOOK:
            token = (
                await SSOOAuthClient(provider.value).oauth.create_client(provider.value).authorize_access_token(request)
            )
            query_params = {"fields": "email", "access_token": token.get("access_token")}
            async with AsyncClient(base_url=settings.FACEBOOK_OIDC_BASE_URL, timeout=None) as session:
                response = await session.get(url=constants.GET_EMAIL, params=query_params)
                if response.status_code in [200, 201, 203, 204]:
                    user_data = response.json()
                    return await service.sso_user(token=token.get("access_token"), provider=provider, **user_data)
                return RedirectResponse(url=settings.ERROR_REDIRECT_URL)


@router_sso_login.post(
    "/{provider}",
    status_code=status.HTTP_200_OK,
    response_description="",
    name="auth2",
    description="",
    include_in_schema=False,
)
async def auth2(
        service: Annotated[AuthService, Depends()], request: Request, provider: Annotated[Providers, Path()]
) -> RedirectResponse:
    """
    get details by provider
    """
    match provider:
        case Providers.APPLE:
            form_data = await request.form()
            apple_token = form_data['id_token']
            user_data = AppleResolver.authenticate(apple_token)
            return await service.sso_user(token=apple_token, provider=provider, **user_data)
