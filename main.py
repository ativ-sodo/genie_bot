import discord
from discord.ext import commands

intents = discord.Intents.all()

cogs: list = [
    "functions.send",
    "functions.verify",
    "functions.dashboard",
]

client = commands.Bot(
    command_prefix='!',
    help_command=None,
    intents=intents,
)


@client.event
async def on_ready():
    print("Genie Bot is ready!")

    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game("Genie Bot")
    )

    for cog in cogs:
        try:
            print(f"Loading cog {cog}")
            await client.load_extension(cog)
            print(f"Loaded cog {cog}")
        except Exception as e:
            exc = "{} : {}".format(type(e).__name__, e)
            print("Failed to load cog {}\n{}".format(cog, exc))


client.run('MTA2NzcxNDczNTkyNTEyMTA2NA.GW3tpR.vVXPjbUdyFqycMSJE_GPvWnZS14sOLq9-A2j2A')