from os.path import dirname, basename, isfile, join
from .config import TeleConf
from pyrogram import Client, enums
from importlib import import_module
from subprocess import Popen
import glob
import uvloop

__all__ = ["bot", "loop"]

uvloop.install()

bot = Client(
    "Ayane San",
    api_id=TeleConf.API_ID,
    api_hash=TeleConf.API_HASH,
    bot_token=TeleConf.BOT_TOKEN,
    parse_mode=enums.ParseMode.HTML,
    max_concurrent_transmissions=1000,
).start()

loop = bot.loop  # ? Current event loop

server = Popen(
    f"gunicorn web.app:app --bind 0.0.0.0:8000", shell=True
)  # ? Important for deploying to Koyeb.app

files = glob.glob(join(join(dirname(__file__), "plugins"), "*py"))
plugins = [
    basename(f)[:-3] for f in files if isfile(f) and not f.endswith("__init__.py")
]

for plugin in plugins:
    import_module("Ayane.plugins." + plugin)
