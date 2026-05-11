import os
from dotenv.cli import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "bigdata"
COLLECTION_NAME = "instagram_events"