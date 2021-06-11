import config


@_pyrogram.on_cmd("repo", about={"header": "dapatkan informasi repo userbot"})
async def see_repo(message: Message):
  """lihat repo"""
  output = f"""
  __REPO USERBOT__ 🌸 **VEEZ** 🌸
  __repo userbot yang dibuat dengan simple__
  __veez userbot details__
  • **Version** : `ver` `0.1`
  • **License** : ""[GNU GPL V.3.0](https://github.com/levina-lab/vinauserbot/blob/master/LICENSE)""
  • **Repo** : ""[VEEZ USERBOT](https://github.com/levina-lab/vinauserbot)""
