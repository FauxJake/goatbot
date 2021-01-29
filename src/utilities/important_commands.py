import requests
import json

async def get_insult():
        '''retrieves an insult from evilinsult.com's API'''
        r = requests.get('https://evilinsult.com/generate_insult.php?lang=en')
        return r.text

async def get_compliment():
        '''retrieves a proper compliment from https://complimentr.com/api'''
        r = requests.get('https://complimentr.com/api')
        return r.json()["compliment"]