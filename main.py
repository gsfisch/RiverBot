import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from music_cog import music_cog
import asyncio


def main():
    load_dotenv()

    # Create RiverBot
    intents = discord.Intents.default()
    intents.message_content = True
    my_bot = commands.Bot(command_prefix='/r', intents=intents)


    # Add Cogs to bot
    loop = asyncio.new_event_loop()
    loop.run_until_complete(my_bot.add_cog(music_cog(my_bot)))


    # Run bot
    my_bot.run(os.getenv('DISCORD_TOKEN'))


if __name__ == "__main__":
    main()
