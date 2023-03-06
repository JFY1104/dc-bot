import discord
from discord.ext import commands
from core.classes import cog_extension


def setup(bot):
    bot.add_cog(Main(bot))
    
class Main(cog_extension):
        
        @commands.command()
        async def ping(self,ctx):
         """ctx = context"""
         await ctx.send(f'{round(self.bot.latency*1000)} ms')




