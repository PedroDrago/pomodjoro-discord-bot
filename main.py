from time import sleep
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

@client.command()
async def djstart(ctx, pomodoro=25, short_break=5, long_break=10, cycles=4):
    channel = client.get_channel(1024003232227393576)
    channel.send('Pomodoro initialized with times bla bla bla')
    while True:
        for c in range(cycles):
            channel.send(f'Starting cycle {c+1}')
            sleep(pomodoro) # *60 after testing
            channel.send(f'End of study time')
            sleep(short_break)
            channel.send(f'End of short break.')
        channel.send(f'Cycles have endend.')
        sleep(long_break)
        channel.send('End of long break.')
            


client.run(TOKEN)