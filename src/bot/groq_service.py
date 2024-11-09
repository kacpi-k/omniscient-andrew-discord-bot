from .config import GROQ_CLIENT, MODEL
from .utils import print_response_usage


def get_groq_response(content: str) -> str:
    chat_completion = GROQ_CLIENT.chat.completions.create(
        messages=[{
            "role": "user",
            "content": content
        }],
        model=MODEL,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
    )

    print_response_usage(chat_completion)

    return chat_completion.choices[0].message.content if chat_completion.choices else "Nie mogę odpowiedzieć na to pytanie"