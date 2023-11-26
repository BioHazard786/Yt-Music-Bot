from Ayane import bot, loop
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InputMediaAnimation,
    InputMediaPhoto,
    InlineQueryResultCachedAudio,
    InlineQuery,
    User,
)
from Ayane.helpers.utils import (
    command_creator,
    get_readable_file_size,
    get_readable_time,
    ytdl_opts,
    extract_yt_id,
    playlist_duration,
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
)
from time import time
from random import choice
from concurrent.futures import ThreadPoolExecutor
import shutil
import psutil
import os
import yt_dlp
import asyncio
