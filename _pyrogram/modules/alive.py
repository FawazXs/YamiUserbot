# (C) 2021, Jayant Kageri

from config import PREFIX
import asyncio
import time
from datetime import datetime
from pyrogram import filters
from _pyrogram import app, StartTime, CMD_HELP
from sys import version_info

from pyrogram import __version__ as __pyro_version__
from pyrogram.types import Message

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(
    filters.command("alive -p")
    & filters.private
    & ~ filters.edited
)

CMD_HELP.update(
    {
        "Alive": """
**Alive**
  `alive -p` -> Untuk mengecek status alive pyrogram
  `alive -t` -> Untuk mengecek status alive telethon
  `ping -p` -> Untuk mem-ping pyrogram
  `ping -t` -> Untuk mem-ping telethon
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


@Client.on_message(filters.command("alive -p", PREFIX) & filters.me)
async def alive(_, m):
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    reply_msg = f"**[✨ VINA USERBOT ✨](https://github.com/levina-lab/vinauserbot)**\n\n"
    reply_msg = f"**[🌸 PEMBUAT 🌸](https://t.me/dlwrml)**\n\n"
    reply_msg += f"**VERSI PYTHON:** `{__python_version__}`\n"
    reply_msg += f"**VERSI PYROGRAM:** `{__pyro_version__}`\n"
    end_time = time.time()
    reply_msg += f"\nUPTIME: {uptime}",
    
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📣 CHANNEL", url="https://t.me/levinachannel")
                  ],[
                    InlineKeyboardButton(
                        "💬 GROUP", url="https://t.me/gcsupportbots"
                    ),
                    InlineKeyboardButton(
                        "🌸 OWNER", url="https://t.me/dlwrml"
                    )
                ]
            ]
        ),
    await m.delete()
    await app.send_message(m.chat.id, reply_msg, disable_web_page_preview=True)


@app.on_message(filters.command("ping -p", PREFIX) & filters.me)
async def pingme(_, message: Message):
    app_info = await app.get_me()
    start = datetime.now()
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"**[[PYROGRAM BOT]](https://docs.pyrogram.org)** \n**⚡️ kecepatan** **[DC-{app_info.dc_id}]**: `{m_s} ms`", disable_web_page_preview=True)
