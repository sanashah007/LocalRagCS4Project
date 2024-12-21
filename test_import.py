from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access variables securely
api_key = os.getenv('GROQ_API_KEY')
print(api_key)