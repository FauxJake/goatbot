import requests
import discord

class GoatBotClient(discord.Client):
    async def on_message(self, message):
        if message.content.startswith('!insult'):
            '''returns a cheeky insult'''
            await message.channel.send(await self.GetInsult())
        elif message.content.startswith('!loss'):
            '''Reports loss to supplied username'''
            pass
        elif message.content.startswith('!stats'):  
            '''Reports stats for username'''
            pass
        elif message.content.startswith('!top'):
            '''Reports top x players (default 10)'''
            pass
        elif message.content.startswith('!h2h'):    
            '''Reports the head-to-head (H2H) record between two supplied 
            usernames'''
            pass
        elif message.content.startswith('!role'):
            '''add or remove the ranked goats role (discord role?)'''
            pass
        elif message.content.startswith('!undo'):
            '''undos the last loss you reported'''
            pass
        elif message.content.startswith('!join'):
            '''join / register for the current tourney'''
            pass
        elif message.content.startswith('!resubmit'):
            '''change decklist for currently joined tournament'''
            pass
        elif message.content.startswith('!drop'):
            '''drop from the current tournament'''
            pass
        elif message.content.startswith('!show'):
            '''show the current tournament''' # TODO define what show means
            pass
        elif message.content.startswith('!db'):
            '''set your duelingbook.com username'''
            pass
        elif message.content.startswith('!save'):
            '''save a deck by supplying an imgur link''' # TODO what?
            pass
        elif message.content.startswith('!decks'):
            '''show username's decks (default self)'''
            pass
        elif message.content.startswith('!bot'): # TODO starting point I think
            '''pm user guide'''
            pass

        # MOD COMMANDS
        elif message.content.startswith('!mod'):
            '''pm the mod command guide'''
            pass
        elif message.content.startswith('!manual'):
            '''record match result between two supplied usernames'''
            pass
        elif message.content.startswith('!undo'):   
            '''undo the most recent loss for username (default last loss 
            reported)'''
            pass

        # TOURNAMENT MANAGEMENT COMMANDS TODO Integrate Challonge.com API
        elif message.content.startswith('!create'):
            '''create a new tournament'''
            pass
        elif message.content.startswith('!signup'):
            '''register provided username for current tournament'''
            pass
        elif message.content.startswith('!edit'):
            '''reclassify a player's decklist''' # TODO what?
            pass
        elif message.content.startswith('!noshow'):
            '''report a noshow for a match''' # TODO how is elo affected?
            pass
        elif message.content.startswith('!remove'):
            '''removes provided username from the current tournament'''
            pass
        elif message.content.startswith('!seed'):
            '''assigns seeds to tournament participants based on 
            elo / rankings'''   # TODO get granular requirements
            pass
        elif message.content.startswith('!start'):
            '''start the tournament'''
            pass
        elif message.content.startswith('!end'):
            '''end the current tournament'''
            pass

        # MOD SERVER COMMANDS
        elif message.content.startswith('!rename'):
            '''set nickname for player''' # TODO can't you just right-click?
            pass
        elif message.content.startswith('!census'): 
            '''add missing players and update names in the db'''
            # TODO player list from where?
            pass
        elif message.content.startswith('!recalc'):
            '''Recalculate all player stats if needed'''
            # TODO define if needed
            # TODO stats == elo? How recalc and not reset?
            pass

    async def GetInsult(self):
        '''retrieves an insult from evilinsult.com's API'''
        r = requests.get('https://evilinsult.com/generate_insult.php?lang=en')
        return r.text