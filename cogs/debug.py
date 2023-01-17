import discord
from discord import app_commands
from discord.ext import commands
import Keys

class Debug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # sets the client variable so we can use it in cogs
        self.description = 'A set of tools related to debugging the bot.'

    @commands.command(name='ping', help='Tests if the bot is online and functional.')
    async def ping(self, ctx):
        # an example command with cogs
        await ctx.send('Pong!')

    @commands.command(name='slash-sync', help='A dev-only command used to synchronize commands with the Discord API.')
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

    @commands.command(name='commands', help='Lists all commands available.')
    async def commands(self, ctx, module=None, cmd=None):
        cogs = self.bot.cogs
        if (module is None) and (cmd is None):
            # List all modules
            embed = discord.Embed(title='Ice Cream Bot Modules', description='Use "/help <module>" for more info.')
            for cog in cogs:
                embed.add_field(name=cog.qualified_name, value=cog.description, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send('Invalid command syntax. Try "$help" for more info.')
        # for key in cogs.keys():
        #     commands = cogs[key].get_commands()
        #     app_commands = cogs[key].get_app_commands()
        #     for command in commands:
        #         print(f'{command.name} -- {command.help}')
        #     for app_command in app_commands:
        #         print(f'{app_command.name} -- {app_command.description}')
        # await ctx.send('Cogs printed!')

async def setup(bot):
    await bot.add_cog(Debug(bot))
