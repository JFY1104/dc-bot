import discord
from discord.ext import commands
import json

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class event(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(jdata['welcome_channel'])
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(jdata['welcome_channel'])
        await channel.send(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        
        if msg.content in jdata['keyword'] and msg.author != self.bot.user:
            await msg.channel.send('嘟嘟可借你摸摸')


async def setup(bot):
    await bot.add_cog(event(bot))
