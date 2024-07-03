import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import field_validator
from pydantic_settings import BaseSettings
from strenum import StrEnum

load_dotenv(override=True)


class AppEnvironment(StrEnum):
    """
    Local: Indicates that the application is running on a local machine or environment.
    Development: Indicates that the application is running in a development environment.
    Production: Indicates that the application is running in a production environment.
    Test: Indicates that the application is running in a test environment.
    """

    LOCAL = "Local"
    DEVELOPMENT = "Development"
    PRODUCTION = "Production"


class Settings(BaseSettings):
    """
    A settings class for the project defining all the necessary parameters within the
    app through an object.
    """

    # App variables
    ENV: str = os.getenv("ENV", AppEnvironment.LOCAL.value)
    APP_NAME: str | None = os.getenv("APP_NAME")
    APP_VERSION: str | None = os.getenv("APP_VERSION")
    APP_HOST: str | None = os.getenv("APP_HOST")
    APP_PORT: Optional[int] = os.getenv("APP_PORT")  # type: ignore
    APP_DEBUG: Optional[bool] = os.getenv("APP_DEBUG")  # type: ignore
    APP_CONTAINER: Optional[bool] = os.getenv("APP_CONTAINER")  # type: ignore

    # JWT Token variables
    JWT_SECRET_KEY: str | None = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str | None = os.getenv("JWT_ALGORITHM")
    COOKIES_DOMAIN: Optional[str] = os.getenv("COOKIES_DOMAIN")
    ACCESS_TOKEN_EXP: Optional[int] = os.getenv("ACCESS_TOKEN_EXP")  # type: ignore
    REFRESH_TOKEN_EXP: Optional[int] = os.getenv("REFRESH_TOKEN_EXP")  # type: ignore

    DATABASE_USER: str | None = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD: str | None = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST: str | None = os.getenv("DATABASE_HOST")
    DATABASE_PORT: str | None = os.getenv("DATABASE_PORT")
    DATABASE_NAME: str | None = os.getenv("DATABASE_NAME")
    DATABASE_URL: str | None = os.getenv("DATABASE_URL")

    FORGET_PASSWORD_URL: str | None = os.getenv("FORGET_PASSWORD_URL")

    REDIS_HOST: Optional[str] = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: Optional[int] = os.getenv("REDIS_PORT", 6380)

    SOCIAL_AUTH_REDIRECT_URL: str | None = os.getenv("SOCIAL_AUTH_REDIRECT_URL")
    SOCIAL_AUTH_ENDPOINT: str | None = os.getenv("SOCIAL_AUTH_ENDPOINT")

    GOOGLE_CLIENT_ID: str | None = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: str | None = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_METADATA_URL: str | None = os.getenv("GOOGLE_METADATA_URL")
    GOOGLE_SCOPE: str | None = os.getenv("GOOGLE_SCOPE")

    FACEBOOK_CLIENT_ID: str | None = os.getenv("FACEBOOK_CLIENT_ID")
    FACEBOOK_CLIENT_SECRET: str | None = os.getenv("FACEBOOK_CLIENT_SECRET")
    FACEBOOK_METADATA_URL: str | None = os.getenv("FACEBOOK_METADATA_URL")
    FACEBOOK_SCOPE: str | None = os.getenv("FACEBOOK_SCOPE")
    FACEBOOK_ACCESS_TOKEN_URL: str | None = os.getenv("FACEBOOK_ACCESS_TOKEN_URL")
    FACEBOOK_OIDC_BASE_URL: str | None = os.getenv("FACEBOOK_OIDC_BASE_URL")

    APPLE_CLIENT_ID: str | None = os.getenv("APPLE_CLIENT_ID")
    APPLE_METADATA_URL: str | None = os.getenv("APPLE_METADATA_URL")
    APPLE_AUTH_URL: str | None = os.getenv("APPLE_AUTH_URL")
    APPLE_SCOPE: str | None = os.getenv("APPLE_SCOPE")
    RESPONSE_MODE: str | None = os.getenv("RESPONSE_MODE")
    RESPONSE_TYPE: str | None = os.getenv("RESPONSE_TYPE")
    APPLE_KEYS_URL: str | None = os.getenv("APPLE_KEYS_URL")

    OTP_LOGIN_PHONE_NUMBER: str | None = os.getenv("OTP_LOGIN_PHONE_NUMBER")
    OTP_LOGIN_EMAIL: str | None = os.getenv("OTP_LOGIN_EMAIL")
    REDIS_URL: str | None = os.getenv("REDIS_URL")

    UI_LOGIN_SCREEN: str | None = os.getenv("UI_LOGIN_SCREEN")

    LOGIN_WITH_PHONE: str | None = os.getenv("LOGIN_WITH_PHONE")
    LOGIN_WITH_EMAIL: str | None = os.getenv("LOGIN_WITH_EMAIL")
    EXPIRES_OTP: str | None = os.getenv("EXPIRES_OTP")

    ERROR_REDIRECT_URL: str | None = os.getenv("ERROR_REDIRECT_URL")

    PASSWORD_LESS_LOGIN: Optional[bool] = os.getenv("PASSWORD_LESS_LOGIN")
    SSO_LOGIN: Optional[bool] = os.getenv("SSO_LOGIN")
    SSO_WITH_PASSWORD_LESS: Optional[bool] = os.getenv("SSO_WITH_PASSWORD_LESS")
    EMAIL_PASSWORD_LOGIN: Optional[bool] = os.getenv("EMAIL_PASSWORD_LOGIN")
    PASSWORD_LESS_EMAIL: Optional[bool] =os.getenv("PASSWORD_LESS_EMAIL")
    PASSWORD_LESS_PHONE: Optional[bool] =os.getenv("PASSWORD_LESS_PHONE")
    SSO_GOOGLE: Optional[bool] =os.getenv("SSO_GOOGLE")
    SSO_FACEBOOK: Optional[bool] =os.getenv("SSO_FACEBOOK")
    SSO_APPLE: Optional[bool] =os.getenv("SSO_APPLE")



    @field_validator("DATABASE_URL", mode="before")
    def assemble_db_url(cls, val, values) -> str:
        """
        Create a Database URL from the settings provided in the .env file.
        """
        if isinstance(val, str):
            return val

        database_user = values.data.get("DATABASE_USER")
        database_password = values.data.get("DATABASE_PASSWORD")
        database_host = values.data.get("DATABASE_HOST")
        database_port = values.data.get("DATABASE_PORT").replace('"', "")
        database_name = values.data.get("DATABASE_NAME")

        if not all([database_user, database_password, database_host, database_port, database_name]):
            raise ValueError("Incomplete database connection information")

        return (
            f"postgresql+asyncpg://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}"
        )

    @property
    def is_production(self) -> bool:
        """
        Check if the app is running in production mode.
        """
        return self.ENV == AppEnvironment.PRODUCTION

    @property
    def is_development(self) -> bool:
        """
        Check if the app is running in development mode.
        """
        return self.ENV == AppEnvironment.DEVELOPMENT

    @property
    def is_local(self) -> bool:
        """
        Check if the app is running in local mode.
        """
        return self.ENV == AppEnvironment.LOCAL


settings = Settings()
