# This file is Originally Written By @okay-retard on GitHub
# The Author (Jayant Kageri) just Ported this for Devloper Userbot
# (C) 2021 Jayant Kageri

from pyrogram import filters
from _pyrogram import app, HELP, CMD_HELP
from config import PREFIX
from _pyrogram.helpers.pyrohelper import get_arg

HELP.update(
    {
        "**📘 ADMIN TOOLS**": "ban, unban, promote, demote, kick, mute, unmute, pin, purge, del, invite",
        "**📘 ALIVE**": "alive, ping, (untuk ping & alive: p untuk pyrogram bot dan t untuk telethon bot)",
        "**📘 DEVELOPER**": "peval, teval, sh",
        "**📘 MISC**": "paste, tr, info, id",
        "**📘 HEROKU**": "update, restart, logs",
        "**📝 Ketik**"."help (nama module) untuk melihat penjelasan dari module tersebut.",
    }
)


@app.on_message(filters.command("help", PREFIX) & filters.me)
async def help(client, message):
    args = get_arg(message)
    if not args:
        text = "**📚 List module vina userbot:**\n\n"
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
