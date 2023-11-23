from .__init__ import *


@bot.on_message(filters.regex(pattern=REGEX_PT) & ~filters.regex(pattern=r"/yt"))
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
    url: str, reply: Message, user: User, playlist: bool = False, song_info: dict = None
):
    try:
        yt_id = extract_yt_id(url)
    except Exception as e:
        return

    if not playlist:
        if saved_song := await check_song(yt_id):
            await reply.delete()
            return await bot.send_cached_media(
                chat_id=reply.chat.id,
                file_id=saved_song["file_id"],
                caption=f"<b>Your Song has been Uploaded -</b> {user.mention()}",
            )
    else:
        await reply.edit_media(
            InputMediaPhoto(
                media=choice(ICONS),
                caption=STATUS.format(
                    title="Checking Song in Database", status="Checking...📝"
                ),
            )
        )

        if saved_song := await check_song(yt_id):
            await reply.edit_media(
                InputMediaPhoto(
                    media=choice(ICONS),
                    caption=STATUS.format(
                        title=f"{saved_song['title']} - {saved_song['artist']}",
                        status="Found...✅",
                    ),
                )
            )
            return await bot.send_cached_media(
                chat_id=reply.chat.id,
                file_id=saved_song["file_id"],
                caption=CAPTION.format(
                    title=saved_song["title"],
                    artist=saved_song["artist"],
                ),
            )

    song_path = os.path.join(os.getcwd(), f"music_{user.id}")

    await reply.edit_media(
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
            return await reply.edit_media(
                InputMediaPhoto(
                    media=choice(ICONS),
                    caption=STATUS.format(title=url, status="Invalid...⛔️"),
                )
            )
        else:
            return
    try:
        await reply.edit_media(
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
    except:
        pass

    await song_upload(reply, info, user, song_path, playlist)


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
            lambda: dl_thumbnail_image(info["thumbnails"][-1]["url"], user.id),
        )
        playlist_upload_finish_time = get_readable_time(
            time() - playlist_upload_start_time
        )
        await reply.reply_photo(
            photo=playlist_thumbnail,
            quote=True,
            caption=PLAYLIST_UPLOADED.format(
                song_num=info["playlist_count"], time=playlist_upload_finish_time
            ),
        )
        os.remove(playlist_thumbnail)

    except:
        return await reply.edit_media(
            InputMediaPhoto(
                media=choice(ICONS),
                caption=STATUS.format(title=url, status="Invalid...⛔️"),
            )
        )
