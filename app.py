import nextcord, os
from nextcord.ext import commands

TESTING_GUILD_ID = os.environ['TESTING_GUILD_ID']

intents = nextcord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

@bot.command()
async def connection(ctx):
    await ctx.send('Hello!')

bot.run(os.environ['TOKEN'])
