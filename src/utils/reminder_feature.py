# a reminder bot for discord
from discord.ext import commands
import asyncio

class reminder_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='remind', help='Reminds you of something')
    async def remind(self, ctx, time, *, reminder):
        await ctx.send(f"Ok, I'll remind you in {time} minutes")
        await asyncio.sleep(int(time)*60)
        await ctx.send(f"Hey {ctx.author.mention}, you asked me to remind you: {reminder}")
    
        
        
            
        