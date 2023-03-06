import discord
from discord.ext import commands


class cog_extension(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
