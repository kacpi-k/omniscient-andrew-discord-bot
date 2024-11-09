from .config import ALLOWED_CHANNELS_ID, GROQ_CLIENT
from src.bot.groq_service import get_groq_response


def split_message(message: str, max_length: int = 2000):
    return [message[i:i + max_length] for i in range(0, len(message), max_length)]

async def handle_message(client, message):
    if message.channel.id not in ALLOWED_CHANNELS_ID:
        print("Zły kanał")
        return

    if message.author == client.user:
        return

    if message.content.startswith('!pytaj'):
        query = message.content[len('!pytaj')]
        print(f'Otrzymałem zapytanie {query}')

        content = "Zachowuj się jakbyś miał na imię Andrzej. " + query + " Odpowiedz w języku polskim."
        answer = get_groq_response(content)

        message_fragments = split_message(answer)
        for fragment in message_fragments:
            await message.channel.send(fragment)