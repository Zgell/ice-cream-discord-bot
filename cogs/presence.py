from color.colors import Colors
from discord import Member
from discord.ext import commands
import Keys
from datetime import datetime

class Presence(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
    await bot.add_cog(Presence(bot))
