import re

from pydantic import field_validator, EmailStr, BaseModel, model_validator

import constants
from core.exceptions import INVALIDARGUMENT
from core.utils import strong_password
from config import settings


class OtpRequest(BaseModel):
    """Request object for creating a new authentication."""
    if settings.PASSWORD_LESS_PHONE == True and settings.PASSWORD_LESS_EMAIL == False:
        phone_number: str | None = None

    elif settings.PASSWORD_LESS_EMAIL == True and settings.PASSWORD_LESS_PHONE == False:
        email: EmailStr | None = None
    else:
        raise INVALIDARGUMENT()

    @model_validator(mode="before")
    @classmethod
    def validate_input(cls, _v):
        """Validate that either email or phone is required, but not both, and return the validated value."""
        if _v.get("phone_number") is None and _v.get("email") is None:
            raise ValueError("Either email or phone should be required")
        if _v.get("phone_number") is not None and _v.get("email") is not None:
            raise ValueError("Either email or phone only one should be required")
        return _v

    @classmethod
    @field_validator("phone_number")
    def validate_phone_number(cls, _v: str) -> str | None:
        """
    Validation of phone number for creating users.
    """
        if not _v or not re.match(r"^\+?[789]\d{9}$", _v, re.I):
            raise ValueError(constants.INVALID_PHONE_NUMBER)
        return _v


class VerifyOTPRequest(BaseModel):
    """
    Request model for verifying OTP.
    """

    if settings.PASSWORD_LESS_PHONE == True and settings.PASSWORD_LESS_EMAIL == False:
        phone_number: str | None = None

    elif settings.PASSWORD_LESS_EMAIL == True and settings.PASSWORD_LESS_PHONE == False:
        email: EmailStr | None = None
    else:
        print("not one select")
    otp: int

    @model_validator(mode="before")
    @classmethod
    def validate_input(cls, values):
        """Validate that either email or phone is required, but not both, and return the validated value."""
        if values.get("phone_number") is None and values.get("email") is None:
            raise ValueError("Either email or phone should be required")
        if values.get("phone_number") is not None and values.get("email") is not None:
            raise ValueError("Either email or phone only one should be required")
        return values

    @classmethod
    @field_validator("phone_number")
    def validate_phone_number(cls, _v: str) -> str | None:
        """
    Validation of phone number for creating users.
    """
        if not _v or not re.match(r"^\+?[789]\d{9}$", _v, re.I):
            raise ValueError(constants.INVALID_PHONE_NUMBER)
        return _v


class SecondOtpRequest(BaseModel):
    """
    Request object for creating a new authentication.
    """
    if settings.PASSWORD_LESS_PHONE == True and settings.PASSWORD_LESS_EMAIL == False:
        email: EmailStr | None = None

    elif settings.PASSWORD_LESS_EMAIL == True and settings.PASSWORD_LESS_PHONE == False:
        phone_number: str | None = None
    else:
        print("not one select")

    @model_validator(mode="before")
    @classmethod
    def validate_input(cls, _v):
        """Validate that either email or phone is required, but not both, and return the validated value."""
        if _v.get("phone_number") is None and _v.get("email") is None:
            raise ValueError("Either email or phone should be required")
        if _v.get("phone_number") is not None and _v.get("email") is not None:
            raise ValueError("Either email or phone only one should be required")
        return _v

    @classmethod
    @field_validator("phone_number")
    def validate_phone_number(cls, _v: str) -> str | None:
        """
    Validation of phone number for creating users.
    """
        if not _v or not re.match(r"^\+?[789]\d{9}$", _v, re.I):
            raise ValueError(constants.INVALID_PHONE_NUMBER)
        return _v


class SecondVerifyOTPRequest(BaseModel):
    """
    Request model for verifying OTP.
    """

    if settings.PASSWORD_LESS_PHONE == True and settings.PASSWORD_LESS_EMAIL == False:
        email: EmailStr | None = None

    elif settings.PASSWORD_LESS_EMAIL == True and settings.PASSWORD_LESS_PHONE == False:
        phone_number: str | None = None
    else:
        print("not one select")
    otp: int

    @model_validator(mode="before")
    @classmethod
    def validate_input(cls, values):
        """Validate that either email or phone is required, but not both, and return the validated value."""
        if values.get("phone_number") is None and values.get("email") is None:
            raise ValueError("Either email or phone should be required")
        if values.get("phone_number") is not None and values.get("email") is not None:
            raise ValueError("Either email or phone only one should be required")
        return values

    @classmethod
    @field_validator("phone_number")
    def validate_phone_number(cls, value: str | None) -> str | None:
        """
    Validation of phone number for creating users.
    """
        if not value or not re.match(r"^\+?[789]\d{9}$", value, re.I):
            raise ValueError(constants.INVALID_PHONE_NUMBER)
        return value


class PasswordSetup(BaseModel):
    email: EmailStr | None = None
    password: str

    @classmethod
    @field_validator("password")
    def password_validate(cls, password: str) -> str:
        if not strong_password(password=password):
            raise ValueError(constants.WEAK_PASSWORD)
        return password


class EmailRequest(BaseModel):
    email: EmailStr


class ForgotPasswordVerifyRequest(BaseModel):
    token: str
    new_password: str

    @classmethod
    @field_validator("new_password")
    def password_validate(cls, new_password: str) -> str:
        if not strong_password(password=new_password):
            raise ValueError(constants.WEAK_PASSWORD)
        return new_password
