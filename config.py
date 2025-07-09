from dotenv import load_dotenv
import os


load_dotenv()

def get_username():
    return os.getenv("USERNAME", "Guest")
