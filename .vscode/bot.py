import discord
from discord.ext import commands
import json
import random

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='*', intents=discord.Intents.all())


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


@bot.command()
async def 圖片(ctx):
    randompic = random.choice(jdata['picpath'])
    pic = discord.File(randompic)
    await ctx.send(file=pic)
""" send中要用file = pic 表示pic為檔案 
    discord.File 而不是file  
    路徑要用 \\ 分隔          
"""


@bot.command()
async def 線上圖片(ctx):
    pic = jdata['picurl']
    await ctx.send(pic)
""" 發送網路上圖片時 只需要將網址當作文字發送即可 """


bot.run(jdata['TOKEN'])
