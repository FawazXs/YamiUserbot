from time import sleep
from pyrogram import filters
from telethon import events
from pyrogram.types import Message

from telethon.events import register
from _pyrogram import app, CMD_HELP
from _pyrogram.helpers.utils import get_message_type, Types
import asyncio


CMD_HELP.update(
    {
        "animation": """
**📕 MODULE ANIMATION:**
`━━━━━━━━━━━━━━━━━━━`
`animation` ⇛ ketik .droopy untuk melihat animasi ketikan.
"""
    }
)


@register(outgoing=True, pattern="^.droopy$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Hallo.")
        sleep(1)
        await e.edit("Hallo..")
        sleep(1)
        await e.edit("Hallo...")
        sleep(1)
        await e.edit("⚡️")
        sleep(4)
        await e.edit("Perkenalkan....")
        sleep(1)
        await e.edit("Namaku Droopy")
        sleep(1)
        await e.edit("Droopy 4U")
        sleep(1)
        await e.edit("Suka Kelapa Montok")
        sleep(1)
        await e.edit("Ntahlah Gue Suka Cok")
        sleep(1)
        await e.edit("💀")
        sleep(5)
        await e.edit("Mending")
        sleep(1)
        await e.edit("Kalean Semua")
        sleep(1)
        await e.edit("Offline aja")
        sleep(1)
        await e.edit("ANJERRRRR")
        sleep(1)
        await e.edit("Kenapa TT Itu Empuk? ")
        sleep(1)
        await e.edit("Ya Karena Kalo Gak Empuk")
        sleep(1)
        await e.edit("TT Nya Tepos...")
        sleep(1)
        await e.edit("KWKWKWKWKW")
        sleep(1)
        await e.edit("Asliiii...🥴🥴")
        sleep(1)
        await e.edit("bwahahaha")
        sleep(1)
        await e.edit("G J M. ")
        sleep(1)
        await e.edit("G J M..")
        sleep(1)
        await e.edit("G J M...")
        sleep(1)
        await e.edit("G J M....")
        sleep(1)
        await e.edit("G J M.....?")
        sleep(1)
        await e.edit("Gua Ganteng Kan....")
        sleep(1)
        await e.edit("Yakannnn...🥺")
        sleep(1)
        await e.edit("👉👈")
        sleep(1)
        await e.edit("Itulah Aku Gabut")
        sleep(1)
        await e.edit("THE END")
