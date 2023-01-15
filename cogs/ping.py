from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # sets the client variable so we can use it in cogs

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     # an example event with cogs
    #     print('Cog "Test" loaded!')

    @commands.command(name='ping')
    async def ping(self, ctx):
        # an example command with cogs
        await ctx.send('Pong!')

async def setup(bot):
    await bot.add_cog(Ping(bot))
