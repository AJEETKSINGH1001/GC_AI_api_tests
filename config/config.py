import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
PARSER_BASE_URL = os.getenv("PARSER_BASE_URL")
CLIENT_ID = os.getenv("client_id")
CLIENT_SECRET = os.getenv("client_secret")
GRANT_TYPE = os.getenv("grant_type")
