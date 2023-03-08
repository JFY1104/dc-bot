import discord
from discord.ext import commands
import datetime



class Main(commands.Cog):
        
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        """ctx = context"""
        await ctx.send(f'{round(self.bot.latency*1000)} ms')

    @commands.command()
    async def info(self,ctx):
        embed = discord.Embed(title="About ", url="https://genshin-impact.fandom.com/wiki/Klee ",
                              description="可莉", color=0xf51414,timestamp=datetime.datetime.now())
        embed.set_author(
            name="KLEE", icon_url="https://i.pinimg.com/736x/ed/33/fc/ed33fcf04c9e027781c770bdce6eb9a6.jpg")
        embed.set_thumbnail(
            url="https://www.pcgamesn.com/wp-content/sites/pcgamesn/2021/01/The-best-Genshin-Impact-Klee-build-550x309.jpg")
        embed.add_field(name="年紀", value="未知", inline=True)
        embed.add_field(name="職位", value="西風騎士團火花騎士", inline=True)
        embed.add_field(name="喜歡的東西", value="嘟嘟可", inline=False)
        embed.add_field(name="愛好", value="炸魚", inline=True)
        embed.add_field(name="討厭的東西", value="禁閉室", inline=True)
        await ctx.send(embed=embed)
 
    @commands.command()
    async def sayagain(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    """ 傳入參數 ,*,msg   """

    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)



async def setup(bot):
    await bot.add_cog(Main(bot))



