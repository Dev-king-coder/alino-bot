from discord.ext import commands
import open_ai

class chat_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='chat',aliases=["ai","gpt"] ,help='Chat with the bot')
    async def chat(self, ctx, *, message):
        bot_response =await open_ai.chatgpt_response(prompt=message)
        await ctx.send(f"Answer: {bot_response}")
    @chat.error
    async def on_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify a message to chat with the bot!")
            await ctx.send("Example: /chat Hello")
            await ctx.send("Type /help-cb for more info")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("Sorry, I am not able to chat with you right now. Please try again later.")

