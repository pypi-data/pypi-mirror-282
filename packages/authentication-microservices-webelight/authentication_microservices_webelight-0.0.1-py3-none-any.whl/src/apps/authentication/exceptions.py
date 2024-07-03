import constants
from core.exceptions import CustomException, UnauthorizedError


class DuplicateEmailException(CustomException):
    """
    Custom exception for email duplication.
    """

    message = constants.DUPLICATE_EMAIL


class InvalidCredentialsException(UnauthorizedError):
    """
    Custom exception to show a generic error message.
    """

    message = constants.INVALID_CREDS


class PhoneIsalReadyExists(CustomException):
    message = constants.PHONE_IS_EXIST


class MobileAlreadyVerified(CustomException):
    message = constants.MOBILE_ALREADY_VERIFIED


class CantUpdateMobile(CustomException):
    message = constants.CANT_UPDATE_MOBILE


class CantUpdateEmail(CustomException):
    message = constants.CANT_UPDATE_EMAIL


class EmailAlreadyVerified(CustomException):
    message = constants.EMAIL_ALREADY_EXIST


class BothAreAlreadyVerified(CustomException):
    message = constants.BOTH_ARE_ALREADY_EXIST
