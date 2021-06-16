import os
from time import sleep
from telethon import events
from pyrogram import filters
from pyrogram.types import Message

from _pyrogram import app
from config import PREFIX
from _pyrogram.helpers.utils import get_message_type, Types
import asyncio


@app.on_message(filters.command("repo", PREFIX) & filters.me)
async def koc(_, m):
  if not m.text[0].isalpha() and m.text[0] not in ("/", "#", "@", "!"):
    await m.edit("╭✠╼━━━━━━❖━━━━━━━✠╮"
                 "\n` `[🌸 𝐑𝐄𝐏𝐎 𝐕𝐄𝐄𝐙 𝐔𝐒𝐄𝐑𝐁𝐎𝐓](https://github.com/levina-lab/veezuserbot)` `"
                 "\n╰✠╼━━━━━━❖━━━━━━━✠╯"
                 "\nthis repository is managed by veez project, copyrights and licenses have been applied to this repository.")
    await app.send_message(m.chat.id, disable_web_page_preview=True)
