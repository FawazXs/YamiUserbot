from logging import disable
import time
from pyrogram import *

from _pyrogram import app, CMD_HELP
from config import PREFIX, LOG_CHAT
import _pyrogram.database.afkdb as afkme
from _pyrogram.helpers.pyrohelper import get_arg, get_readable_time, user_afk

CMD_HELP.update(
    {
        "afk": """
**📕 MODULE AFK:**
`━━━━━━━━━━━━`
`afk or afk <reason>` ⇛ Go afk (away from keyboard).
"""
    }
)

LOG_CHAT = LOG_CHAT


@app.on_message(filters.command("afk", PREFIX) & filters.me)
async def afk(Client, message):
    afk_time = time.time()
    arg = get_arg(message)
    if not arg:
        await afkme.set_afk(True, afk_time)
    else:
        await afkme.set_afk(True, afk_time, arg)
    x = await message.edit("**I am going AFK**")
    await asyncio.sleep(3)
    await x.delete()


@app.on_message(
    filters.mentioned & ~filters.bot & filters.create(user_afk) & ~filters.me
)
async def afk_mentioned(client, message):
    afk_since, reason = await afkme.get_afk_time()
    afk_e = get_readable_time(time.time() - afk_since)

    await message.reply(
        f"**I am AFK Right Now**\n**Reason:** `{reason}`\n**AFK for:** `{afk_e}`"
    )
    await message.forward_message(
        chat_id=LOG_CHAT,
        from_chat_id=message.chat.id,
        message_id=message.id,
        disable_notification=True,
    )


@app.on_message(filters.outgoing & filters.me & filters.create(user_afk))
async def auto_unafk(client, message):

    unafk_message = await app.send_message(message.chat.id, "**I am no longer AFK**")
    afk_since, reason = await afkme.get_afk_time()
    afk_e = get_readable_time(time.time() - afk_since)
    await app.send_message(
        LOG_CHAT,
        f"__You are no longer AFK!!.__\n**You have received the above messages when you were offline**\n**Total Time AFK:** `{afk_e}`",
    )
    await asyncio.sleep(3)
    await unafk_message.delete()
    await afkme.set_unafk()
