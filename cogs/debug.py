import discord
from discord import app_commands
from discord.ext import commands
import Keys

class Debug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # sets the client variable so we can use it in cogs
        self.description = 'A set of tools related to debugging the bot.'

    async def cog_app_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        print('An error occurred in the following command:', interaction.command)
        print('ERROR:', str(error))

    @commands.command(name='ping', 
                    description='Tests if the bot is online and functional.')
    async def ping(self, ctx):
        # an example command with cogs
        await ctx.send('Pong!')

    @commands.command(name='slash-sync', 
                    description='A dev-only command used to synchronize commands with the Discord API.')
    async def slash_sync(self, ctx):
        if ctx.author.id == Keys.ZGELL_ID:
            try:
                synced = await self.bot.tree.sync()
                print(f"Synced {len(synced)} commands with Discord API!")
            except Exception as e:
                print(f"Error syncing commands: {e}")

    @app_commands.command(name='slash', 
                        description='A test command for slash commands. Does absolutely nothing.')
    async def slash(self, interaction: discord.Interaction):
        # an example command with cogs
        # await ctx.send('Yeeoooo!')
        await interaction.response.send_message("Yeeoooo!", ephemeral=True)

    @app_commands.command(name='help', description='Lists all available commands.')
    async def help(self, interaction: discord.Interaction, module: str = None, command: str = None):
        if (module is None) and (command is None):
            # List all modules
            embed = discord.Embed(title='Ice Cream Bot Modules', description='Use "/help <module>" for more info.')
            for cog in self.bot.cogs.keys():
                cog_name = cog
                cog_desc = self.bot.cogs[cog].description
                embed.add_field(name=cog_name, value=cog_desc, inline=False)
            await interaction.response.send_message(embed=embed)

        elif (module is not None) and (command is None):
            # List all commands within the specified module
            # Firstly, make sure module exists
            formatted_module_name = module[0].upper() + module[1:]  # Force first letter to be uppercase
            if (formatted_module_name in self.bot.cogs.keys()):
                # Valid cog, display info for it
                cog = self.bot.cogs[formatted_module_name]
                embed = discord.Embed(title=f'Ice Cream Bot - {formatted_module_name}', 
                    description=f'{cog.description}\nUse /help {formatted_module_name} <command> for more info.')
                # First scan all regular commands
                for cmd in cog.get_commands():
                    # print(command.name, command.description, type(command.description))
                    if cmd.description == '':
                        desc = 'No description.'
                    else:
                        desc = cmd.description
                    embed.add_field(name=cmd.name, value=desc)
                # Then scan all slash commands
                for app_cmd in cog.get_app_commands():
                    if app_cmd.description == '':
                        desc = 'No description.'
                    else:
                        desc = app_cmd.description
                    embed.add_field(name=app_cmd.name, value=desc)
                await interaction.response.send_message(embed=embed)
            else:
                # Module does not exist
                await interaction.response.send_message(f'WARNING: Module {formatted_module_name} does not exist.')

        elif (module is not None) and (command is not None):
            # List all information pertaining to a certain command.
            formatted_module_name = module[0].upper() + module[1:]
            if (formatted_module_name in self.bot.cogs.keys()):
                cog = self.bot.cogs[formatted_module_name]
                # cmds = [cmd for cmd in cog.get_commands()]
                cmds = {cmd.name: cmd for cmd in cog.get_commands()}
                # app_cmds = [cmd for cmd in cog.get_app_commands()]
                app_cmds = {cmd.name: cmd for cmd in cog.get_app_commands()}
                # total_cmds = cmds + app_cmds
                total_cmds = dict()
                total_cmds.update(cmds)
                total_cmds.update(app_cmds)
                if command.lower() in total_cmds.keys():
                    # Valid module and valid command, print info
                    command_object = total_cmds[command.lower()]
                    embed = discord.Embed(title=f'Ice Cream Bot - **{command.lower()}**', 
                                        description=command_object.description)
                    await interaction.response.send_message(embed=embed)
                    
                else:
                    await interaction.response.send_message(f'WARNING: Command {command.lower()} does not exist.')
            else:
                await interaction.response.send_message(f'WARNING: Module {formatted_module_name} does not exist.')

        else:
            await interaction.response.send_message('/help called!')

    # @commands.command(name='help', help='Lists all commands available.')
    # async def help(self, ctx, module=None, cmd=None):
    #     cogs = self.bot.cogs
    #     if (module is None) and (cmd is None):
    #         # List all modules
    #         embed = discord.Embed(title='Ice Cream Bot Modules', description='Use "/help <module>" for more info.')
    #         for cog in cogs:
    #             embed.add_field(name=cog.qualified_name, value=cog.description, inline=False)
    #         await ctx.send(embed=embed)
    #     else:
    #         await ctx.send('Invalid command syntax. Try "$help" for more info.')
    #     # for key in cogs.keys():
    #     #     commands = cogs[key].get_commands()
    #     #     app_commands = cogs[key].get_app_commands()
    #     #     for command in commands:
    #     #         print(f'{command.name} -- {command.help}')
    #     #     for app_command in app_commands:
    #     #         print(f'{app_command.name} -- {app_command.description}')
    #     # await ctx.send('Cogs printed!')

async def setup(bot):
    # By default, Discord.py includes a help command. It must be removed first.
    await bot.add_cog(Debug(bot))
