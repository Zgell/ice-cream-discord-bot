'''
Ice Cream Bot Main File
'''

'''
RANDOM IDEAS FOR THIS BOT
- Use an OpenAI API? Only if free though
https://beta.openai.com/docs/api-reference/introduction
- Some kind of inventory system similar to Unbelievaboat?
- Something that links to channel points on Twitch (if possible?)
- Twitch API integration?
'''

import asyncio
from color.colors import Colors
import discord
from discord.ext import commands
from Keys import DISCORD_TOKEN as SECRET_KEY

initial_extensions = [
    'cogs.fun',
    'cogs.debug'
]

bot = commands.Bot(command_prefix='$', description='A bot for general-purpose Discord functionality.', intents=discord.Intents.all())
# bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as: {Colors.CYAN+bot.user.name+Colors.RESET} - {bot.user.id}\nVersion: {discord.__version__}\n')

# @bot.command(name='help', help='Lists all commands available.')
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


async def main():
    '''Loads all extensions asynchronously and starts the bot when done.'''
    # Load all extensions
    print('Loading extension...')
    for extension in initial_extensions:
        print(f'Loading {extension}...')
        await bot.load_extension(extension)
    print('Starting bot...\n')
    await bot.start(SECRET_KEY)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
