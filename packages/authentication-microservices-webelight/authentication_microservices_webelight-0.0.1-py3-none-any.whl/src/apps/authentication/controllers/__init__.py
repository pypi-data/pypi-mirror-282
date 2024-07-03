from apps.authentication.controllers.auth import router_sso_login as router_sso_login
from apps.authentication.controllers.auth import router_password_less as router_password_less
from apps.authentication.controllers.auth import router_email_password_login as router_email_password_login

__all__ = ["router_sso_login","router_password_less","router_email_password_login"]
