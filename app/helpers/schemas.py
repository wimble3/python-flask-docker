from marshmallow import Schema, fields


class BinaryResponseSchema(Schema):
    """Schema for common binary server response."""
    message = fields.Str(example="Server response message!")
    result = fields.Bool(example=True)

