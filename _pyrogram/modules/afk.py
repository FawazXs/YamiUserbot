import humanize
from pyrogram import filters
from pyrogram.types import Message

AFK = False
AFK_REASON = ""

@app.on_message(
    ((filters.group & filters.mentioned) | filters.private) & ~filters.me & ~filters.service, group=3
)
async def collect_afk_messages(_, message: Message):
    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME)
        is_group = True if message.chat.type in ["supergroup", "group"] else False
        CHAT_TYPE = GROUPS if is_group else USERUSER
        text = (
            f"`Beep boop. This is an automated message.\n"
            f"I am not available right now.\n"
            f"Last seen: {last_seen}\n"
            f"Reason: ```{AFK_REASON.upper()}```\n"
            f"See you after I'm done doing whatever I'm doing.`"
        )
        await message._client.send_message(
            chat_id=GetChatID(message),
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
    AFK_TIME = datetime.now()

    await message.delete()
