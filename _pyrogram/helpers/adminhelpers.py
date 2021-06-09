from time import sleep, time

from pyrogram.types import Message

from _pyrogram import app


async def CheckAdmin(message: Message):
    """pastikan jika anda adalah admin."""
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await app.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__saya bukan admin!__")
        sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin or SELF.can_restrict_members:
            return True
        else:
            await message.edit("__tidak punya izin untuk membatasi anggota__")
            sleep(2)
            await message.delete()
