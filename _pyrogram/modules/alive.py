# (C) 2021, Levina Shavila
import os

from pyrogram.types.messages_and_media import message

from config import PREFIX
import asyncio
import time
from datetime import datetime
from pyrogram import filters
from _pyrogram import app, StartTime, CMD_HELP
from sys import version_info

from pyrogram import __version__ as __pyro_version__
from pyrogram.types import Message

CMD_HELP.update(
    {
        "mybot": """
**📕 MODULE MYBOT:**
`━━━━━━━━━━━━`
`alive p` ⇛ Cek status alive pyrogram bot.
`alive t` ⇛ Cek status alive telethon bot.
`ping p` ⇛ Cek ping pyrogram bot.
`ping t` ⇛ Cek ping telethon bot.
`repo` ⇛ give your repo information.
"""
    }
)

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@app.on_message(filters.command("alive p", PREFIX) & filters.me)
async def alive(_, message: Message):
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    reply_msg = f"**[۩▬ 𝐘𝐀𝐌𝐈 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝗜𝗦 𝗔𝗟𝗜𝗩𝗘 ▬۩](https://github.com/FawazXs/YamiUserbot)**\n━━━━━━━━━━━━━━━━━━━━━━\n"
    reply_msg += f"**🐍 Python** : `ver` `{__python_version__}`\n"
    reply_msg += f"**🖥 Pyrogram** : `ver` `{__pyro_version__}`\n"
    reply_msg += f"**🤖 Userbot** : `ver 0.2.0`\n"
    reply_msg += f"**🧪 Project** : `veez project`\n"
    reply_msg += f"**🗃 Database** : `functioning`\n"
    reply_msg += f"**🧩 Commands** : `50 commands`\n"
    reply_msg += f"**📚 Module** : `8 module`\n"
    reply_msg += f"**👩🏼‍💻 Owner** : `{message.from_user.first_name}`\n"
    reply_msg += f"**🔖 Branch** : `master`\n"
    reply_msg += (
        f"**🎖 License** : "
        "[GNU GPL V.3.0](https://github.com/levina-lab/vinauserbot/blob/master/LICENSE)"
        "\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    end_time = time.time()
    reply_msg += f"\n📶 **Uptime** : `{uptime}`\n━━━━━━━━━━━━━━━━━━━━━━\n"
    reply_msg += f"` `[GROUP](https://t.me/gcsupportbots)` `|` `[CHANNEL](https://t.me/levinachannel)` `|` `[OWNER](tg://user?id={message.from_user.id})` `\n"
    photo = "https://telegra.ph/file/b18a1a786e370ca903f6f.jpg"
    await message.delete()
    if message.reply_to_message:
        await app.send_photo(
            message.chat.id,
            photo,
            caption=reply_msg,
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await app.send_photo(message.chat.id, photo, caption=reply_msg)


@app.on_message(filters.command("ping p", PREFIX) & filters.me)
async def pingme(_, message: Message):
    app_info = await app.get_me()
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    if message.from_user.username:
        await message.edit(
            f"**[𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠 𝗕𝗢𝗧](https://docs.pyrogram.org) • 𝐏𝐈𝐍𝐆!!** \n┈───────────────┈\n**⚡️ kecepatan**: `{m_s} ms`\n**⚡️ uptime**: `{uptime}`\n**👩‍💻 owner**: `{(message.from_user.first_name).upper()}`\n**🦊 Username**: @{message.from_user.username}",
            disable_web_page_preview=True,
        )
    else:
        await message.edit(
            f"**[𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠 𝗕𝗢𝗧](https://docs.pyrogram.org) • 𝐏𝐈𝐍𝐆!!** \n┈───────────────┈\n**⚡️ kecepatan**: `{m_s} ms`\n**⚡️ uptime**: `{uptime}`\n**👩‍💻 owner**: `{(message.from_user.first_name).upper()}`\n**🦊 Username**: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
            disable_web_page_preview=True,
        )
