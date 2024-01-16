from marshmallow import fields, Schema

from app.helpers.schemas import BinaryResponseSchema


class UserLoginSchema(Schema):
    """Schema for user loging."""
    phone_number = fields.Str(required=True, example="+79507206578")


class QRCodeResponseSchema(BinaryResponseSchema):
    """Schema for server response contains qr code."""
    qrcode_link = fields.Str(required=True, example="http://localhost...")

