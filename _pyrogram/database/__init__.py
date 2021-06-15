import motor.motor_asyncio
from config import MONGO_URI

_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
