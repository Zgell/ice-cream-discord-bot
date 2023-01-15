from discord.ext import commands
import Keys

class Late(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if (Keys.CRY_TWITCH_URL in msg.content) and (msg.author.id == Keys.CRYENOGENIC_ID or msg.author.id == Keys.ZGELL_ID):
            await msg.reply('late')

async def setup(bot):
    await bot.add_cog(Late(bot))
