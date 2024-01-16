import logging

from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.api.auth.models import User


def create_user(phone_number):
    """
    Creates user in db.
    Args:
        phone_number (str): user's phone number

    Returns:
        User | bool: user if user has been created or exists else False
    """
    try:
        user = User.query.filter_by(phone_number=phone_number).first()
        if user:
            return user

        user = User(phone_number=phone_number)
        db.session.add(user)
        db.session.commit()
        return user
    except SQLAlchemyError as e:
        logging.warning(f"User has not been created {e}")
        return False
