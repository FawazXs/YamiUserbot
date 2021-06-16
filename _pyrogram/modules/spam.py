# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 01:43:36 2021

@author: Kgf123
"""
from pyrogram import filters
from pyrogram.errors import FloodWait
from _pyrogram import app, CMD_HELP
from config import PREFIX
import asyncio

CMD_HELP.update(
    {
        "utils": """
**📕 MODULE UTILS:**
`━━━━━━━━━━━━`
'spam <count> <text>' ⇛ Spam the number of messages
"""
    }
)


@app.on_message(filters.command("spam", PREFIX) & filters.me)
async def spam(Client, message):
    x = message.text
    y = x.split(" ")
    spam_count = int(y[1])
    spam_text = y[2:]
    try:
        while spam_count > 0:
            await app.send_message(message.chat.id, spam_text)
            spam_count -= 1
    except FloodWait as e:
        await asyncio.sleep(e.x)
