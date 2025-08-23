import os
from dotenv import load_dotenv, find_dotenv

def load_env() -> None:
    load_dotenv(find_dotenv())
    
def get_key(key: str, default=None):
    return os.getenv(key, default)

