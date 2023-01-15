import discord
from discord import app_commands
from discord.ext import commands
import Keys

'''
NOTE: Make sure to install the correct libraries needed:
pip install discord.py[voice]
'''

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # sets the client variable so we can use it in cogs

    @commands.command(name='join', help='Tells the bot to join the voice channel you are in.')
    async def join(self, ctx):
        await ctx.send('Joining voice channel...')
        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel!")
            return
        else:
            channel = ctx.message.author.voice.channel
            await channel.connect()

    @commands.command(name='leave', help='Tells the bot to disconnect from the voice channel.')
    async def leave(self, ctx):
        await ctx.send('Leaving voice channel...')
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

    @commands.command(name='play', help='Plays an audio source.')
    async def play(self, ctx):
        '''
        NOTE: For now, just use a dummy audio file. Later you can integrate music streaming
        '''
        try:
            server = ctx.message.guild
            voice_channel = server.voice_client

            async with ctx.typing():
                filename = 'audio/test_audio.mp3'  # NOTE: Change this later!
                voice_channel.play(discord.FFmpegPCMAudio(executable="audio/ffmpeg.exe", source=filename))
            await ctx.send(f'**Now playing:** {filename}')
        except Exception as e:
            await ctx.send("The bot is not connected to a voice channel.")
            print(e)

async def setup(bot):
    await bot.add_cog(Music(bot))
