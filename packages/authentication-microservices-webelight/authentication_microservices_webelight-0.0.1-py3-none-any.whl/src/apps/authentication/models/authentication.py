import uuid
from typing import Self, Optional
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base
from core.utils.mixins import TimeStampMixin


class AuthenticationModel(Base, TimeStampMixin):
    __tablename__ = "authentication"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    phone_number: Mapped[str | None] = mapped_column(nullable=True)
    email: Mapped[str | None] = mapped_column(nullable=True)
    password: Mapped[str | None] = mapped_column()
    is_phone_verify: Mapped[bool] = mapped_column(default=False)
    is_email_verify: Mapped[bool] = mapped_column(default=False)
    verified_user: Mapped[bool] = mapped_column(default=False)

    @classmethod
    def create(
            cls,
            phone_number: str= None,
            email: Optional[str] = None,
            is_phone_verify: Optional[bool] = None,
            password: Optional[str] = None,
            is_email_verify: Optional[bool] = None,
            verified_user: Optional[bool] = None
    ) -> Self:
        """`create()`: Creates a new User."""
        return cls(
            id=uuid.uuid4(),
            phone_number=phone_number,
            email=email.lower() if email else None,
            password=password,
            is_phone_verify=is_phone_verify,
            is_email_verify=is_email_verify,
            verified_user=verified_user,
        )
