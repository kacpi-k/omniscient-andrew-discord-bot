import discord
from .commands import handle_message, start_timer
from .config import ALLOWED_CHANNELS_ID

intents = discord.Intents.default()
intents.message_content = True
discordClient = discord.Client(intents=intents)


@discordClient.event
async def on_ready():
    print(f'Zalogowano jako {discordClient.user}')

@discordClient.event
async def on_message(message):
    if message.channel.id not in ALLOWED_CHANNELS_ID:
        print("Zły kanał")
        return

    if message.author == discordClient.user:
        return

    if message.content.startswith('!pytaj'):
        await handle_message(message)

    if message.content.startswith('!czekaj'):
        await start_timer(message)