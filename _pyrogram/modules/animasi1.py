from time import sleep
from telethon import events
from pyrogram import filters
from pyrogram.types import Message

from telethon.events import register
from _pyrogram import app, CMD_HELP
from config import PREFIX
from _pyrogram.helpers.utils import get_message_type, Types
import asyncio


CMD_HELP.update(
    {
        "animation1": """
**📕 MODULE ANIMATION 1:**
`━━━━━━━━━━━━━━━━━━`
`usage` ⇛ ketik .droopy
`usage` ⇛ ketik .kevincan
`usage` ⇛ ketik .pantau
`usage` ⇛ ketik .piki
`usage` ⇛ ketik .hati
`usage` ⇛ ketik .ok
`usage` ⇛ ketik .nyanyi
`usage` ⇛ ketik .ular
`usage` ⇛ ketik .bundir
`usage` ⇛ ketik .pig
"""
    }
)


@app.on_message(filters.command("hati", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("`\n(\\_/)`"
                 "`\n(●_●)`"
                 "`\n />❤️ *Ini Buat Kamu`")
    sleep(3)
    await e.edit("`\n(\\_/)`"
                 "`\n(●_●)`"
                 "`\n/>💔  *Aku Ambil Lagi`")
    sleep(2)
    await e.edit("`\n(\\_/)`"
                 "`\n(●_●)`"
                 "`\n💔<\\  *Terimakasih`")



@app.on_message(filters.command("piki", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("`Piki itu Ganteng😁..`")
    sleep(1)
    await e.edit("`Piki juga manis..`")
    sleep(1)
    await e.edit("`Baik hati 🥺`")
    sleep(1)
    await e.edit("`penyayang Pulak 🥰`")
    sleep(1)
    await e.edit("`Dan Buat Lo Semua...`")
    sleep(1)
    await e.edit("`NGENTOTTT!!!!!!`")
    
    
# created by levina, under this cloning from geez userbot


@app.on_message(filters.command("pantau", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("`\n┻┳|―-∩`"
                 "`\n┳┻|     ヽ`"
                 "`\n┻┳|    ● |`"
                 "`\n┳┻|▼) _ノ`"
                 "`\n┻┳|￣  )`"
                 "`\n┳ﾐ(￣ ／`"
                 "`\n┻┳T￣|`"
                 "\n**masih gw pantau anj.**")
    
    
@app.on_message(filters.command("ok", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
                 "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                 "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                 "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
                 "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
                 "██████▄▄█‡‡‡‡‡‡████████▄\n"
                 "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                 "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                 "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                 "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                 "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                 "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
                 "█████‡‡‡‡‡‡‡██████████\n")
    
    
@app.on_message(filters.command("nyanyi", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("**Cakep Doang Gak Bernyanyi (ง˙o˙)ว**")
    sleep(2)
    await e.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await e.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await e.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await e.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await e.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await e.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await e.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await e.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await e.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await e.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await e.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await e.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await e.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await e.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await e.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    
    
@app.on_message(filters.command("ular", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("░░░░▓\n"
                 "░░░▓▓\n"
                 "░░█▓▓█\n"
                 "░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░░░██▓▓██\n"
                 "░░░░██▓▓██\n"
                 "░░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░██▓▓██\n"
                 "░░░██▓▓███\n"
                 "░░░░██▓▓████\n"
                 "░░░░░██▓▓█████\n"
                 "░░░░░░██▓▓██████\n"
                 "░░░░░░███▓▓███████\n"
                 "░░░░░████▓▓████████\n"
                 "░░░░█████▓▓█████████\n"
                 "░░░█████░░░█████●███\n"
                 "░░████░░░░░░░███████\n"
                 "░░███░░░░░░░░░██████\n"
                 "░░██░░░░░░░░░░░████\n"
                 "░░░░░░░░░░░░░░░░███\n"
                 "░░░░░░░░░░░░░░░░░░░\n")
    
    
@app.on_message(filters.command("bundir", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("`Dadah Semuanya...`          \n　　　　　|"
                 "\n　　　　　| \n"
                 "　　　　　| \n"
                 "　　　　　| \n"
                 "　　　　　| \n"
                 "　　　　　| \n"
                 "　　　　　| \n"
                 "　　　　　| \n"
                 "　／￣￣＼| \n"
                 "＜ ´･ 　　 |＼ \n"
                 "　|　３　 | 丶＼ \n"
                 "＜ 、･　　|　　＼ \n"
                 "　＼＿＿／∪ _ ∪) \n"
                 "　　　　　 Ｕ Ｕ\n")
    
    
@app.on_message(filters.command("pig", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("┈┈┏━╮╭━┓┈╭━━━━╮\n"
                 "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
                 "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
                 "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
                 "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
                 "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
                 "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
                 "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")
