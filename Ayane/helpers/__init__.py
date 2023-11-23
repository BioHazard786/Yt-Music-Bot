from Ayane import bot, loop
from pyrogram import filters
from pyrogram.types import InputMediaAudio
from urllib.parse import urlparse, parse_qs
from Ayane.config import CAPTION, TeleConf, REGEX_PT
from Ayane.database.mongodb import save_song_to_db
import os
import re
import requests
import yt_dlp
import asyncio
