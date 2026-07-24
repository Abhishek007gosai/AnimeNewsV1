import os

# Read configuration from environment variables
API_ID = int(os.environ.get("API_ID", 29245477))
API_HASH = os.environ.get("API_HASH", "0abc83883262245c90ca337b7a0375c4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
URL_A = os.environ.get("URL_A", "https://www.animenewsnetwork.com/newsfeed/rss.xml?ann-edition=us")
URL_B = os.environ.get("URL_B", "")
START_PIC = os.environ.get("START_PIC", "")
MONGO_URI = os.environ.get("MONGO_URI", "")
ADMINS = [int(x.strip()) for x in os.environ.get("ADMINS", "8771195193").split(",") if x.strip()]
