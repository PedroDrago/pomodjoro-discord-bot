import discord
from discord.ext import commands

client = commands.bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot have been successfully initialized.')
    print('_______________________________________')