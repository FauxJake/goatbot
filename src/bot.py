import os
import json

from utilities.important_commands import get_compliment, get_insult

from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
token = os.getenv("DISCORD_TOKEN").strip("{").strip("}").strip("\"")
bot = commands.Bot(command_prefix="!")

@bot.command(
    help = 'Gets an insult. Optionally @mention a username to throw some shade.',
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
    help='Gets a compliment. Optionally @mention a username to throw some love.',
    brief='Gets a nice compliment'
)
async def compliment(ctx):
    compliment = await get_compliment()
    if ctx.message.mentions and len(ctx.message.mentions) > 0:
        mentionIds = (m.mention for m in ctx.message.mentions)
        compliment = (f"{', '.join([str(x) for x in mentionIds])} {compliment}\n" 
                      f"Sincerely, {ctx.message.author}")
                      
    await ctx.channel.send(compliment)

### General User Commands
async def stats(ctx, username):
    '''Reports stats for username'''
    pass

async def top(ctx, num):
    '''Reports top x players (default 10)'''
    pass

async def h2h(ctx, num):
    '''Reports the head-to-head (H2H) record between two supplied 
       usernames'''
    pass

async def db(ctx, dbusername):
    '''sets duelingbook.com username'''
    pass

async def save(ctx, link):
    '''save a deck by supplying an imgur link''' # TODO what?
    pass

async def decks(ctx, username):
    '''show username's decks (default self)'''
    pass

### Tournament User Commands
async def show(ctx):
    '''show the current tournament''' # TODO define what show means
    pass

async def join(ctx, decklist):
    '''join / register for the current tourney'''
    pass

async def resubmit(ctx, decklist):
    '''change decklist for currently joined tournament'''
    pass

async def loss(ctx, username):
    '''reports a loss to the username specified'''
    pass

async def undo(ctx):
    '''undos the last loss you reported'''
    pass  

async def drop(ctx):
    '''drop from the current tournament'''
    pass

### General Mod Commands
async def role(ctx):
    '''add or remove the ranked goats role (discord role?)'''
    pass

async def rename(ctx, username, newname):
    '''set nickname for player''' # TODO can't you just right-click?
    pass

async def census(ctx):
    '''add missing players and update names in the db'''
    # TODO player list from where?
    pass

async def recalc(ctx):
    '''Recalculate all player stats if needed'''
    # TODO define if needed
    # TODO stats == elo? How recalc and not reset?
    pass

### Tournament Mod Commands
async def create(ctx):
    '''create a new tournament'''
    pass

async def signup(ctx, username):
    '''register provided username for current tournament'''
    pass

async def edit(ctx, username, decklist):
    '''reclassify a player's decklist''' # TODO what?
    pass

async def manual(ctx, username_win, username_lose):
    '''manually records match result between two usernames'''
    pass

async def sudoundo(ctx, username):
    '''undo the most recent loss for username (default last loss 
       reported)'''
    pass

async def noshow(ctx, username):
    '''report a noshow for a match''' # TODO how is elo affected?
    pass

async def remove(ctx, username):
    '''removes provided username from the current tournament'''
    pass

async def seed(ctx):
    '''assigns seeds to tournament participants based on 
       elo / rankings'''   # TODO get granular requirements
    pass

async def start(ctx):
    '''start the tournament'''
    pass

async def end(ctx):
    '''end the current tournament'''
    pass

bot.run(token)