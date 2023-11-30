from Ayane import bot, loop
from pyrogram import Client, filters, enums
from pyrogram.types import (
    Message,
    InputMediaAnimation,
    InputMediaPhoto,
    InlineQueryResultCachedAudio,
    InlineQuery,
    User,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InputTextMessageContent,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    InputMediaAudio,
)
from Ayane.helpers.utils import (
    command_creator,
    get_readable_file_size,
    get_readable_time,
    ytdl_opts,
    extract_yt_id,
    playlist_duration,
    extract_spotify_id,
)
from Ayane.helpers.song_upload import song_upload
from Ayane.helpers.thumbnail_downloader import dl_thumbnail_image
from Ayane.database.mongodb import (
    check_song,
    song_title_matching,
    initial_search_result,
)
from Ayane.config import (
    botStartTime,
    TeleConf,
    HELP,
    REGEX_PT,
    ICONS,
    STATUS,
    PLAYLIST_UPLOADED,
    CAPTION,
    YT_THUMB_LINK,
    PLAYLIST_LOG_CHANNEL_MESSAGE,
    YT_MUSIC,
    SEARCH_RESULT,
    REGEX_PT_SPOTIFY,
    SPOTIFY_API,
)
from time import time
from random import choice
from concurrent.futures import ThreadPoolExecutor
from pytube import YouTube
import shutil
import psutil
import os
import yt_dlp
import asyncio
import re
