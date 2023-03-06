import discord
from discord.ext import commands
import json
import random
import os
import asyncio
import cmd

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


async def load():
    for filename in os.listdir('C:\\Users\\home\\Documents\\GitHub\\bot\\.vscode\\cmds'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cmds.{filename[:-3]}')
                print(filename)

    

async def main():
    await load()

    
asyncio.run(main())
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
