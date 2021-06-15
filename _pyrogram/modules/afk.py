from logging import disable
import time
from pyrogram import *

from _pyrogram import app
from config import PREFIX, CMD_HELP, LOG_CHAT
import _pyrogram.database.afkdb as afkme
from _pyrogram.helpers.pyrohelper import get_arg, user_afk

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
    afk_time = int(time.time())
    arg = get_arg(message)
    if not arg:
        await afkme.set_afk(True, afk_time)
    else:
        await afkme.set_afk(True, afk_time, arg)
    await message.edit("**I am going AFK**")


@app.on_message(filters.mentioned & ~filters.bot & filters.create(user_afk))
async def afk_mentioned(client, message):
    global MENTIONED
    afk_since, reason = afkme.get_afk_time()
    total_afk = int(afk_since) - int(time.time())
    if "-" in str(message.chat.id):
        cid = str(message.chat.id)[4:]
    else:
        cid = str(message.chat.id)
    await message.reply(
        f"**I am AFK Right Now**\n**Reason:** `{reason}`\n**AFK for:** `{total_afk}`"
    )
    await app.forward_message(
        chat_id=LOG_CHAT,
        from_chat_id=message.chat.id,
        message_id=message.id,
        disable_notification=True,
    )


@app.on_message(filters.outgoing & filters.me & filters.create(user_afk))
async def auto_unafk(client, message):
    await afkme.set_unafk()
    unafk_message = await app.send_message(message.chat.id, "**I am no longer AFK**")
    await app.send_message(
        LOG_CHAT,
        "You are no longer AFK!!. You have received the above messages when you were offline",
    )
    await asyncio.sleep(2)
    await unafk_message.delete()
