import os
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

from help_cog import help_cog
from music_cog import music_cog

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())

async def setup(bot):
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))
asyncio.run(setup(bot))

bot.run(TOKEN)