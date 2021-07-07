#! python3.7
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready ():
    print('bot is ready')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

client.run('ODQzOTMxNjI4MDExMzg4OTc4.YKLCkw.c8RKQd2tn-u-O-ZOKDTucrlmHJU')