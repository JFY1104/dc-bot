import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='*',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot is online")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1078228435857588304)
    await channel.send(f'{member} join!')
   


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1078228435857588304)
    await channel.send(f'{member} leave!')


bot.run('MTA3ODIzNzU4MjE0OTgyNDU5NA.GHTn_J.4vOvwbL11sQvF6HpUKkIjS1Qj9U5nTOrGWciwA')


