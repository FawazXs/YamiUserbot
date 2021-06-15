<h1 align="center"><b>veez userbot</b></h1>
<p align="center">
<img src="https://telegra.ph/file/63ff170a7a8e4ed3fb278.jpg" width="256" height="256"/>
</p>

<p align="center">
<a href="#"><img title="Telegram-Userbot" src="https://img.shields.io/badge/Telegram%20Userbot-blue?colorA=%23ff0000&colorB=00BFFF&style=for-the-badge"></a>
</p>
<p align="center">
<img title="Followers" src="https://img.shields.io/github/followers/levina-lab?label=Followers&color=gold&style=flat-square">
<img title="Stars" src="https://img.shields.io/github/stars/levina-lab/vinauserbot?label=Stars&color=magenta&style=flat-square">
<img title="Forks" src="https://img.shields.io/github/forks/levina-lab/vinauserbot?label=Forks&color=brickred&style=flat-square">
<img title="Watching" src="https://img.shields.io/github/watchers/levina-lab/vinauserbot?label=Watchers&color=red&style=flat-square">
</p>
<h4 align="center">a telegram userbot based on pyrogram and telethon.</h4>

> Telegram userbot based on [Pyrogram](https://github.com/pyrogram/pyrogram) and [Telethon](https://github.com/LonamiWebs/Telethon)

Repositori ini berisi kode sumber Telegram Userbot dan instruksi untuk menjalankan dan menyalin repo ini. Selain tujuan utamanya, bot ini juga menampilkan [**Pyrogram Asyncio**](https:////github.com/pyrogram/pyrogram/issues/181) dan [**Smart Plugins**](https://docs.pyrogram.org/topics/smart-plugins) jangan ragu untuk menjelajahi kode sumber untuk pelajari lebih lanjut tentang topik ini.

Saya berasumsi anda akan membaca seluruh isi file README.md ini sebelum melanjutkan.

> Pengembangan Dan Pengoptimalisasian Repo Sedang Berlangsung.

# PENJELESAN
dibawah ini ada 2 opsi untuk mendeploy userbot, yakni melalui heroku maupun secara local, silahkan dipilih yang mana yang gampang. Repo ini juga masih rilis tahap awal, dan masih banyak yang harus di kembangkan, jika ingin berkontribusi di persilahkan, dan repo userbot ini membutuhkan 2 jenis string session yakni pyrogram dan telethon.

### Deploy Userbot & String Session
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/levina-lab/vinauserbot) [![STRING SESSION](https://replit.com/badge/github/levina-lab/vinauserbot)](https://replit.com/@levinalab/StringSession#main.py)

Tap the purple button above to deploy this userbot on heroku and tap the grey button to generate string session.

### Local Deploy
- Fill in config.py with your own values.
- Open Terminal
- Install Requirements `pip3 install -r requirements.txt`
- Running bot `python3 main.py`
- All Done :)

## 🛠 Configuration
- `API_ID` and `API_HASH` - Dapatkan dari https://my.telegram.org
- `TELETHON_SESSION` dan `PYROGRAM_SESSION`
- `HEROKU_APP_NAME` [ONLY FOR HEROKU] - Isi dengan app name yang kamu isi di kolom pertama.
- `HEROKU_API` [ONLY FOR HEROKU] - Dapatkan dari [sini](https://dashboard.heroku.com/account)
- `LOG_CHAT` - Buat grup, lalu masukkan [@VinaGroupBot](https://telegram.me/VinaGroupBot) lalu ketik `/id`

## 💬 Support Group
- Kalo ada masalah, Tanyakan di sini yah 👉 [@gcsupportbots](https://telegram.me/gcsupportbots)

# LEGAL
## 💖 Credits

- Thanks to [Levina](https://github.com/levina-lab) for creating this repository
- Thanks to [Satwik](https://github.com/okay-retard) for his [Zect Userbot](https://github.com/okay-retard/ZectUserbot)
- Thanks to [Dan Tès](https://github.com/delivrance) for his [Pyrogram](https://docs.pyrogram.org)
- Thanks to [Lonami](https://github.com/lonami/) for his [Telethon](https://docs.telethon.dev)
- Thanks to [Jayant Hegde Kageri](https://github.com/jayantkageri)
- Thanks to [Shrimadhv UK](https://github.com/SpEcHiDe)
- Thanks to [Aditya S](https://github.com/xditya)
- Thanks to [Swanit](https://github.com/swatv3nub)
- Thanks to [Sipak](https://github.com/ProgrammingError)

## 🎖 License
```
    Veez Userbot, A Telegram Lightweight Userbot for Developers
    Copyright (C) 2021 Levina Shavila

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
````
