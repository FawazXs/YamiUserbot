from time import sleep
from telethon import events
from pyrogram import filters
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


@app.on_message(filters.command("^.droopy$")
async def typewritter(typew):
                typew.pattern_match.group(1)
                await typew.edit("Hallo.")
                sleep(1)
                await typew.edit(" Hallo..")
                sleep(1)
                await typew.edit("Hallo...")
                sleep(1)
                await typew.edit("⚡️")
                sleep(4)
                await typew.edit("Perkenalkan....")
                sleep(1)
                await typew.edit("Namaku Droopy")
                sleep(1)
                await typew.edit("Droopy 4U")
                sleep(1)
                await typew.edit("Suka Kelapa Montok")
                sleep(1)
                await typew.edit("Ntahlah Gue Suka Cok")
                sleep(1)
                await typew.edit("💀")
                sleep(5)
                await typew.edit("Mending")
                sleep(1)
                await typew.edit("Kalean Semua")
                sleep(1)
                await typew.edit("Offline aja")
                sleep(1)
                await typew.edit("ANJERRRRR")
                sleep(1)
                await typew.edit("Kenapa TT Itu Empuk? ")
                sleep(1)
                await typew.edit("Ya Karena Kalo Gak Empuk")
                sleep(1)
                await typew.edit("TT Nya Tepos...")
                sleep(1)
                await typew.edit("KWKWKWKWKW")
                sleep(1)
                await typew.edit("Asliiii...🥴🥴")
                sleep(1)
                await typew.edit("bwahahaha")
                sleep(1)
                await typew.edit("G J M. ")
                sleep(1)
                await typew.edit("G J M..")
                sleep(1)
                await typew.edit("G J M...")
                sleep(1)
                await typew.edit("G J M....")
                sleep(1)
                await typew.edit("G J M.....?")
                sleep(1)
                await typew.edit("Gua Ganteng Kan....")
                sleep(1)
                await typew.edit("Yakannnn...🥺")
                sleep(1)
                await typew.edit("👉👈")
                sleep(1)
                await typew.edit("Itulah Aku Gabut")
                sleep(1)
                await typew.edit("THE END")
