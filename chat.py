from dotenv import load_dotenv
import os
import cohere

load_dotenv()
secret_key = os.getenv("API_KEY")
# print(secret_key)
# co = cohere.Client(secret_key)