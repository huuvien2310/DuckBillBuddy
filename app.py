import nextcord, os
from nextcord.ext import commands
from dotenv import load_dotenv
from io import BytesIO
import requests
import aiohttp
import set12

load_dotenv()

TESTING_GUILD_ID = os.getenv("TESTING_GUILD_ID")

intents = nextcord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


@bot.command()
async def bagsize(ctx):
    costs = [30, 25, 18, 10, 9]

    message = "\n".join(
        f"{cost} cost: {size}" for cost, size in enumerate(costs, start=1)
    )
    await ctx.send(message)


@bot.command()
async def loottable(ctx):
    await ctx.send("")


@bot.command()
async def fortune(ctx):
    await ctx.send(set12.fortunetable())


@bot.command()
async def goldenquest(ctx):
    imgur_url = set12.golden_quest()
    async with aiohttp.ClientSession() as session:
        async with session.get(imgur_url) as resp:
            if resp.status != 200:
                return await ctx.send("Could not download file...")
            data = BytesIO(await resp.read())

            await ctx.send(file=nextcord.File(data, "goldenquest.png"))


@bot.command()
async def missedconnection(ctx):
    await ctx.send(file=nextcord.File("missedconnection.png"))


@bot.command()
async def missedconnectionxerath(ctx):
    await ctx.send(file=nextcord.File("f0mpjw4ddzv41.png"))


bot.run(os.getenv("TOKEN"))
