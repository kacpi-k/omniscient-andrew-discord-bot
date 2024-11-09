import os
from bot.client import discordClient

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    discordClient.run(TOKEN)
