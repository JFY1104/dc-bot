import discord
from discord.ext import commands




class Main(commands.Cog):
        
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        """ctx = context"""
        await ctx.send(f'{round(self.bot.latency*1000)} ms')

 

async def setup(bot):
    await bot.add_cog(Main(bot))



