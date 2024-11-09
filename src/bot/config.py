import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GROQ_CLIENT = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.2-90b-vision-preview"

ALLOWED_CHANNELS_ID = [1303720981407465592]
ALLOWED_USERS_ID = []