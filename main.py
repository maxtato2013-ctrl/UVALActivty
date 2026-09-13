import discord
from discord.ext import commands

from config import TOKEN
from commands import setup_commands

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.reactions = True
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

setup_commands(bot)


@bot.event
async def on_ready():
    print("=" * 40)
    print(f"Logged in as {bot.user}")
    print("=" * 40)
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(e)


bot.run(TOKEN)
