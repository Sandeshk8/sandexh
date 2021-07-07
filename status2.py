import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)
    await fetch_user(user_id)


bot.run('ODQzOTMxNjI4MDExMzg4OTc4.YKLCkw.c8RKQd2tn-u-O-ZOKDTucrlmHJU')