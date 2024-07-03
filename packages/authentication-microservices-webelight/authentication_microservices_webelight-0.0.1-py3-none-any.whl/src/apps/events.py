from fastapi import FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache
from sqlalchemy.orm import Session

from apps.authentication.services import AuthService
from config import settings
from core.utils import logger


def startup_events(_app: FastAPI) -> None:
    """
    Define startup events for the FastAPI application.
    """
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=settings.REDIS_URL,
        prefix=settings.APP_NAME,
        response_header=f"X-{settings.APP_NAME}-Cache",
        ignore_arg_types=[Request, Response, Session, AuthService],
    )


def shutdown_events(_app: FastAPI):
    """
    Define shutdown events for the FastAPI application.
    """
    logger.info("Adding shutdown functions...")
