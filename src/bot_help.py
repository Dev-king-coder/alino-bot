from discord.ext import commands

class musicBotHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message="""
        ```*Music Bot Help*\n
/play <song name> - Plays a song from youtube\n
/pause - Pauses the current song\n
/resume - Resumes the current song\n
/leave - Leaves the voice channel\n
/skip - Skips the current song\n
/clear - Clears the current queue```
        """

    @commands.Cog.listener()
    async def on_ready(self):
        return
    @commands.command(name='help-mb', help='Displays help on music bot')    
    async def help(self, ctx):
        print('Music bot help command ready')
        if ctx.channel.name == 'music-bot':
            await ctx.send(self.help_message)
        else:
            await ctx.send('Go to music-bot channel and type /help-mb for HELP!')


class reminderBotHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message="""
        ```*Reminder Bot Help*\n
/remind <time-in-minutes> <message> - Reminds you of something after a certain time\n
/help-rb - Displays help on reminder bot for HELP!/n```
        """

    @commands.Cog.listener()
    async def on_ready(self):
        return
    @commands.command(name='help-rb', help='Displays help on reminder bot for HELP!')
    async def help(self, ctx):
        print('Reminder bot help is ready')
        if ctx.channel.name == 'reminder-bot':
            await ctx.send(self.help_message)
        else:
            await ctx.send('Go to reminder-bot channel and type /help-rb')

class chatBotHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message="""
        ```
        *Chat Bot Help*\n
/chat <message> - Chat with the bot\n
/help-cb - Displays help on chat bot for HELP!\n ```
        """

    @commands.Cog.listener()
    async def on_ready(self):
        return

    @commands.command(name='help-cb',help='Chat with the bot')
    async def help(self, ctx):
        print('Chat bot help is ready')
        if ctx.channel.name == 'chat-bot':
            await ctx.send(self.help_message)
        else:
            await ctx.send('Go to chat-bot channel and type /help-cb')

