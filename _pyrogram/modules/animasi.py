from time import sleep
from telethon import events
from pyrogram import filters
from pyrogram.types import Message

from telethon.events import register
from _pyrogram import app, CMD_HELP
from config import PREFIX
from _pyrogram.helpers.utils import get_message_type, Types
import asyncio


CMD_HELP.update(
    {
        "animation": """
**📕 MODULE ANIMATION:**
`━━━━━━━━━━━━━━━━━`
`usage` ⇛ ketik .droopy untuk melihat animasi ini.
`usage` ⇛ ketik .kevincan untuk melihat animasi ini.
`usage` ⇛ ketik .pantau untuk melihat animasi ini.
`usage` ⇛ ketik .mengsad untuk melihat animasi ini.
`usage` ⇛ ketik .hati untuk melihat animasi ini.
"""
    }
)


@app.on_message(filters.command("hati", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("`\n(\\_/)`"
                 "`\n(●_●)`"
                 "`\n />❤️ *Ini Buat Kamu`")
    sleep(3)
    await e.edit("`\n(\\_/)`"
                 "`\n(●_●)`"
                 "`\n/>💔  *Aku Ambil Lagi`")
    sleep(2)
    await e.edit("`\n(\\_/)`"
                 "`\n(●_●)`"
                 "`\n💔<\\  *Terimakasih`")



@app.on_message(filters.command("mengsad", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("`kamu itu cantik..`")
    sleep(1)
    await e.edit("`dan kamu juga manis..`")
    sleep(1)
    await e.edit("`baik hati 🥺`")
    sleep(1)
    await e.edit("`dan penyayang 🥰`")
    sleep(1)
    await e.edit("`tapi sayang...`")
    sleep(1)
    await e.edit("`kamu bukan jodoh aku 😔`")
    
    
# created by levina, under this cloning from geez userbot


@app.on_message(filters.command("pantau", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("`\n┻┳|―-∩`"
                 "`\n┳┻|     ヽ`"
                 "`\n┻┳|    ● |`"
                 "`\n┳┻|▼) _ノ`"
                 "`\n┻┳|￣  )`"
                 "`\n┳ﾐ(￣ ／`"
                 "`\n┻┳T￣|`"
                 "\n**masih gw pantau anj.**")
