import aiohttp
import random
from typing import Union

class Rosie:
    def __init__(self):
        self.url = "https://siesta.red/api/"

    async def text(self, text: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}txt/{text}") as url:
                image = await url.json()
                return image.get("response")
              
    async def image(self, image: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}png/{image}") as url:
                image = await url.json()
                return image.get("response")
              
    async def gif(self, gif: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}gif/{gif}") as url:
                image = await url.json()
                return image.get("response")           
