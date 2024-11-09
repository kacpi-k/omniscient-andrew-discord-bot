import os

import discord
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GROQ_CLIENT = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.2-90b-vision-preview"

# Kanały w kolejności: test
ALLOWED_CHANNELS_ID = [1303720981407465592]

# Userzy w kolejności:
ALLOWED_USERS_ID = []

intents = discord.Intents.default()
intents.message_content = True
discordClient = discord.Client(intents=intents)


def split_message(message: str, max_length: int = 2000):
    return [message[i:i + max_length] for i in range(0, len(message), max_length)]


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
        query = message.content[len('!pytaj '):]
        print(f'Otrzymałem zapytanie: {query}')

        content = "Zachowuj się jakbyś miał na imię Andrzej. " + query + " Odpowiedz w języku polskim."

        chat_completion = GROQ_CLIENT.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            model=MODEL,
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
        )

        answer = chat_completion.choices[0].message.content if chat_completion.choices else "Nie mogę odpowiedzieć na to pytanie"

        message_fragments = split_message(answer)
        for fragment in message_fragments:
            await message.channel.send(fragment)


discordClient.run(TOKEN)
