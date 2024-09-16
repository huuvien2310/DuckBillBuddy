import nextcord, os
from nextcord.ext import commands
from dotenv import load_dotenv
import requests

load_dotenv()

TESTING_GUILD_ID = os.getenv('TESTING_GUILD_ID')

intents = nextcord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def connection(ctx):
    await ctx.send('Hello!')

@bot.command()
async def augment(ctx):
    response = requests.get("https://ddragon.leagueoflegends.com/cdn/13.24.1/data/en_US/tft-arena.json")
    print(response.content)
    await ctx.send(response)

bot.run(os.getenv('TOKEN'))