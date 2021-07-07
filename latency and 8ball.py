#! python3.7
import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *,question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",]
    await ctx.send(f'Question = {question}\n Answer: {random.choice(responses)}')     
        
 
client.run('ODQzOTMxNjI4MDExMzg4OTc4.YKLCkw.c8RKQd2tn-u-O-ZOKDTucrlmHJU')