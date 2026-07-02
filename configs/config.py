import os

from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME")

VERSION = os.getenv("VERSION")

DEBUG = os.getenv("DEBUG")

HOST = os.getenv("HOST")

PORT = int(os.getenv("PORT"))

LOG_LEVEL = os.getenv("LOG_LEVEL")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")