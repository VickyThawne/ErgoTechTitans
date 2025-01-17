import os
import dotenv
import urllib.parse


from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Load environment variables from .env file
    username = os.getenv("POSTGRES_USER")
    dbname = os.getenv("POSTGRES_DB")
    encoded_password = urllib.parse.quote_plus(os.getenv("POSTGRES_PASS"))

    SQLALCHEMY_DATABASE_URI = f'postgresql://{username}:{encoded_password}@localhost:5433/{dbname}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
