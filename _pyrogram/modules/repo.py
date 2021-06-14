from time import sleep
from telethon import events
from pyrogram import filters
from pyrogram.types import Message

from _pyrogram import app
from config import PREFIX
from _pyrogram.helpers.utils import get_message_type, Types
import asyncio


@app.on_message(filters.command("repo", PREFIX) & filters.me)
async def koc(_, e, m):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("╭✠╼━━━━━━❖━━━━━━━✠╮"
    reply_msg = f"\n` `[🌸 𝐑𝐄𝐏𝐎 𝐕𝐄𝐄𝐙 𝐔𝐒𝐄𝐑𝐁𝐎𝐓](https://github.com/levina-lab/vinauserbot)` `"
    reply_msg = f"\n╰✠╼━━━━━━❖━━━━━━━✠╯"
    reply_msg = f"\n🎖` `[GNU GPL V.3.0](https://github.com/levina-lab/vinauserbot/blob/master/LICENSE)` `")
    await m.edit()
    await app.send_message(m.chat.id, disable_web_page_preview=True)
