from time import sleep
from telethon import events
from pyrogram import filters
from pyrogram.types import Message

from telethon.events import register
from _pyrogram import app
from config import PREFIX
from _pyrogram.helpers.utils import get_message_type, Types
import asyncio


@app.on_message(filters.command("repo", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("╭✠╼━━━━━━❖━━━━━━━✠╮"
                 "\n` `[𝐕𝐄𝐄𝐙 𝐔𝐒𝐄𝐑𝐁𝐎𝐓](https://github.com/levina-lab/vinauserbot)` `"
                 "\n╰✠╼━━━━━━❖━━━━━━━✠╯")
