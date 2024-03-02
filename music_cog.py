import discord
from discord.ext import commands
from yt_dlp import YoutubeDL
from youtubesearchpython import VideosSearch
import nacl
import asyncio


class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_playing = False
        self.is_paused = False
        self.current_song = {}
        self.music_queue = []
        self.vc = None

        self.YTDL_OPTIONS = {
            'format': 'bestaudio/best',
            'nonplaylist': 'True',
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        self.FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }

        self.ytdl = YoutubeDL(self.YTDL_OPTIONS)


    def search_yt(self, item):
        if item.startswith("https://"):
            title = self.ytdl.extract_info(item, download=False)["title"]
            return{'source':item, 'title':title}
        search = VideosSearch(item, limit=1)
        return{'source':search.result()["result"][0]["link"], 'title':search.result()["result"][0]["title"]}


    @commands.command(name="play", aliases=["p"], help="Plays a song from youtube")
    async def play(self, ctx, *args):
        query = " ".join(args)
        try:
            voice_channel = ctx.author.voice.channel
        except:
            await ctx.send("```You need to connect to a voice channel first!```")
            return
        if self.is_paused:
            self.vc.resume()
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("```Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.```")
            else:
                if self.is_playing:
                    await ctx.send(f"**#{len(self.music_queue)+2} -'{song['title']}'** added to the queue")  
                else:
                    await ctx.send(f"**'{song['title']}'** added to the queue")  
                self.music_queue.append([song, voice_channel])
                if self.is_playing == False:
                    await self.play_music(ctx)


    async def play_music(self, ctx):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            #try to connect to voice channel if you are not already connected
            if self.vc == None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()

                #in case we fail to connect
                if self.vc == None:
                    await ctx.send("```Could not connect to the voice channel```")
                    return
            else:
                await self.vc.move_to(self.music_queue[0][1])
            #remove the first element as you are currently playing it
            self.current_song = self.music_queue.pop(0)
            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: self.ytdl.extract_info(m_url, download=False))
            song = data['url']
            self.vc.play(discord.FFmpegPCMAudio(song, executable= "ffmpeg.exe", **self.FFMPEG_OPTIONS), after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(), self.bot.loop))

        else:
            self.is_playing = False
            self.current_song = {}

    
    async def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            #get the first url
            m_url = self.music_queue[0][0]['source']

            #remove the first element as you are currently playing it
            self.current_song = self.music_queue.pop(0)
            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: self.ytdl.extract_info(m_url, download=False))
            song = data['url']
            self.vc.play(discord.FFmpegPCMAudio(song, executable= "ffmpeg.exe", **self.FFMPEG_OPTIONS), after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(), self.bot.loop))
        else:
            self.is_playing = False
            self.current_song = {}


    @commands.command(name="clean", aliases=["c"])
    async def clean(self, ctx):
        if ctx.author.voice.channel == self.vc.channel:
            await self.pause(ctx, clean=True)
            self.is_playing = False 
            self.is_paused = False
            self.music_queue = []
            self.current_song = {}
        

    @commands.command(name="leave", aliases=["l"])
    async def leave(self, ctx):
        if ctx.author.voice.channel == self.vc.channel:
            self.is_playing = False
            self.is_paused = False
            self.music_queue = []
            await self.vc.disconnect()
            self.vc = None

    
    @commands.command(name="join", aliases=["j"])
    async def join(self, ctx):
        if ctx.author.voice.channel:
            print(self.vc)
            self.vc = await ctx.author.voice.channel.connect()
            print(self.vc)

    
    @commands.command(name="queue", aliases=["q"])
    async def queue(self, ctx):
        if ctx.author.voice.channel == self.vc.channel:
            if not self.current_song:
                message = "No more songs queued.\n"

            else:
                message = "Songs queued:\n\n\\> " + f"{self.current_song[0]['title']}\n" 

                for song_info in self.music_queue:
                    message += "   " + str( song_info[0]['title'] ) + "\n"

            await ctx.send(message)


    @commands.command(name="pause", aliases=["stop", "s"])
    async def pause(self, ctx, clean=False):
        if ctx.author.voice.channel == self.vc.channel:
            if self.is_playing:
                if not clean:
                    await ctx.send("Song paused!")

                else:
                    await ctx.send("Playlist cleaned!")

                self.is_playing = False
                self.is_paused = True
                self.vc.pause()

    
    @commands.command(name="resume", aliases=["r"])
    async def resume(self, ctx):
        if ctx.author.voice.channel == self.vc.channel:
            if self.is_paused:
                await ctx.send("Song resumed!")
                self.is_playing = True
                self.is_paused = False
                self.vc.resume()
