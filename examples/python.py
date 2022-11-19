# imports
import asyncio
from rosieapi import Rosie

# API
loop = asyncio.get_event_loop()
print(loop.run_until_complete(api.get("gif", "cuddle")))
print(loop.run_until_complete(api.gif("cuddle")))
