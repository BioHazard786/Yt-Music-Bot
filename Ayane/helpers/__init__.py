from Ayane import bot, loop
from pyrogram import filters, enums
from pyrogram.types import (
    InputMediaAudio,
    InputMediaPhoto,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
    User,
)
from urllib.parse import urlparse, parse_qs
from Ayane.config import (
    CAPTION,
    TeleConf,
    REGEX_PT,
    ICONS,
    SONG_UPLOADED,
    LOG_CHANNEL_MESSAGE,
    YT_THUMB_LINK,
    INLINE_SONG_UPLOADED,
    REGEX_PT_SPOTIFY,
)
from Ayane.database.mongodb import save_song_to_db
from random import choice
from time import time
import os
import re
import requests
import yt_dlp
import asyncio
import glob
