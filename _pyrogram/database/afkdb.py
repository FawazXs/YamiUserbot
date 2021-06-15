from . import _client

col1 = _client["veezuserbot"]["afk"]


async def set_afk(
    afk_status, afk_since, afk_reason="My master is busy. Will respond later."
):
    doc = {
        "afk_id": 1,
        "afk_status": afk_status,
        "afk_since": afk_since,
        "afk_reason": afk_reason,
    }
    if await col1.find_one({"afk_id": 1}):
        await col1.update_one(
            {"afk_id": 1},
            {
                "$set": {
                    "afk_status": afk_status,
                    "afk_since": afk_since,
                    "afk_reason": afk_reason,
                }
            },
        )
    else:
        await col1.insert_one(doc)


async def set_unafk():
    await col1.update_one(
        {"afk_id": 1},
        {"$set": {"afk_status": False, "afk_since": None, "afk_reason": None}},
    )


async def get_afk_status():
    g_afk = await col1.find_one({"afk_id": 1})
    f = g_afk["afk_status"]
    if f == True:
        return True
    else:
        return False


async def get_afk_time():
    ak = await col1.find_one({"afk_id": 1})
    return ak["afk_since"], ak["afk_reason"]
