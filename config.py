from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

# settings
load_dotenv(join(dirname(__file__), '.env'))

CONSUMER_KEY = environ.get("CONSUMER_KEY")
CONSUMER_SECRET = environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = environ.get("ACCESS_TOKEN_SECRET")

# global variables
HASHTAGS = []
