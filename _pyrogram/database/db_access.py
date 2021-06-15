from _pyrogram.database.database_handlers import DB
import config

mongodb = DB(config.MONGO_URI, "veezuserbot")

