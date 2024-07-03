import os

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.sessions import SessionMiddleware
# from starlette.middleware.sessions import SessionMiddleware

import constants

from apps.events import startup_events, shutdown_events
from apps.handlers import start_exception_handlers
from apps.authentication.controllers import router_email_password_login, router_password_less, router_sso_login
from config import settings


def init_routers(_app: FastAPI) -> None:
    """
    Initialize all routers.
    """

    # _app.include_router(auth_router)
    password_less_login = settings.PASSWORD_LESS_LOGIN
    sso_login = settings.SSO_LOGIN
    email_password_login = settings.EMAIL_PASSWORD_LOGIN

    if sso_login== True:
        if password_less_login==True:
            _app.include_router(router_password_less)
            _app.include_router(router_sso_login)

        elif email_password_login==True:
            _app.include_router(router_email_password_login)
            _app.include_router(router_sso_login)

        else:
            _app.include_router(router_sso_login)
    elif password_less_login==True:
        _app.include_router(router_password_less)
    else:
        _app.include_router(router_email_password_login)

def root_health_path(_app: FastAPI) -> None:
    """
    Health Check Endpoint.
    """

    @_app.get("/", include_in_schema=False)
    def root() -> JSONResponse:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": constants.SUCCESS})

    @_app.get("/healthcheck", include_in_schema=False)
    def healthcheck() -> JSONResponse:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": constants.SUCCESS})


def init_middlewares(_app: FastAPI) -> None:
    """
    Middleware initialization.
    """
    _app.add_middleware(
        CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
    )
    _app.add_middleware(SessionMiddleware, secret_key="Uqn7rDayJJi4zoQgUZS6zlenOmMXSFcawibJSIHMhG")


def create_app(debug: bool = False) -> FastAPI:
    """
    Create a Initialize the FastAPI app.
    """
    _app = FastAPI(
        title=settings.APP_NAME, version=settings.APP_VERSION, docs_url="/docs", redoc_url="/redoc" if debug else None
    )
    init_routers(_app)
    root_health_path(_app)
    init_middlewares(_app)
    start_exception_handlers(_app)
    startup_events(_app)
    shutdown_events(_app)
    return _app


debug_app = create_app(debug=True)
production_app = create_app()
