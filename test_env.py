import os

from dotenv import load_dotenv

load_dotenv()  # Загружает переменные из .env

api_key = os.getenv("EXCHANGE_RATE_API_KEY")
print(f"API Key: {api_key}")
