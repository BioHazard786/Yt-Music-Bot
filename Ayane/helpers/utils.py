from .__init__ import *

SIZE_UNITS = ["B", "KB", "MB", "GB", "TB", "PB"]


def command_creator(command_name: str):
    commands = [command_name, f"{command_name}@{bot.get_me().username}"]
    return filters.command(commands)


def get_readable_time(seconds: int) -> str:
    result = ""
    (days, remainder) = divmod(seconds, 86400)
    days = int(days)
    if days != 0:
        result += f"{days}d "
    (hours, remainder) = divmod(remainder, 3600)
    hours = int(hours)
    if hours != 0:
        result += f"{hours}h "
    (minutes, seconds) = divmod(remainder, 60)
    minutes = int(minutes)
    if minutes != 0:
        result += f"{minutes}m "
    seconds = int(seconds)
    result += f"{seconds}s"
    return result


def get_readable_file_size(size_in_bytes: int) -> str:
    if size_in_bytes is None:
        return "0B"
    index = 0
    while size_in_bytes >= 1024:
        size_in_bytes /= 1024
        index += 1
    try:
        return f"{round(size_in_bytes, 3)} {SIZE_UNITS[index]}"
    except IndexError:
        return "File too large"


def ytdl_opts(song_path: str):
    return {
        "format": "bestaudio/best",
        "writethumbnail": True,
        "keepvideo": False,
        "noplaylist": True,
        "windowsfilenames": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",
            },
            {
                "key": "FFmpegThumbnailsConvertor",
                "format": "jpg",
            },
            {
                "key": "FFmpegMetadata",
            },
            {
                "key": "EmbedThumbnail",
                "already_have_thumbnail": True,
            },
        ],
        "outtmpl": f"{song_path}/%(title)s.%(ext)s",
    }


def extract_yt_id(url: str):
    if match := re.search(REGEX_PT, url):
        return match[3]
    else:
        raise Exception("Link is Invalid")


def playlist_duration(songs: dict):
    total_duration = 0
    for song in songs:
        total_duration += song["duration"]
    return get_readable_time(total_duration)
