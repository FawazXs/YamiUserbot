# (C) 2021, Levina Shavila
import os

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
        "alive": """
**📕 MODUL ALIVE:**
`━━━━━━━━━━━━`
`alive p` ⇛ Cek status alive pyrogram bot.
`alive t` ⇛ Cek status alive telethon bot.
`ping p` ⇛ Cek ping pyrogram bot.
`ping t` ⇛ Cek ping telethon bot.
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
async def alive(_, m):
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    reply_msg = f"**[۩▬▬ 𝐕𝐈𝐍𝐀 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 ▬▬۩](https://github.com/levina-lab/vinauserbot)**\n━━━━━━━━━━━━━━━━━━━━\n"
    reply_msg += f"**➠ versi python:** `{__python_version__}`\n"
    reply_msg += f"**➠ versi pyrogram:** `{__pyro_version__}`\n"
    reply_msg += f"**➠ versi userbot:** `0.1`\n"
    reply_msg += f"**➠ project name:** `veez project`\n"
    reply_msg += f"**➠ database:** `functioning`\n"
    reply_msg += f"**➠ commands:** `25 commands`\n"
    reply_msg += f"**➠ module:** `6 module`\n"
    reply_msg += f"**➠ branch:** `master`\n"
    reply_msg += f"**➠ owner:** `𝕃𝔼𝕍𝕀ℕ𝔸`\n━━━━━━━━━━━━━━━━━━━━"
    end_time = time.time()
    reply_msg += f"\n📶 bot uptime: {uptime}\n━━━━━━━━━━━━━━━━━━━━\n"
    reply_msg += f"**``[GROUP](https://t.me/gcsupportbots)` |` `[CHANNEL](https://t.me/levinachannel)` `| `[OWNER](https://t.me/dlwrml)``**\n"
    await m.delete()
    await app.send_message(m.chat.id, reply_msg, disable_web_page_preview=True)


@app.on_message(filters.command("ping p", PREFIX) & filters.me)
async def pingme(_, message: Message):
    app_info = await app.get_me()
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"**[𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠 𝗕𝗢𝗧](https://docs.pyrogram.org) • 𝐕𝐄𝐄𝐙 𝐏𝐑𝐎𝐉𝐄𝐂𝐓** \n\n**⚡️ kecepatan**: `{m_s} ms`\n**⚡️ uptime**: `{uptime}`\n**👩‍💻 owner**: `ʟᴇᴠɪɴᴀ`", disable_web_page_preview=True)
