import asyncio
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


load_dotenv()
spotify = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'), client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'))
    )
class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='play', help='Plays a song from Spotify')
    async def play(self, ctx, *, song):
        results=spotify.search(q=song, type='track', limit=1)
        if not results['tracks']['items']:
            await ctx.send(f"Sorry, I couldn't find the song \"{song}\".")
            return

        track = results['tracks']['items'][0]
        if not track['preview_url']:
            await ctx.send(f"Sorry, I couldn't find a preview of the song \"{song}\".")
            return
        preview_url = track['preview_url']

        if ctx.author.voice is None:
            await ctx.send("You need to be in a voice channel to use this command.")
            return

        if not ctx.voice_client:
            voice_client = ctx.author.voice.channel
            await voice_client.connect()

        # Play song
        print(preview_url)
        source = discord.FFmpegPCMAudio(preview_url)
        voice_client = ctx.voice_client
        voice_client.play(source)

        # Disconnect from voice channel after song is done playing
        while voice_client.is_playing():
            await asyncio.sleep(1)
        await voice_client.disconnect()
