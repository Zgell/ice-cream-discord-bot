from discord.ext import commands
import Keys

'''
NOTE: This module has been (temporarily) deprecated!
I intend to use this module in the future for random fun commands, but for
now it will be disconnected, but will remain in the codebase.
'''

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # sets the client variable so we can use it in cogs
        self.description = 'A set of fun commands!'

    @commands.Cog.listener()
    async def on_message(self, msg):
        """If Cry posts his Twitch URL, automatically reply with "late" """
        if (Keys.CRY_TWITCH_URL in msg.content) and (msg.author.id == Keys.CRYENOGENIC_ID or msg.author.id == Keys.ZGELL_ID):
            await msg.reply('late')

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
    await bot.add_cog(Fun(bot))
