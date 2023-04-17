# a reminder bot for discord
from discord.ext import commands
import asyncio

class reminder_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='remind', help='Reminds you of something')
    async def remind(self, ctx, time, *, reminder):
        try:
            time = int(time)
        except ValueError:
            await ctx.send("Please enter command in valid Format:")
            await ctx.send("Example: !remind 10 'eat lunch'")
            return
        await ctx.send(f"Ok, I'll remind you in {time} minutes")
        await asyncio.sleep(time*60)
        await ctx.send(f"Hey {ctx.author.mention}, you asked me to remind you: {reminder}")

    @remind.error 
    async def on_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify When,What to remind!")
            await ctx.send("Example: !remind 10 eat lunch")
            await ctx.send("Type /help-rb for more info")
    
        
        
            
        