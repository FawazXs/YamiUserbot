# This file is Originally Written By @okay-retard on GitHub
# The Author (Jayant Kageri) just Ported this for Devloper Userbot
# (C) 2021 Jayant Kageri

from pyrogram import filters
from _pyrogram import app, HELP, CMD_HELP
from config import PREFIX
from _pyrogram.helpers.pyrohelper import get_arg

HELP.update(
    {
        "**📚 module 1**": "admin tools: ban, unban, promote, demote, kick, mute, unmute, pin, purge, del, invite",
        "**📚 module 2**": "alive, ping, (p untuk pyrogram bot dan t untuk telethon bot)",
        "**📚 module 3**": "developer: peval, teval, sh",
        "**📚 module 4**": "misc: paste, tr, info, id",
        "**📚 module 5**": "heroku: update, restart, logs",
        "**📝 notes**": "ketik .help (nama module) untuk melihat penjelasan dari module tersebut.",
    }
)


@app.on_message(filters.command("help", PREFIX) & filters.me)
async def help(client, message):
    args = get_arg(message)
    if not args:
        text = "**━━━━━━ MODULE LIST ━━━━━━━━**\n\n"
        for key, value in HELP.items():
            text += f"{key}: {value}\n\n"
        await message.edit(text)
        return
    else:
        module_help = CMD_HELP.get(args, False)
        if not module_help:
            await message.edit("nama module yang anda berikan salah!")
            return
        else:
            await message.edit(module_help)
