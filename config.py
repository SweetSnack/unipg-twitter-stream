from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

# settings
load_dotenv(join(dirname(__file__), '.env'))

CONSUMER_KEY = environ.get("CONSUMER_KEY")
CONSUMER_SECRET = environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = environ.get("ACCESS_TOKEN_SECRET")

# static path
STATIC_PATH = join(dirname(__file__), "server", "static")

# global variables
HASHTAGS = []
