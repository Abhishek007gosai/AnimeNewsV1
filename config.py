import os

# Read configuration from environment variables
API_ID = int(os.environ.get("API_ID", ))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
URL_A = os.environ.get("URL_A", "https://www.animenewsnetwork.com/newsfeed/rss.xml?ann-edition=us")
URL_B = os.environ.get("URL_B", "")
START_PIC = os.environ.get("START_PIC", "")
MONGO_URI = os.environ.get("MONGO_URI", "")
ADMINS = [int(x.strip()) for x in os.environ.get("ADMINS", "").split(",") if x.strip()]
