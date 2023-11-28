from .__init__ import *


@bot.on_message(
    filters.regex(pattern=REGEX_PT) & ~filters.regex(pattern=r"/yt") & filters.private
)
async def ytmusicdl(app, message):
    url = message.text
    await message_helper(url, message)


@bot.on_message(command_creator("yt"))
async def ytmusicdl(app, message):
    args = message.text.split(" ")

    if len(args) == 1:
        return await message.reply("<b>Use like this : </b><code>/yt link</code>")
    elif len(args) == 2:
        url = args[-1].strip()
    else:
        return await message.reply("<b>Use like this : </b><code>/yt link</code>")

    await message_helper(url, message)


async def message_helper(url: str, message: Message):
    if "playlist" in url.lower():
        reply = await message.reply_photo(
            photo=choice(ICONS),
            caption=STATUS.format(
                title="Importing Songs from Playlist", status="Extracting...📂"
            ),
        )
        await yt_music_playlist_dl_helper(url, reply, message.from_user)
    else:
        try:
            yt_id = extract_yt_id(url)
        except Exception as e:
            return await message.reply_photo(
                photo=choice(ICONS),
                caption=STATUS.format(title=url, status="Invalid...⛔️"),
            )
        reply = await message.reply_photo(
            photo=choice(ICONS),
            caption=STATUS.format(
                title="Checking Song in Database", status="Checking...📝"
            ),
        )
        await yt_music_dl_helper(url, reply, message.from_user)


async def yt_music_dl_helper(
    url: str,
    reply: Message | CallbackQuery,
    user: User,
    playlist: bool = False,
    song_info: dict = None,
):
    try:
        yt_id = extract_yt_id(url)
    except Exception as e:
        return

    song_upload_start_time = time()

    if not playlist:
        if isinstance(reply, CallbackQuery):
            await reply.edit_message_media(
                InputMediaPhoto(
                    media=choice(ICONS),
                    caption=STATUS.format(
                        title="Checking Song in Database", status="Checking...📝"
                    ),
                )
            )
        if saved_song := await check_song(yt_id):
            return await reply.edit_message_media(
                InputMediaAudio(
                    media=saved_song["file_id"],
                    caption=CAPTION.format(
                        title=saved_song["title"], artist=saved_song["artist"]
                    )
                    + f"\n<b>𝗬𝗼𝘂𝗿 𝗦𝗼𝗻𝗴 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 - </b>{user.mention}",
                )
            )
    else:
        await reply.edit_message_media(
            InputMediaPhoto(
                media=choice(ICONS),
                caption=STATUS.format(
                    title="Checking Song in Database", status="Checking...📝"
                ),
            )
        )

        if saved_song := await check_song(yt_id):
            await asyncio.sleep(3)
            await reply.edit_message_media(
                InputMediaPhoto(
                    media=choice(ICONS),
                    caption=STATUS.format(
                        title=f"{saved_song['title']} - {saved_song['artist']} ({song_info.get('current_song')}/{song_info.get('total_songs')})",
                        status="Found...✅",
                    ),
                )
            )
            await asyncio.sleep(3)
            return await bot.send_cached_media(
                chat_id=reply.chat.id,
                file_id=saved_song["file_id"],
                caption=CAPTION.format(
                    title=saved_song["title"],
                    artist=saved_song["artist"],
                ),
            )

    song_path = os.path.join(os.getcwd(), f"song_{user.id}")

    await asyncio.sleep(3)
    await reply.edit_message_media(
        InputMediaPhoto(
            media=choice(ICONS),
            caption=STATUS.format(
                title=f'{song_info.get("title")} ({song_info.get("current_song")}/{song_info.get("total_songs")})'
                if playlist
                else f"Song ({yt_id})",
                status="Downloading...📥",
            ),
        )
    )

    ydl_opts = ytdl_opts(song_path)

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url)
    except:
        try:
            shutil.rmtree(song_path)
        except:
            pass
        if not playlist:
            return await reply.edit_message_media(
                InputMediaPhoto(
                    media=choice(ICONS),
                    caption=STATUS.format(title=url, status="Unavailable...❎"),
                )
            )
        else:
            return await bot.send_photo(
                chat_id=reply.chat.id,
                photo=choice(ICONS),
                caption=STATUS.format(
                    title=song_info.get("title"), status="Unavailable...❎"
                ),
            )
    try:
        await reply.edit_message_media(
            InputMediaPhoto(
                media=YT_THUMB_LINK.format(id=info["id"]),
                caption=STATUS.format(
                    title=f'{song_info.get("title")} ({song_info.get("current_song")}/{song_info.get("total_songs")})'
                    if playlist
                    else info["title"],
                    status="Uploading...📤",
                ),
            )
        )
    except Exception as e:
        print(str(e))

    await song_upload(reply, info, user, song_path, song_upload_start_time, playlist)


async def yt_music_playlist_dl_helper(url: str, reply: Message, user: User):
    current_song = 1
    try:
        playlist_upload_start_time = time()
        with yt_dlp.YoutubeDL({"extract_flat": True}) as ydl:
            info = ydl.extract_info(url)

        for song in info["entries"]:
            await yt_music_dl_helper(
                song["url"],
                reply,
                user,
                True,
                {
                    "title": song["title"],
                    "current_song": current_song,
                    "total_songs": info["playlist_count"],
                },
            )
            current_song += 1
            await asyncio.sleep(3)

        playlist_thumbnail = await loop.run_in_executor(
            ThreadPoolExecutor(1),
            lambda: dl_thumbnail_image(
                playlist_thumbnail_url(info["thumbnails"][0]["url"]), user.id
            ),
        )
        playlist_upload_finish_time = get_readable_time(
            time() - playlist_upload_start_time
        )
        await bot.send_photo(
            chat_id=reply.chat.id,
            photo=playlist_thumbnail,
            caption=PLAYLIST_UPLOADED.format(
                song_num=info["playlist_count"],
                time=playlist_upload_finish_time,
                duration=playlist_duration(info["entries"]),
                mention=user.mention(),
                playlist=info["title"],
            ),
        )
        await reply.delete()
        await bot.send_message(
            chat_id=TeleConf.LOG_CHANNEL,
            text=PLAYLIST_LOG_CHANNEL_MESSAGE.format(
                requested_by=user.mention,
                playlist_name=info["title"],
                playlist_url=info["original_url"],
                duration=playlist_duration(info["entries"]),
                song_count=info["playlist_count"],
                time_taken=playlist_upload_finish_time,
            ),
            disable_web_page_preview=True,
        )
        os.remove(playlist_thumbnail)

    except Exception as e:
        return await reply.edit_message_media(
            InputMediaPhoto(
                media=choice(ICONS),
                caption=STATUS.format(title=str(e), status="Error...❌"),
            )
        )
