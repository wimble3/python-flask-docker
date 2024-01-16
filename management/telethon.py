from flask import Blueprint

from app.telegram.telethon import client

bp = Blueprint("telethon", __name__)


@bp.cli.command("run", help="run telethon bot")
def run():
    with client:
        client.run_until_disconnected()
