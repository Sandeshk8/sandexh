import discord 
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
status = cycle(['status1', 'status2'])

@client.event 
async def on_ready():
    print('bot is ready')

@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))

    
client.run('ODQzOTMxNjI4MDExMzg4OTc4.YKLCkw.c8RKQd2tn-u-O-ZOKDTucrlmHJU')