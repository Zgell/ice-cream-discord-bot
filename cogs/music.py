import discord
from discord import app_commands
from discord.ext import commands
import Keys
from ytdl import YTDLSource

'''
NOTE: Make sure to install the correct libraries needed:
pip install discord.py[voice]
'''

YTDL_ENABLED = True

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # sets the client variable so we can use it in cogs

    '''
    Info on nested slash commands / command groups:
    https://gist.github.com/AbstractUmbra/a9c188797ae194e592efe05fa129c57f
    '''

    '''
    TODO: Add a "play" queue
    TODO: Add clean-up for files after usage
    TODO: Look into streaming the audio directly? See this: https://stackoverflow.com/questions/60745020/is-there-a-way-to-directly-stream-audio-from-a-youtube-video-using-youtube-dl-or
    TODO: Make "src" argument for /vc play optional so it can play a default noise
    '''

    vc_group = app_commands.Group(name="vc", description="All commands pertaining to Voice Channel functionality.")



    @vc_group.command(name="join", description="Tells the bot to join the voice channel the user is in.")
    async def join(self, interaction: discord.Interaction) -> None:
        '''
        BUG: For whatever reason if you are not in a VC, you don't get the "you are not connected" message.
        This might be due to a quirk with interaction.user.voice being different than ctx.message.author.voice?
        Either way this should be investigated further.
        '''
        if not interaction.user.voice:
            await interaction.response.send_message("You are not connected to a voice channel!", ephemeral=True)
            return
        else:
            channel = interaction.user.voice.channel
            await interaction.response.send_message("Joining voice channel...", ephemeral=True)
            await channel.connect()


    @vc_group.command(name='leave', description='Tells the bot to disconnect from the voice channel.')
    async def leave(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message('Leaving voice channel...', ephemeral=True)
        voice_client = interaction.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await interaction.response.send_message('The bot is not connected to a voice channel.', ephemeral=True)


    @vc_group.command(name='play', description='Plays an audio source.')
    @app_commands.describe(
        src='The source of audio to be played. Can be a URL from a supported website or a filename stored on the bot\'s server.'
    )
    async def play(self, interaction: discord.Interaction, src: str):
        '''
        Plays an audio source:
        src - Audio source. Can refer to an on-system file or a URL.
        '''
        try:
            server = interaction.guild
            voice_channel = server.voice_client

            '''
            BUG: For now, just assume that only YT URLs are passed. Can fix this later.
            '''
            # Slash commands don't have an analog for typing, so we'll adapt for now
            await interaction.response.send_message('Downloading audio source...', ephemeral=True)
            if YTDL_ENABLED and src is not None:
                filename = await YTDLSource.from_url(src, loop=self.bot.loop)
            else:
                filename = 'audio/test_audio.mp3'
            voice_channel.play(discord.FFmpegPCMAudio(executable="audio/ffmpeg.exe", source=filename))
            await interaction.response.send_message(f'**Now playing:** {filename}')
        except Exception as e:
            await interaction.response.send_message('The bot is not connected to a voice channel.', ephemeral=True)
            print(e)


    @vc_group.command(name='pause', description='Pauses the current audio source.')
    async def pause(self, interaction: discord.Interaction):
        voice_client = interaction.guild.voice_client
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await interaction.response.send_message('The bot is not playing any audio at the moment.', ephemeral=True)


    @vc_group.command(name='resume', description='Unpauses the current audio source.')
    async def resume(self, interaction: discord.Interaction):
        voice_client = interaction.guild.voice_client
        if voice_client.is_paused():
            await voice_client.resume()
        else:
            await interaction.response.send_message('The bot was not playing anything before. Use **/vc play <audio>** first.', ephemeral=True)


    @vc_group.command(name='stop', description='Stops the current audio source.')
    async def stop(self, interaction: discord.Interaction):
        '''
        BUG: This throws an error for some reason, even though it works?
        '''
        voice_client = interaction.guild.voice_client
        if voice_client.is_playing():
            await voice_client.stop()
            await interaction.response.send_message('The bot has stopped playing audio.', ephemeral=True)
        else:
            await interaction.response.send_message('The bot is not playing any audio at the moment.', ephemeral=True)


async def setup(bot):
    await bot.add_cog(Music(bot))
