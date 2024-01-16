from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from apispec_webframeworks.flask import FlaskPlugin

from flask import current_app

from marshmallow import Schema

from app import app

from settings import (
    APISPEC_OPENAPI_VER,
    APISPEC_SERVER,
    APISPEC_SERVER_DESC,
    APISPEC_TITLE,
    APISPEC_VERSION,
    SWAGGER_FILENAME,
)


def add_security_scheme(documentation):
    """
    Adds security schemas.
    Args:
        documentation (APISpec): app documentation

    Returns:
        None:
    """
    auth_schema = {"type": "http", "scheme": "basic"}
    documentation.components.security_scheme("BasicAuth", auth_schema)
    auth_cookie_schema = {"type": "apiKey", "in": "cookie", "name": "session"}
    documentation.components.security_scheme("cookieAuth", auth_cookie_schema)


def add_responses(documentation):
    """
    Adds the most useful response codes.
    Args:
        documentation (APISpec): app documentation

    Returns:
        None:
    """
    response_400 = {
        "description": "Данные введены некорректно!",
        "content": {
            "application/json": {
                "schema": "BinaryResponseSchema",
                "examples": {
                    "Bad Request": {
                        "value": {
                            "message": "Неверный формат введенных данных",
                            "result": False,
                        }
                    }
                },
            }
        },
    }
    response_401 = {
        "description": "Ошибка авторизации!",
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "сообщение с сервера!",
                        },
                        "result": {"type": "boolean"},
                    },
                },
                "examples": {
                    "Invalid token": {
                        "value": {
                            "message": "Время жизни токена закончилось!!",
                            "result": False,
                        }
                    },
                    "No token": {
                        "value": {
                            "message": "Пользователь не авторизован!",
                            "result": False,
                        }
                    },
                },
            }
        },
    }
    response_403 = {
        "description": "Недостаточно прав!",
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "сообщение с сервера!",
                        },
                        "result": {"type": "boolean"},
                    },
                },
                "examples": {
                    "403 Forbidden": {
                        "value": {
                            "message": "Недостаточно прав!",
                            "result": False,
                        }
                    },
                },
            }
        },
    }
    response_415 = {
        "description": "Формат входных данных JSON",
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "description": "Сообщение о результатах регистрации",
                    "properties": {
                        "message": {"type": "string"},
                        "result": {"type": "boolean"},
                    },
                },
                "examples": {
                    "No JSON": {
                        "value": {
                            "message": "Формат входных данных JSON!!",
                            "result": False,
                        }
                    }
                },
            }
        },
    }

    documentation.components.response("BadRequest", response_400)
    documentation.components.response("Unauthorized", response_401)
    documentation.components.response("NoJson", response_415)
    documentation.components.response("Forbidden", response_403)


def add_schemas(documentation):
    """
    Adds schemas containing in app.
    Args:
        documentation (APISpec): app documentation

    Returns:
        None:
    """
    documentation.components.example(
        component_id="RegUserSchema",
        component={
            "value": {"password": "123",
                      "username": "name",
                      "email": "name@m.com"}
        },
    )

    for schema in Schema.__subclasses__():
        if schema.__name__ == "SQLAlchemySchema" \
                or schema.__name__ == "Schema":
            continue
        with app.app_context():
            documentation.components.schema(schema.__name__, schema=schema)


def add_view_to_docs(documentation):
    """
    Adds methods of apps in docs.
    Description will be thrown from doc-string.
    Args:
        documentation (APISpec): app documentation

    Returns:
        None:
    """
    for fn_name in app.view_functions:
        if "api" in fn_name and "flask-apispec" not in fn_name:
            view_fn = app.view_functions[fn_name]
            with app.app_context():
                documentation.path(view=view_fn)


def write_docs_to_file(documentation):
    """
    Writes doc in yaml file.
    Args:
        documentation (APISpec): app documentation

    Returns:
        None:
    """
    try:
        file = open(SWAGGER_FILENAME, "w")
        with app.app_context():
            print(documentation.to_yaml(), file=file)
        file.close()
    except PermissionError:
        current_app.logger.info(
            f"No rights for file creation: {SWAGGER_FILENAME}."
        )


def create_spec():
    """
    Creates docs and saves in yaml file.
    Returns:
        None:
    """
    apispec = APISpec(
        title=APISPEC_TITLE,
        version=APISPEC_VERSION,
        plugins=[MarshmallowPlugin(), FlaskPlugin()],
        openapi_version=APISPEC_OPENAPI_VER,
        servers=[{"url": APISPEC_SERVER, "description": APISPEC_SERVER_DESC}],
    )

    add_security_scheme(apispec)
    add_responses(apispec)
    add_schemas(apispec)
    add_view_to_docs(apispec)
    write_docs_to_file(apispec)
    return apispec


if __name__ == "__main__":
    create_spec()
