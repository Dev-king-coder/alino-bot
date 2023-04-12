import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message="""
        ```
        **Commands:**
        /play <song name> - Plays a song
        /pause - Pauses the current song
        /resume - Resumes the current song
        /skip - Skips the current song
        /leave - Kicks the bot from the voice channel
        ```
        """
        self.text_channel=[]
        