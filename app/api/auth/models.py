import enum
import uuid

from sqlalchemy import UUID

from app import db

from settings import DB_TBL_PREFIX


class StatusEnum(enum.Enum):
    """Enum for representation auth user status."""
    logined = "logined"
    waiting_qr_login = "waiting qr login"
    error = "error"
    logout = "logout"


class User(db.Model):
    """
    User model.

    Attrs:
        - id (int): user's id
        - phone (str): phone number
        - status (StatusEnum): current auth status
    """
    __tablename__ = f"{DB_TBL_PREFIX}user"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    phone_number = db.Column(
        db.String(16),
        nullable=False,
        index=True,
        default="",
        unique=True
    )
    status = db.Column(
        db.String(32),
        nullable=False,
        default=StatusEnum.waiting_qr_login.value
    )
