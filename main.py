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

@bot.event
async def on_ready():
    print(f'Logged in as: {Colors.CYAN+bot.user.name+Colors.RESET} - {bot.user.id}\nVersion: {discord.__version__}\n')


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
