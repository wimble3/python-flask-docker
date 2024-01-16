from flask import Blueprint, request

from app.api.auth.helpers import create_user
from app.api.auth.schemas import UserLoginSchema, \
    QRCodeResponseSchema  # noqa: F401
from app.helpers.schemas import BinaryResponseSchema  # noqa: F401
from app.helpers.services import QRCodeService, FileService
from settings import TELETHON_QR_FOLDER

bp = Blueprint("api_auth", __name__, url_prefix="/api/auth")


@bp.route("/login/", methods=["POST"])
def login():
    """
    ---
    post:
        summary: Авторизация
        requestBody:
            content:
                Application/json:
                    schema: UserLoginSchema
        responses:
            '200':
                content:
                    application/json:
                        schema: QRCodeResponseSchema
            '400':
                description: Incorrect format
                content:
                    application/json:
                        schema: BinaryResponseSchema
                        example:
                            message: Phone number is not correct
                            result: false
            '415': NoJson
        tags:
            - Auth
    """
    # validation
    data = request.json
    phone_number = data.get("phone_number")

    user = create_user(phone_number=phone_number)

    if not user:
        return BinaryResponseSchema().dump({
            "message": "Missing connection with database",
            "result": False

        })

    qrcode_img = QRCodeService.generate_qrcode(phone_number)
    # @@@

    return QRCodeResponseSchema().dump({
        "message": "QR code has been created successfully",
        "result": True,
        "qrcode_link": "http://localost..."
    })
