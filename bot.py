import discord
from discord.ext import commands
import json

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='*',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot is online")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(jdata['welcome_channel'])
    await channel.send(f'{member} join!')
   


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(jdata['welcome_channel'])
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    """ctx = context"""
    await ctx.send(f'{round(bot.latency*1000)} ms')

bot.run(jdata['TOKEN'])


