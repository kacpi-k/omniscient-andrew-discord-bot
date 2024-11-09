import asyncio
from src.bot.groq_service import get_groq_response
from .utils import split_message, capitalize_first_letter


async def handle_message(message):
    query = message.content[len('!pytaj')]
    print(f'Otrzymałem zapytanie {query}')

    content = "Zachowuj się jakbyś miał na imię Andrzej. " + query + " Odpowiedz w języku polskim."
    answer = get_groq_response(content)

    message_fragments = split_message(answer)
    for fragment in message_fragments:
        await message.channel.send(fragment)

async def start_timer(message):
    try:
        time_minutes = int(message.content.split()[1])
    except:
        await message.channel.send('Podaj czas w minutach, np. !czekaj 15')
        return

    name = str(message.content.split()[2])
    wait_for = capitalize_first_letter(name)

    await message.channel.send(f'Oczekiwanie rozpoczęte! {wait_for} ma {time_minutes} min na dołączenie.')

    time_seconds = time_minutes * 60

    await asyncio.sleep(time_seconds)

    await message.channel.send(f'Czas minął. Czy {wait_for} zdążył?')