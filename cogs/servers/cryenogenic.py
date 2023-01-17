import discord
from discord import app_commands
from discord.ext import commands
import Keys

'''
TODO: Restrict command access to be used only in Cry's server!
'''

class CryenogenicServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands unique to the Cryenogenic Discord Server'
        self.public_module = False  # To signify that these commands should only be shown in /help when in Cry's server

    cryo_group = app_commands.Group(name="cryo", description="All commands unique to the Cryenogenic discord.")

    async def cog_app_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError) -> None:
        '''
        Called any time a slash command receives an error. Logs the error in 
        the terminal and lets the user know that an error occurred.
        '''
        # Log the error for developer's sake
        print('An error occurred in the following command:', interaction.command)
        print('ERROR:', str(error))
        # Also let the user know something went wrong
        await interaction.response.send_message()

    @commands.Cog.listener()
    async def on_message(self, msg):
        """If Cry posts his Twitch URL, automatically reply with "late" """
        if (Keys.CRY_TWITCH_URL in msg.content) and (msg.author.id == Keys.CRYENOGENIC_ID or msg.author.id == Keys.ZGELL_ID):
            await msg.reply('late')

    # Code commented out below for now as it is a little too chaotic for even Cry's discord
    """
    @commands.Cog.listener()
    async def on_presence_update(self, before: Member, after: Member):
        '''
        If a server member starts playing League of Legends, DM them to
        make them reconsider their life choices.
        '''
        activity_list = [activity.name for activity in after.activities]
        print(f"{after}: {activity_list}")
        if 'League of Legends' in activity_list:
            print('!!!!!!!!!! LEAGUE OF LEGENDS DETECTED !!!!!!!!!!\n')
            channel = await after.create_dm()
            await channel.send('mmMMm... where ya mom at')
    """

async def setup(bot):
    await bot.add_cog(CryenogenicServer(bot))
