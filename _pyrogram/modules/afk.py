import humanize
import asyncio
from _pyrogram import app, CMD_HELP
from pyrogram import filters
from pyrogram.types import Message
from config import PREFIX, LOG_CHAT
import time
from datetime import datetime
import _pyrogram.database.afkdb as _pyrogram
from _pyrogram.helpers.pyrohelper import get_arg
from _pyrogram.helpers.pyrohelper import user_afk
from _pyrogram.modules.alive import get_readable_time
from _pyrogram.helpers.utils import get_message_type, Types

AFK = False
AFK_REASON = ""

CMD_HELP.update(
    {
        "afk": """
**📕 MODULE AFK:**
`━━━━━━━━━━━━━`
`afk (alasan)` ⇛ Tandai dirimu sedang afk atau offline.
"""
    }
)

LOG_CHAT = LOG_CHAT

MENTIONED = []
AFK_RESTIRECT = {}
DELAY_TIME = 60


@app.on_message(filters.command("afk", PREFIX) & filters.me)
async def afk(client, message):
    afk_time = int(time.time())
    arg = get_arg(message)
    if not arg:
        reason = None
    else:
        reason = arg
    await _pyrogram.set_afk(True, afk_time, reason)
    await message.edit("**I'm goin' AFK**")


@app.on_message(
    ((filters.group & filters.mentioned) | filters.private) & ~filters.me & ~filters.service, group=3
)
async def collect_afk_messages(_, message: Message):
    if AFK:
        text = (
            f"`saya sedang afk.\n"
            f"\nsedang offline dan sibuk.\n"
            f"alasan: ```{AFK_REASON.upper()}```\n"
            f"\nsaya akan kembali online..`"
        )
        await message._client.send_message(
            chat_id=message.chat.id,
            text=text,
            reply_to_message_id=message.message_id,
        )


@app.on_message(filters.command("afk", PREFIX) & filters.me, group=3)
async def afk_set(_, message: Message):
    global AFK_REASON, AFK

    cmd = message.command
    afk_text = ""

    if len(cmd) > 1:
        afk_text = " ".join(cmd[1:])

    if isinstance(afk_text, str):
        AFK_REASON = afk_text

    AFK = True

    await message.delete()
