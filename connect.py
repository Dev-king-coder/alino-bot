import os;
import random;
import discord
from dotenv import load_dotenv;
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())


bot.run(TOKEN)