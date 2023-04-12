import os
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

from help_cog import musicBotHelp, reminderBotHelp
from music_cog import music_cog
from reminder_cog import reminder_cog

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())

@bot.event
async def setupMusicBot():
    await bot.add_cog(musicBotHelp(bot))
    await bot.add_cog(music_cog(bot))
    print('Music bot setup complete')
asyncio.run(setupMusicBot())

@bot.event
async def setupReminderBot():
    await bot.add_cog(reminderBotHelp(bot))
    await bot.add_cog(reminder_cog(bot))
    print('Reminder bot setup complete')
asyncio.run(setupReminderBot())
   
bot.run(TOKEN)