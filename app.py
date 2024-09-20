import nextcord, os
from nextcord.ext import commands
from dotenv import load_dotenv
import requests

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


# TODO
@bot.command()
async def loottable(ctx):
    await ctx.send()


# TODO
@bot.command()
async def loot(ctx):
    await ctx.send()


@bot.command()
async def missedconnection(ctx):
    await ctx.send(file=nextcord.File("f0mpjw4ddzv41.png"))


@bot.command()
async def missedconnectionxerath(ctx):
    await ctx.send(file=nextcord.File("f0mpjw4ddzv41.png"))


bot.run(os.getenv("TOKEN"))
