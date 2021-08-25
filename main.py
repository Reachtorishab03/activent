# Imports

import discord 
from discord.ext import commands
import os
import json 

# Token function
def get_token():
    with open("config.json", "r") as f:
        data = json.load(f)

        return data['token'] 


# Main variable initialisation
bot = commands.Bot(command_prefix='./', intents = discord.Intents.all())


# Events and loading cogs
@bot.event 
async def on_ready():
    print(f'{bot.user} is now ready!')
    for filename in os.listdir("./extensions"):
        if filename.endswith(".py"):
            try:
                bot.load_extension(f'extensions.{filename[:-3]}')
                print(f"Loaded {filename[:-3]}")
            except Exception as e:
                print(f'Not able to load {filename[:-3]} extensions \n{e.__name__} : {e}')



bot.run(get_token())