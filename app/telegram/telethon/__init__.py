from settings import TELETHON_SESSION, TELETHON_API_ID, TELETHON_API_HASH

from telethon import TelegramClient

client = TelegramClient(TELETHON_SESSION, TELETHON_API_ID, TELETHON_API_HASH)
