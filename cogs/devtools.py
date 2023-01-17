import discord
from discord import app_commands
from discord.ext import commands
import Keys

class Devtools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = 'A set of commands reserved for bot developers only.'
        self.public_module = True  # Lets commands show up in any server

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

    @commands.command(name='slash-sync', 
                    description='A dev-only command used to synchronize commands with the Discord API.')
    async def slash_sync(self, ctx: commands.Context) -> None:
        # TODO: Replace this later with proper database integration!
        # TODO: Remove this command once the slash command version, "sync", is online!
        if ctx.author.id == Keys.ZGELL_ID:
            try:
                synced = await self.bot.tree.sync()
                print(f"Synced {len(synced)} commands with Discord API!")
            except Exception as e:
                print(f"Error syncing commands: {e}")

    @app_commands.command(name='sync', 
                        description='Used to synchronize the bot\'s commands with the Discord API.')
    async def slash_sync_slash(self, interaction: discord.Interaction) -> None:
        # TODO: Replace this later with proper database integration!
        if interaction.user.id == Keys.ZGELL_ID:
            try:
                synced = await self.bot.tree.sync()
                print(f"Synced {len(synced)} commands with Discord API!")
                await interaction.response.send_message('Commands synced with API! Please wait a few minutes for changes to be reflected.')
            except Exception as e:
                print(f"Error syncing commands: {e}")


async def setup(bot):
    await bot.add_cog(Devtools(bot))
