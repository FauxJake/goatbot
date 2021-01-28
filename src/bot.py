import os
import json

from utilities.important_commands import get_compliment, get_insult

from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
token = os.getenv("DISCORD_TOKEN").strip("{").strip("}").strip("\"")
bot = commands.Bot(command_prefix="!")

@bot.command(
    help = '',
    brief = 'Gets that perfect insult.'
)
async def insult(ctx):
    insult = await get_insult()
    if ctx.message.mentions and len(ctx.message.mentions) > 0:
        mentionIds = (m.mention for m in ctx.message.mentions)
        insult = (f"{', '.join([str(x) for x in mentionIds])} {insult}\n" 
                  f"Sincerely, {ctx.message.author}")

    await ctx.channel.send(insult)

@bot.command(
    help='',
    brief=''
)
async def compliment(ctx):
    compliment = await get_compliment()
    if ctx.message.mentions and len(ctx.message.mentions) > 0:
        mentionIds = (m.mention for m in ctx.message.mentions)
        compliment = (f"{', '.join([str(x) for x in mentionIds])} {compliment}\n" 
                      f"Sincerely, {ctx.message.author}")
                      
    await ctx.channel.send(compliment)

bot.run(token)