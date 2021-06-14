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
        "animation2": """
**📕 MODULE ANIMATION 2:**
`━━━━━━━━━━━━━━━━━━`
`usage` ⇛ ketik .darling
`usage` ⇛ ketik .zombi
`usage` ⇛ ketik .djokes
"""
    }
)


@app.on_message(filters.command("darling", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("I LOVE YOU BEB 💕")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💗💕")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG KAMU 💝💖💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SELAMANYA 💕")
    await e.edit("💘💘💘💘")
    await e.edit("CINTA")
    await e.edit("KAMU")
    await e.edit("SELAMANYA")
    await e.edit("KAMU")
    await e.edit("PUJAAN HATIKU")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY DARLING 🥰")
    await e.edit("💕💞💘💝")
    await e.edit("💘💕💞💝")
    await e.edit("SAYANG KAMU 💞")
    
    
@app.on_message(filters.command("zombi", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/". "#", "@", "!"):
    await e.edit("`ZO.. ZOMBIEEE...`")
    sleep(1)
    await e.edit("`LARII ADA ZOMBIEEE...`")
    sleep(1)
    await e.edit("`🏃                        🧟‍♀️`")
    await e.edit("`🏃                       🧟‍♀️`")
    await e.edit("`🏃                      🧟‍♀️`")
    await e.edit("`🏃                     🧟‍♀️`")
    await e.edit("`🏃   `LARII`          🧟‍♀️`")
    await e.edit("`🏃                   🧟‍♀️`")
    await e.edit("`🏃                  🧟‍♀️`")
    await e.edit("`🏃                 🧟‍♀️`")
    await e.edit("`🏃                🧟‍♀️`")
    await e.edit("`🏃               🧟‍♀️`")
    await e.edit("`🏃              🧟‍♀️`")
    await e.edit("`🏃             🧟‍♀️`")
    await e.edit("`🏃            🧟‍♀️`")
    await e.edit("`🏃           🧟‍♀️`")
    await e.edit("`🏃 TIDAK!!  🧟‍♀️`")
    await e.edit("`🏃           🧟‍♀️`")
    await e.edit("`🏃            🧟‍♀️`")
    await e.edit("`🏃             🧟‍♀️`")
    await e.edit("`🏃              🧟‍♀️`")
    await e.edit("`🏃               🧟‍♀️`")
    await e.edit("`🏃                🧟‍♀️`")
    await e.edit("`🏃                 🧟‍♀️`")
    await e.edit("`🏃                  🧟‍♀️`")
    await e.edit("`🏃                   🧟‍♀️`")
    await e.edit("`🏃                    🧟‍♀️`")
    await e.edit("`🏃                     🧟‍♀️`")
    await e.edit("`🏃  Huft Capek        🧟‍♀️`")
    await e.edit("`🏃                   🧟‍♀️`")
    await e.edit("`🏃                  🧟‍♀️`")
    await e.edit("`🏃                 🧟‍♀️`")
    await e.edit("`🏃                🧟‍♀️`")
    await e.edit("`🏃               🧟‍♀️`")
    await e.edit("`🏃              🧟‍♀️`")
    await e.edit("`🏃             🧟‍♀️`")
    await e.edit("`🏃            🧟‍♀️`")
    await e.edit("`🏃           🧟‍♀️`")
    await e.edit("`🏃          🧟‍♀️`")
    await e.edit("`🏃         🧟‍♀️`")
    await e.edit("`DIA SEMAKIN MENDEKAT!!!`")
    sleep(1)
    await e.edit("`🏃       🧟‍♀️`")
    await e.edit("`🏃      🧟‍♀️`")
    await e.edit("`🏃     🧟‍♀️`")
    await e.edit("`🏃    🧟‍♀️`")
    await e.edit("`Habislah Aku...`")
    sleep(1)
    await e.edit("🧟‍♂️")
    sleep(3)
    await e.edit("`ARRGGHHHHH`")
    await e.edit("😱")
    sleep(3)
    await e.edit("`DEATH ☠️`")
    
    
@app.on_message(filters.command("djokes", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("`dark jokes kuy..`")
    sleep(1)
    await e.edit("`kuylah gass...`")
    sleep(1)
    await e.edit("`😈 YOK MULAIII`")
    sleep(1)
    await e.edit("`orang buntung ngak pernah masuk surga..`")
    sleep(1)
    await e.edit("`karna apa?..`")
    sleep(1)
    await e.edit("`karena wudhunya tidak pernah sah..`")
    sleep(2)
    await e.edit("`okok, lagi lagi...`")
    sleep(1)
    await e.edit("`bagaimana cara orang buntung makan?..`")
    sleep(1)
    await e.edit("`apakah cara makannya sama seperti ayam?..`")
    sleep(2)
    await e.edit("`okok ini yg terakhir..`")
    sleep(1)
    await e.edit("`kegiatan pramuka disinyalir diskriminatif..`")
    sleep(1)
    await e.edit("`tau kenapa?...`")
    sleep(1)
    await e.edit("`karena yang tangannya buntung tidak bisa tepuk pramuka..`")
    sleep(1)
    await e.edit("`sekian, terimakasih..`")
