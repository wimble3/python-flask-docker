from telethon import events

from app.telegram.telethon import client


@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    """@@@"""
    await event.respond("Hello!")
