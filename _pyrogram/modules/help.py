# This file is Originally Written By @okay-retard on GitHub
# The Author (Jayant Kageri) just Ported this for Devloper Userbot
# (C) 2021 Jayant Kageri

from pyrogram import filters
from _pyrogram import app, HELP, CMD_HELP
from config import PREFIX
from _pyrogram.helpers.pyrohelper import get_arg

HELP.update(
    {
        "**📚 𝗠𝗢𝗗𝗨𝗟𝗘 𝟭**": "𝙖𝙙𝙢𝙞𝙣: ban, unban, promote, demote, kick, mute, unmute, pin, purge, del, invite",
        "**📚 𝗠𝗢𝗗𝗨𝗟𝗘 𝟮**": "𝙢𝙮𝙗𝙤𝙩: alive, ping, repo",
        "**📚 𝗠𝗢𝗗𝗨𝗟𝗘 𝟯**": "𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧: peval, teval, sh",
        "**📚 𝗠𝗢𝗗𝗨𝗟𝗘 𝟰**": "𝙢𝙞𝙨𝙘: paste, tr, info, id",
        "**📚 𝗠𝗢𝗗𝗨𝗟𝗘 𝟱**": "𝙝𝙚𝙧𝙤𝙠𝙪: update, restart, logs",
        "**📚 𝗠𝗢𝗗𝗨𝗟𝗘 𝟲**": "𝙖𝙛𝙠 (pembaruan untuk modul ini segera hadir)",
        "**📚 𝗠𝗢𝗗𝗨𝗟𝗘 𝟳**": "𝙖𝙣𝙞𝙢𝙖𝙩𝙞𝙤𝙣𝟭, 𝙖𝙣𝙞𝙢𝙖𝙩𝙞𝙤𝙣𝟮",
        "**📝 𝗡𝗢𝗧𝗘**": "ketik .help (nama module) untuk melihat penjelasan dari module tersebut.",
    }
)


@app.on_message(filters.command("bot", PREFIX) & filters.me)
async def help(client, message):
    args = get_arg(message)
    if not args:
        text = "**━━━━━━ 𝗠𝗢𝗗𝗨𝗟𝗘 𝗟𝗜𝗦𝗧 ━━━━━━━━**\n\n"
        for key, value in HELP.items():
            text += f"{key}: {value}\n\n"
        await message.edit(text)
        return
    else:
        module_help = CMD_HELP.get(args, False)
        if not module_help:
            await message.edit("`nama module yang anda berikan salah!`")
            return
        else:
            await message.edit(module_help)
