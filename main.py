import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

client = commands.Bot(intents=discord.Intents.all() ,command_prefix = '!')
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

@client.event
async def on_ready():
    print('Bot have been successfully initialized.')
    print('_______________________________________')

client.run(TOKEN)