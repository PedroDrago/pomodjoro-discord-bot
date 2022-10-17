from time import sleep
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
#from PyQt5.QtCore import QTimer

#criacao da instancia do bot
client = commands.Bot(intents=discord.Intents.all() ,command_prefix = '-')
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

#evento que printa mensagem informando que o bot foi inicializado
@client.event
async def on_ready():
    print('Bot have been successfully initialized.')
    print('_______________________________________')

#funcao que faz o bot entrar no canal de audio
@client.command(pass_context = True)
async def join(ctx):
    print('join function initialized')
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('not in voice channel')

#Funcao que faz o bot sair do canal de audio
@client.command(pass_context = True)
async def leave(ctx):
    print('leave function initialized')
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('not in voice channel')

#funcao que faz o bot entrar no canal de audio, tocar alarm.mp3 e apos isso sair do canal
@client.command(pass_context = True)
async def alarm(ctx):
    print('alarm() function initialized')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('alarm.mp3')
    voice.play(source)
    sleep(7)
    await leave(ctx)

#funcao que comeca o timer pomodoro.    
@client.command()
async def pomstart(ctx, pomodoro=25, short_break=5, long_break=10, cycles=4):
    print('pomstart() function initialized')
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

#roda o bot            
client.run(TOKEN)