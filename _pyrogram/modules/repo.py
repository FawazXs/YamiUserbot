from time import sleep
from telethon import events
from pyrogram import filters
from pyrogram.types import Message

from _pyrogram import app
from config import PREFIX
from _pyrogram.helpers.utils import get_message_type, Types
import asyncio


@app.on_message(filters.command("repo", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("╭✠╼━━━━━━❖━━━━━━━✠╮"
                 "\n` `[🌸 𝐑𝐄𝐏𝐎 𝐕𝐄𝐄𝐙 𝐔𝐒𝐄𝐑𝐁𝐎𝐓](https://github.com/levina-lab/vinauserbot)` `"
                 "\n╰✠╼━━━━━━❖━━━━━━━✠╯"
                 "\n🎖` `[GNU GPL V.3.0](https://github.com/levina-lab/vinauserbot/blob/master/LICENSE)` `")
    await app.send_message(chat.id, disable_web_page_preview=True)