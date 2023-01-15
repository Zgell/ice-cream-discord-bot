'''
A test module for slash commands.
Includes a way to resync slash commands with the Discord API (takes time).
'''
import discord
from discord import app_commands
from discord.ext import commands
import Keys

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # sets the client variable so we can use it in cogs

    @commands.command(name='slash-sync')
    async def slash_sync(self, ctx):
        if ctx.author.id == Keys.ZGELL_ID:
            try:
                synced = await self.bot.tree.sync()
                print(f"Synced {len(synced)} commands with Discord API!")
            except Exception as e:
                print(f"Error syncing commands: {e}")

    @app_commands.command(name='slash', description='A test command for slash commands. Does absolutely nothing.')
    async def slash(self, interaction: discord.Interaction):
        # an example command with cogs
        # await ctx.send('Yeeoooo!')
        await interaction.response.send_message("Yeeoooo!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Slash(bot))