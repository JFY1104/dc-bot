import discord
from discord.ext import commands
import random
import json

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)



class react(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def 圖片(self,ctx):
        randompic = random.choice(jdata['picpath'])
        pic = discord.File(randompic)
        await ctx.send(file=pic)
    """ send中要用file = pic 表示pic為檔案 
        discord.File 而不是file  
        路徑要用 \\ 分隔          
    """

    @commands.command()
    async def 線上圖片(self,ctx):
        pic = jdata['picurl']
        await ctx.send(pic)


""" 發送網路上圖片時 只需要將網址當作文字發送即可 """


async def setup(bot):
    await bot.add_cog(react(bot))


