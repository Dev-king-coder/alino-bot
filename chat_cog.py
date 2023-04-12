from discord.ext import commands
import chatgpt_ai.open_ai as open_ai

class chat_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='chat',aliases=["ai","chatgpt","gpt"] ,help='Chat with the bot')
    async def chat(self, ctx, *, message):
        bot_response = open_ai.chatgpt_response(prompt=message)
        await ctx.send(f"Answer: {bot_response}")
