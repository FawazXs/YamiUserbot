from time import sleep
from telethon import events
from pyrogram import filters
from pyrogram.types import Message

from telethon.events import register
from _pyrogram import app
from config import PREFIX
from _pyrogram.helpers.utils import get_message_type, Types
import asyncio


# created by levina (c) 2021 by veez project


@app.on_message(filters.command("kevincan", PREFIX) & filters.me)
async def koc(_, e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("perkenalkan.")
        sleep(1)
        await e.edit("perkenalkan..")
        sleep(1)
        await e.edit("perkenalkan...")
        sleep(1)
        await e.edit("😎")
        sleep(3)
        await e.edit("namaku kevin")
        sleep(1)
        await e.edit("kevin forever")
        sleep(1)
        await e.edit("kevin handsome")
        sleep(1)
        await e.edit("orang nya baik hati..")
        sleep(1)
        await e.edit("tampan..")
        sleep(1)
        await e.edit("pemberani")
        sleep(1)
        await e.edit("seperti...")
        sleep(1)
        await e.edit("🗿")
        sleep(4)
        await e.edit("yap benar, seperti dia..")
        sleep(1)
        await e.edit("tampan bukan ?...")
        sleep(1)
        await e.edit("selain tampan..")
        sleep(1)
        await e.edit("dan pemberani..")
        sleep(1)
        await e.edit("aku juga cerdas..")
        sleep(1)
        await e.edit("siapa?..")
        sleep(1)
        await e.edit("ya aku dong..")
        sleep(1)
        await e.edit("iya aku..")
        sleep(1)
        await e.edit("kevin cool..")
        sleep(1)
        await e.edit("satu..")
        sleep(1)
        await e.edit("kata...")
        sleep(1)
        await e.edit("buat....")
        sleep(1)
        await e.edit("lu semua.....")
        sleep(1)
        await e.edit("ASUUUU...")
        sleep(1)
        await e.edit("dahlah....")
        sleep(1)
        await e.edit("bye sj...")
        sleep(1)
        await e.edit("ku gabut...")
        sleep(1)
        await e.edit("gabut sekali....")
        sleep(1)
        await e.edit("👻")
        sleep(4)
        await e.edit("misi..")
        sleep(1)
        await e.edit("foya...")
        sleep(1)
        await e.edit("misi..")
        sleep(1)
        await e.edit("foya...")
        sleep(1)
        await e.edit("don't play play bosquahh 🥵")
        sleep(1)
        await e.edit("🤑")
        sleep(4)
        await e.edit("sekian...")
        sleep(1)
        await e.edit("terimakasih....")
        sleep(1)
        await e.edit("TAMAT 😜")
