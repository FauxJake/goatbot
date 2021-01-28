# bot.py
import os
import discord
import json
from dotenv import load_dotenv
from goat_client import GoatBotClient

load_dotenv()
client = GoatBotClient()
token = os.getenv("DISCORD_TOKEN").strip("{").strip("}").strip("\"")
client.run(token)