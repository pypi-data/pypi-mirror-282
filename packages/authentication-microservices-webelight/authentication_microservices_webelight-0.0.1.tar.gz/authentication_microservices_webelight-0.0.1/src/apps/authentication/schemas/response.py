from uuid import UUID

from core.utils import CamelCaseModel


class SendOtpResponse(CamelCaseModel):
    """
    Response model for sending OTP.
    """

    otp: str


class AccessResponse(CamelCaseModel):
    message: str = "OTP verified successfully"
    access_token: str
    refresh_token: str


class ForgotPasswordResponse(CamelCaseModel):
    url: str
