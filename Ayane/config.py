from os import getenv
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env")
except:
    pass

botStartTime = time()


class TeleConf(object):
    BOT_TOKEN = getenv("BOT_TOKEN")
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    DUMP_CHANNEL = int(getenv("DUMP_CHANNEL"))


class MongoConf(object):
    MONGODB = getenv("MONGODB")
    DB_NAME = getenv("DB_NAME", "MusicDump")


REGEX_PT = r"(youtu.*be.*)\/(watch\?v=|embed\/|v|shorts|)(.*?((?=[&#?])|$))"
CAPTION = """
<b>Title</b> - <code>{title}</code>
<b>Artist</b> - <code>{artist}</code>
"""
YT_THUMB_LINK = "https://i.ytimg.com/vi/{id}/mqdefault.jpg"

HELP = f"""
/start: Check bot is alive or not
/stats: Show stats of the machine where the bot is hosted in.
/yt [yt_url]: Download song and dump it in channel
/help: To get this message
"""
