from time import sleep
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord import FFmpegPCMAudio

client = commands.Bot(intents=discord.Intents.all() ,command_prefix = '-')
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

@client.event
async def on_ready():
    print('Bot have been successfully initialized.')
    print('_______________________________________')

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('not in voice channel')

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('not in voice channel')

@client.command(pass_context = True)
async def alarm(ctx):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('alarm.mp3')
    voice.play(source)
    sleep(7)
    await leave(ctx)
    


@client.command()
async def djstart(ctx, pomodoro=25, short_break=5, long_break=10, cycles=4):
    channel = client.get_channel(1024003232227393576)
    await channel.send(f'Pomodoro initialized with times')
    for c in range(cycles):
        await channel.send(f'Starting cycle {c+1}')
        sleep(pomodoro) # *60 after testing
        await alarm(ctx)
        await channel.send(f'End of study time')
        sleep(short_break)
        await alarm(ctx)
        await channel.send(f'End of short break.')
    await channel.send(f'Cycles have endend.')
    sleep(long_break)
    await alarm(ctx)
    await channel.send('End of long break.')
            





client.run(TOKEN)