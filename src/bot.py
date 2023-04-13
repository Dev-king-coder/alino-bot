import os
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

from utils.bot_help import musicBotHelp, reminderBotHelp, chatBotHelp
from utils.music_feature import music_cog
from utils.reminder_feature import reminder_cog
from utils.chat_feature import chat_cog

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def setupBot():
    await bot.add_cog(musicBotHelp(bot))
    await bot.add_cog(music_cog(bot))
    print('Music bot setup complete')

    await bot.add_cog(reminderBotHelp(bot))
    await bot.add_cog(reminder_cog(bot))
    print('Reminder bot setup complete')

    await bot.add_cog(chatBotHelp(bot))
    await bot.add_cog(chat_cog(bot))
    print('Chat bot setup complete')
asyncio.run(setupBot())

   
bot.run(TOKEN)