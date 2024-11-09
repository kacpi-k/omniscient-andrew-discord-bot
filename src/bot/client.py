import discord
from .commands import handle_message

intents = discord.Intents.default()
intents.message_content = True
discordClient = discord.Client(intents=intents)

@discordClient.event
async def on_ready():
    print(f'Zalogowano jako {discordClient.user}')

@discordClient.event
async def on_message(message):
    await handle_message(discordClient, message)