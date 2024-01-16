from flask import Response  # noqa: F401

from flask import Blueprint, jsonify

from flask_swagger_ui import get_swaggerui_blueprint

from app.swagger_ui.helpers import create_spec


bp = Blueprint("swagger", __name__, url_prefix="/api")

# swagger urls
SWAGGER_URL = "/api/docs/"
API_URL = "/api/swagger/"

# registration swagger urls
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "python-flask-docker"}
)


@bp.route("/swagger/")
def create_swagger_spec():
    """
    Creates swagger docs and sends it in json.
    Returns:
        Response
    """
    spec = create_spec()
    return jsonify(spec.to_dict())
