from Ayane import bot, loop
from pyrogram import filters
from pyrogram.types import InputMediaAudio
from urllib.parse import urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor
from Ayane.config import CAPTION, YT_THUMB_LINK, DUMP_CHANNEL
from Ayane.database.mongodb import save_song_to_db
import os
import requests
