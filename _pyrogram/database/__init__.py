# This file originally writen by @levina-lab on github
# Copyright (c) 2021 by veez project
# Released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/levina-lab/vinauserbot/blob/master/LICENSE >
#
# All rights reserved.


import motor.motor_asyncio
from config import MONGO_URI


cli = motor.motor_asyncio.AsyncioMotorClient(MONGO_URI)
