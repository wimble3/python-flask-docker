import os

from dotenv import load_dotenv


load_dotenv()

# App
HOST = os.getenv("HOST")
DEBUG = bool(os.getenv("DEBUG"))
PORT = int(os.getenv("PORT"))
DB_TBL_PREFIX = os.getenv("DB_TBL_PREFIX")
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
SECRET_KEY = os.getenv("SECRET_KEY")

# Api spec
APISPEC_TITLE = os.getenv("APISPEC_TITLE")
APISPEC_VERSION = os.getenv("APISPEC_VERSION")
APISPEC_OPENAPI_VER = os.getenv("APISPEC_OPENAPI_VER")
APISPEC_SERVER = os.getenv("APISPEC_SERVER")
APISPEC_SERVER_DESC = os.getenv("APISPEC_SERVER_DESC")
SWAGGER_FILENAME = os.getenv("SWAGGER_FILENAME")

# Telethon
TELETHON_API_ID = os.getenv("TELETHON_API_ID")
TELETHON_API_HASH = os.getenv("TELETHON_API_HASH")
TELETHON_SESSION = os.getenv("TELETHON_SESSION")
TELETHON_QR_FOLDER = os.getenv("TELETHON_QR_FOLDER")

# Redis
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_DB = int(os.getenv("REDIS_DB"))
