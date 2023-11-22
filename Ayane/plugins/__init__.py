from Ayane import bot
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InputMediaAnimation,
    InputMediaPhoto,
    InlineQueryResultCachedAudio,
    InlineQuery,
)
from Ayane.helpers.utils import (
    command_creator,
    get_readable_file_size,
    get_readable_time,
    ytdl_opts,
    extract_yt_id,
)
from Ayane.helpers.song_upload import song_upload
from Ayane.database.mongodb import (
    check_song,
    song_title_matching,
    initial_search_result,
)
from Ayane.config import botStartTime, HELP, REGEX_PT
import shutil
import psutil
import os
from time import time
import yt_dlp
