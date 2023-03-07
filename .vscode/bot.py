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


@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'LOAD cmds.{extension} DONE')


@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'RELOAD cmds.{extension} DONE')


@bot.command()
async def unload(ctx, extension):
    print(f'cmds.{extension}')
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'UNLOAD cmds.{extension} DONE')


async def load():
    for filename in os.listdir('C:\\Users\\home\\Documents\\GitHub\\bot\\.vscode\\cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')


async def main():
    await load()


asyncio.run(main())
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
