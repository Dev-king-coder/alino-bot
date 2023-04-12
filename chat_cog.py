import discord
from discord.ext import commands


class chat_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='chat',aliases=["ai","chatgpt","gpt"] ,help='Chat with the bot')
    async def chat(self, ctx, *, message):
        bot_response = chatgpt_response(prompt=message)
        await ctx.send(f"Ok, I'll chat with you in {message} minutes")
        await ctx.send(f"Hey {ctx.author.mention}, you asked me to chat with you: {message}")