import humanize
from _pyrogram import app, CMD_HELP
from pyrogram import filters
from pyrogram.types import Message
from config import PREFIX
import time
from datetime import datetime

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


@app.on_message(
    ((filters.group & filters.mentioned) | filters.private) & ~filters.me & ~filters.service, group=3
)
async def collect_afk_messages(_, message: Message):
    if AFK:
        text = (
            f"`haii, ini adalah pesan otomatis.\n"
            f"saat ini saya sedang offline, hubungi lagi nanti.\n"
            f"alasan: ```{AFK_REASON.upper()}```\n"
            f"saya akan kembali online setelah selesai menyelesaikan urusan ku ☺.`"
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
