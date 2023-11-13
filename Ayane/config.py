from os import getenv
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env")
except:
    pass

botStartTime = time()

BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
DUMP_CHANNEL = int(getenv("DUMP_CHANNEL"))
MONGODB = getenv("MONGODB")

CAPTION = """
<b>Title</b> - <code>{title}</code>
<b>Artist</b> - <code>{uploader}</code>
"""
YT_THUMB_LINK = "https://i.ytimg.com/vi/{id}/mqdefault.jpg"
