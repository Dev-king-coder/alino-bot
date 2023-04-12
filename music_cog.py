import discord
from discord.ext import commands
import yt_dlp as youtube_dl

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.is_playing = False
        self.is_paused=False

        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = None

    def search_yt(self, search):
        with youtube_dl.YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                get_info = ydl.extract_info(f"ytsearch:{search}", download=False)['entries'][0]
            except Exception:
                return False
        return {'source': get_info['formats'][0]['url'], 'title': get_info['title']}

    async def play_music(self,ctx):
        if(len(self.music_queue)>0):
            self.is_playing=True
            url=self.music_queue[0][0]['source']
            if self.vc ==None or self.vc.is_connected() == False:
                self.vc = await self.music_queue[0][1].connect()

                if self.vc == None:
                    await ctx.send("Could not connect to voice channel")
                    return
                else:
                    await self.vc.move_to(self.music_queue[0][1])
                self.music_queue.pop(0)
                self.vc.play(discord.FFmpegPCMAudio(url,**self.FFMPEG_OPTIONS),after=lambda e: self.play_next(ctx))
                ctx.send(f"**Now Playing:** {url['title']}")

    def play_next(self, ctx):
        if len(self.music_queue) > 0:
            self.is_playing = True
            n = self.music_queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(n['source'], **self.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            ctx.send(f"**Now Playing:** {n['title']}")
        else:
            self.is_playing = False

    @commands.command(name='play',aliases=["p","playing"] ,help='Plays a song')
    async def play(self,ctx,*args):
        query = ' '.join(args)
        voice = ctx.author.voice
        if voice is None:
            await ctx.send("Join a voice channel first")
        else:
            voice_channel=voice.channel
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Could not download song")
            else:
                await ctx.send(f"Added {song['title']} to the queue")
                self.music_queue.append([song,voice_channel])

                if self.is_playing == False:
                    await self.play_music(ctx)

    @commands.command(name='pause',help='Pauses the current song')
    async def pause(self,ctx):
        if self.is_playing:
            self.is_paused = True
            self.is_playing = False
            self.vc.pause()
            await ctx.send("Paused")
        elif self.is_paused:
            await ctx.send("Already paused...resuming")
            self.vc.resume()
    
    @commands.command(name='resume',help='Resumes the current song')
    async def resume(self,ctx):
        if self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.vc.resume()
            await ctx.send("Resumed")
        elif self.is_playing:
            await ctx.send("Already playing")
            
    @commands.command(name='skip',help='Skips the current song')
    async def skip(self,ctx):
        if self.vc != None and self.vc:
            self.vc.stop()
            await self.play_music(ctx)
    
    @commands.command(name='clear',help='Clears the queue')
    async def clear(self,ctx):
        self.music_queue.clear()
        
        await ctx.send("Queue cleared")


    @commands.command(name='leave',help='Kicks the bot from the voice channel')
    async def leave(self,ctx):
        self.is_paused = False
        self.is_playing = False
        await self.vc.disconnect()

