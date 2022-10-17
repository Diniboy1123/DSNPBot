import asyncio

import aiohttp

class DisneyPlus():
    def __init__(self, bot):
        self.session = None
        self.bot = bot
        self._regions = []
    
    async def init_session(self, bot):
        self.session = aiohttp.ClientSession(headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"})

        async with self.session.get("https://cdn.registerdisney.go.com/jgc/v8/client/DTCI-DISNEYPLUS.GC.WEB-PROD/configuration/site") as req:
            try:
                self._regions = (await req.json()).get("data", {}).get("compliance", {}).get("countries", [])
            except Exception as e:
                self.bot.logging.error(f"Failed to get regions {e}")

    @property
    def regions(self):
        return self._regions

