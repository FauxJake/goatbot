# bot.py
import os
import discord
import json
import requests
from dotenv import load_dotenv

load_dotenv()
class GoatBotClient(discord.Client):
    async def on_message(self, message):
        if message.content.startswith('$insult'):
            await message.channel.send(await self.GetInsult())

    async def GetInsult(self):
        r = requests.get('https://evilinsult.com/generate_insult.php?lang=en')
        return r.text

client = GoatBotClient()
token = os.getenv("DISCORD_TOKEN").strip("{").strip("}").strip("\"")
client.run(token)