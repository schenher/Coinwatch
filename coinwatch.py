import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
import requests
import json
from pricewatch import pricewatch
#load info from .env
load_dotenv()
#get discord token
TOKEN = os.getenv('DISCORD_TOKEN')
#allows for commands in the future
bot = commands.Bot(command_prefix="!", description="Coinwatcher")

@bot.event
async def on_ready():
	print('Logged in as {0.user}'.format(bot))
	print(discord.__version__)
	watcher = pricewatch()
	await watcher.watch(bot)

bot.run(TOKEN)

