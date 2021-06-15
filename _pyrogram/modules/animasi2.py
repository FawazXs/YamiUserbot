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
        "animation2": """
**📕 MODULE ANIMATION 2:**
`━━━━━━━━━━━━━━━━━━`
`usage` ⇛ ketik .darling
`usage` ⇛ ketik .zombi
`usage` ⇛ ketik .djokes
`usage` ⇛ ketik .nih
`usage` ⇛ ketik .hiks
`usage` ⇛ ketik .hujat
`usage` ⇛ ketik .heli
`usage` ⇛ ketik .shoot
`usage` ⇛ ketik .tank
`usage` ⇛ ketik .dog
"""
    }
)


@app.on_message(filters.command("darling", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("I LOVE YOU BEB 💕")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💗💕")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG KAMU 💝💖💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SELAMANYA 💕")
    await e.edit("💘💘💘💘")
    await e.edit("CINTA")
    await e.edit("KAMU")
    await e.edit("SELAMANYA")
    await e.edit("KAMU")
    await e.edit("PUJAAN HATIKU")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY DARLING 🥰")
    await e.edit("💕💞💘💝")
    await e.edit("💘💕💞💝")
    await e.edit("SAYANG KAMU 💞")
    
    
@app.on_message(filters.command("zombi", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("`ZO.. ZOMBIEEE...`")
    sleep(1)
    await e.edit("`LARII ADA ZOMBIEEE...`")
    sleep(1)
    await e.edit("`🏃                        🧟‍♀️`")
    await e.edit("`🏃                       🧟‍♀️`")
    await e.edit("`🏃                      🧟‍♀️`")
    await e.edit("`🏃                     🧟‍♀️`")
    await e.edit("`🏃   `LARII`          🧟‍♀️`")
    await e.edit("`🏃                   🧟‍♀️`")
    await e.edit("`🏃                  🧟‍♀️`")
    await e.edit("`🏃                 🧟‍♀️`")
    await e.edit("`🏃                🧟‍♀️`")
    await e.edit("`🏃               🧟‍♀️`")
    await e.edit("`🏃              🧟‍♀️`")
    await e.edit("`🏃             🧟‍♀️`")
    await e.edit("`🏃            🧟‍♀️`")
    await e.edit("`🏃           🧟‍♀️`")
    await e.edit("`🏃 TIDAK!!  🧟‍♀️`")
    await e.edit("`🏃           🧟‍♀️`")
    await e.edit("`🏃            🧟‍♀️`")
    await e.edit("`🏃             🧟‍♀️`")
    await e.edit("`🏃              🧟‍♀️`")
    await e.edit("`🏃               🧟‍♀️`")
    await e.edit("`🏃                🧟‍♀️`")
    await e.edit("`🏃                 🧟‍♀️`")
    await e.edit("`🏃                  🧟‍♀️`")
    await e.edit("`🏃                   🧟‍♀️`")
    await e.edit("`🏃                    🧟‍♀️`")
    await e.edit("`🏃                     🧟‍♀️`")
    await e.edit("`🏃  Huft Capek        🧟‍♀️`")
    await e.edit("`🏃                   🧟‍♀️`")
    await e.edit("`🏃                  🧟‍♀️`")
    await e.edit("`🏃                 🧟‍♀️`")
    await e.edit("`🏃                🧟‍♀️`")
    await e.edit("`🏃               🧟‍♀️`")
    await e.edit("`🏃              🧟‍♀️`")
    await e.edit("`🏃             🧟‍♀️`")
    await e.edit("`🏃            🧟‍♀️`")
    await e.edit("`🏃           🧟‍♀️`")
    await e.edit("`🏃          🧟‍♀️`")
    await e.edit("`🏃         🧟‍♀️`")
    await e.edit("`DIA SEMAKIN MENDEKAT!!!`")
    sleep(1)
    await e.edit("`🏃       🧟‍♀️`")
    await e.edit("`🏃      🧟‍♀️`")
    await e.edit("`🏃     🧟‍♀️`")
    await e.edit("`🏃    🧟‍♀️`")
    await e.edit("`Habislah Aku...`")
    sleep(1)
    await e.edit("🧟‍♂️")
    sleep(3)
    await e.edit("`ARRGGHHHHH`")
    await e.edit("😱")
    sleep(3)
    await e.edit("`DEATH ☠️`")
    
    
@app.on_message(filters.command("djokes", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("`dark jokes kuy..`")
    sleep(1)
    await e.edit("`kuylah gass...`")
    sleep(1)
    await e.edit("`😈 YOK MULAIII`")
    sleep(1)
    await e.edit("`orang buntung ngak akan pernah masuk surga..`")
    sleep(2)
    await e.edit("`karna apa?..`")
    sleep(2)
    await e.edit("`karena wudhunya tidak pernah sah..`")
    sleep(2)
    await e.edit("`okok, lagi lagi...`")
    sleep(1)
    await e.edit("`bagaimana cara orang buntung makan?..`")
    sleep(2)
    await e.edit("`apakah cara makannya sama seperti ayam?..`")
    sleep(2)
    await e.edit("`okok ini yg terakhir..`")
    sleep(1)
    await e.edit("`kegiatan pramuka disinyalir diskriminatif..`")
    sleep(2)
    await e.edit("`tau kenapa?...`")
    sleep(2)
    await e.edit("`karena yang tangannya buntung tidak bisa tepuk pramuka..`")
    sleep(2)
    await e.edit("`sekian, terimakasih..`")
    
    
@app.on_message(filters.command("nih", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("`\n(\\_/)`"
                 "`\n(●_●)`"
                 "`\n />💖 *Nih Buat Kamu`")
    sleep(2)
    await e.edit("`\n(\\_/)`"
                 "`\n(●_●)`"
                 "`\n💖<\\  *Tapi Bo'ong HiyaHiyaHiya`")
    
    
@app.on_message(filters.command("hiks", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("أ‿أ")
    await e.edit("╥﹏╥")
    await e.edit("(;﹏;)")
    await e.edit("(ToT)")
    await e.edit("(┳Д┳)")
    await e.edit("(ಥ﹏ಥ)")
    await e.edit("（；へ：）")
    await e.edit("(T＿T)")
    await e.edit("（πーπ）")
    await e.edit("(Ｔ▽Ｔ)")
    await e.edit("(⋟﹏⋞)")
    await e.edit("（ｉДｉ）")
    await e.edit("(´Д⊂ヽ")
    await e.edit("(;Д;)")
    await e.edit("（>﹏<）")
    await e.edit("(TдT)")
    await e.edit("(つ﹏⊂)")
    await e.edit("༼☯﹏☯༽")
    await e.edit("(ノ﹏ヽ)")
    await e.edit("(ノAヽ)")
    await e.edit("(╥_╥)")
    await e.edit("(T⌓T)")
    await e.edit("(༎ຶ⌑༎ຶ)")
    await e.edit("(☍﹏⁰)｡")
    await e.edit("(ಥ_ʖಥ)")
    await e.edit("(つд⊂)")
    await e.edit("(≖͞_≖̥)")
    await e.edit("(இ﹏இ`｡)")
    await e.edit("༼ಢ_ಢ༽")
    await e.edit("༼ ༎ຶ ෴ ༎ຶ༽")
    
    
@app.on_message(filters.command("hujat", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("`Hai Beban Keluarga, Apa Kabar 😜`")
    sleep(1)
    await e.edit("`Jangan Bilang Lu Gak Dianggep Sama Ortu Lu 🤣`")
    sleep(1)
    await e.edit("`Mau Tau Karena Apa ?`")
    sleep(1)
    await e.edit("`Karena Lo Wibu, Sampah, Pemuja Plastik xixixi 🙊🙊`")
    sleep(1)
    await e.edit("`Dahlah Gak Usah Berharap Banyak, Elu Itu Udah Gak Berguna 😜`")
    sleep(1)
    await e.edit("`MANA MUNGKIN ORTU LU PEDULII xixixi 🙈`")
    sleep(1)
    await e.edit("`KETAWA DULU BOLEH KALI YAA 😁`")
    sleep(1)
    await e.edit("`HAHAHAHAHAHAHA`")
    sleep(1)
    await e.edit("`KASIAN ORTUNYAA GAPEDULIII 🙈🤣`")
    sleep(1)
    await e.edit("`MAAF YA, CANDAA BEBANNNN xixixi 🙈`")
    sleep(1)
    await e.edit("`Tapi Bo'ong Hiyahiyahiya`")
    sleep(1)
    await e.edit("`Skip, Baperan...`")
    sleep(1)
    await e.edit("`BYE.`")
    
    
@app.on_message(filters.command("heli", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("▬▬▬.◙.▬▬▬ \n"
                 "═▂▄▄▓▄▄▂ \n"
                 "◢◤ █▀▀████▄▄▄▄◢◤ \n"
                 "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
                 "◥█████◤ \n"
                 "══╩══╩══ \n"
                 "╬═╬ \n"
                 "╬═╬ \n"
                 "╬═╬ \n"
                 "╬═╬ \n"
                 "╬═╬ \n"
                 "╬═╬ \n"
                 "╬═╬ Hallo Epribadeh :) \n"
                 "╬═╬☻/ \n"
                 "╬═╬/▌ \n"
                 "╬═╬/ \\ \n")
    
    
@app.on_message(filters.command("shoot", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("_/﹋\\_\n"
                 "(҂`_´)\n"
                 "<,︻╦╤─ ҉\n"
                 "_/﹋\_"
                 "\n**Gw Tembak Juga Lu Anj!!**")
    
    
@app.on_message(filters.command("tank", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
                 "▂▄▅█████████▅▄▃▂…\n"
                 "[███████████████████]\n"
                 "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n")
    
    
@app.on_message(filters.command("dog", PREFIX) & filters.me)
async def koc(_, e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    await e.edit("╥━━━━━━━━╭━━╮━━┳\n"
                 "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
                 "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
                 "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
                 "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
                 "╨━━┗┛┗┛━━┗┛┗┛━━┻\n")
