import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('mgnrega ma majdoori'))
    print('bot is ready')
    
client = discord.Client(activity=discord.Game(name='with your feelings'))


client.run('ODQzOTMxNjI4MDExMzg4OTc4.YKLCkw.c8RKQd2tn-u-O-ZOKDTucrlmHJU')