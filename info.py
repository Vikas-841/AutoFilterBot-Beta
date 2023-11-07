import re, sys, logging
from os import environ
from Script import script

logging.basicConfig(level=logging.ERROR)

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
API_ID = 25826048
API_HASH = "b486ee260537697fdfc56b2b61cbc049"
BOT_TOKEN = "6882915473:AAFykN6NnKYxbV9sYDxo0orMjnEQBjg-L_A"
PORT = 8080

# Bot pics
PICS = [
    "https://telegra.ph/file/58fef5cb458d5b29b0186.jpg",
    "https://telegra.ph/file/f0aa4f433132769f8970c.jpg",
    "https://telegra.ph/file/f515fbc2084592eca60a5.jpg",
    "https://telegra.ph/file/20dbdcffaa89bd3d09a74.jpg",
    "https://telegra.ph/file/6045ba953af4def846238.jpg"
]

# Bot Admins
ADMINS = [6882915473]  # Replace with your admin IDs

# Channels
INDEX_CHANNELS = [-1002126379861]
AUTH_CHANNEL = [-1002126379861]
LOG_CHANNEL = -1002126379861
SUPPORT_GROUP = -1002126379861

# MongoDB information
DATABASE_URL = "mongodb+srv://bikashxd:bgtop@cluster0.gh1hqe3.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "Cluster0"
COLLECTION_NAME = "Files"

# Links
SUPPORT_LINK = "https://t.me/SL_Bots_Support"
UPDATES_LINK = "https://t.me/SL_Bots_Updates"

# Bot settings
AUTO_FILTER = True
IMDB = True
SPELL_CHECK = True
SHORTLINK = False
DELETE_TIME = 3600  # Add time in seconds
AUTO_DELETE = False
WELCOME = False
PROTECT_CONTENT = False
LONG_IMDB_DESCRIPTION = False
LINK_MODE = True
CACHE_TIME = 300

# Other
IMDB_TEMPLATE = script.IMDB_TEMPLATE
FILE_CAPTION = script.FILE_CAPTION
SHORTLINK_URL = "mdiskshortner.link"
SHORTLINK_API = "36f1ae74ba1aa01e5bd73bdd0bc22aa915443501"
VERIFY_EXPIRE = 86400  # Add time in seconds
IS_VERIFY = False
WELCOME_TEXT = script.WELCOME_TEXT
TUTORIAL = "https://t.me/SL_Bots_Updates"
INDEX_EXTENSIONS = ["mp4", "mkv"]

# Stream features vars
BIN_CHANNEL = -1002126379861
URL = "https://your-api-url-here/"
