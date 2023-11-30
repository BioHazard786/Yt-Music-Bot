from .__init__ import *
from Ayane.plugins.youtube import yt_music_dl_helper


@bot.on_message(command_creator("sp"))
async def spotify(app: Client, message: Message):
    args = message.text.split(" ", maxsplit=1)

    if len(args) == 1:
        return await message.reply(
            "<b>Use like this : </b><code>/sp spotify_link</code>"
        )
    elif len(args) == 2:
        url = args[-1].strip()
    else:
        return await message.reply(
            "<b>Use like this : </b><code>/sp spotify_link</code>"
        )

    if "playlist" in url.lower() or "album" in url.lower():
        return await message.reply_photo(
            photo=choice(ICONS),
            caption="<b>Playlists and Albums are not supported Currently :(</b>",
        )

    try:
        spotify_id = extract_spotify_id(url)
    except Exception as e:
        return await message.reply_photo(
            photo=choice(ICONS),
            caption=STATUS.format(title=url, status="Invalid...⛔️"),
        )
    await spotify_helper(spotify_id, message)


@bot.on_message(
    filters.regex(pattern=REGEX_PT_SPOTIFY)
    & ~filters.regex(pattern=r"/sp")
    & filters.private
)
async def ytmusicdl(app, message):
    url = message.text.strip()

    if "playlist" in url.lower() or "album" in url.lower():
        return await message.reply_photo(
            photo=choice(ICONS),
            caption="<b>Playlists and Albums are not supported Currently :(</b>",
        )

    try:
        spotify_id = extract_spotify_id(url)
    except Exception as e:
        return await message.reply_photo(
            photo=choice(ICONS),
            caption=STATUS.format(title=url, status="Invalid...⛔️"),
        )
    await spotify_helper(spotify_id, message)


async def spotify_helper(spotify_id: str, message: Message):
    reply = await message.reply_photo(
        photo=choice(ICONS),
        caption=STATUS.format(
            title="Extracting track info from Spotify Link", status="Extracting...📂"
        ),
    )
    track_info = await loop.run_in_executor(
        ThreadPoolExecutor(1), lambda: SPOTIFY_API.track(spotify_id)
    )
    search_query = "{} {} {}".format(
        track_info["name"],
        track_info["album"]["name"],
        track_info["artists"][0]["name"],
    )
    search_results = await loop.run_in_executor(
        ThreadPoolExecutor(1),
        lambda: YT_MUSIC.search(query=search_query, filter="songs"),
    )
    if len(search_results) == 0:
        return await reply.edit_media(
            InputMediaPhoto(
                media=track_info["album"]["images"][0]["url"],
                caption=f"➜ 𝗡𝗼 𝗥𝗲𝘀𝘂𝗹𝘁𝘀 𝗙𝗼𝘂𝗻𝗱 𝗳𝗼𝗿 - <i>{track_info['name']} - {track_info['artists']}",
            )
        )

    url = f"https://youtu.be/{search_results[0]['videoId']}"
    await reply.edit_media(
        InputMediaPhoto(
            media=track_info["album"]["images"][0]["url"],
            caption=STATUS.format(
                title="Checking Song in Database", status="Checking...📝"
            ),
        )
    )
    await yt_music_dl_helper(
        url=url,
        reply=reply,
        user=message.from_user,
        song_info={"title": search_results[0]["title"]},
    )
