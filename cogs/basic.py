import discord
from discord import app_commands
from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = 'A set of basic commands to get started with the bot.'
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

    @app_commands.command(name='ping', 
                    description='Tests if the bot is online and functional.')
    async def ping(self, interaction: discord.Interaction) -> None:
        # an example command with cogs
        await interaction.response.send_message('Pong!')

    @app_commands.command(name='help', description='Lists all available commands.')
    async def help(self, interaction: discord.Interaction, module: str = None, command: str = None) -> None:
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

async def setup(bot):
    # NOTE: The bot comes with a default "$help" command, the one registered
    # in this module is a separate, custom one.
    await bot.add_cog(Basic(bot))
