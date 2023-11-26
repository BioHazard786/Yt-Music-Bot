from .__init__ import *
from Ayane.helpers.utils import get_readable_time


async def song_upload(
    reply, info, user, song_path, song_upload_start_time, playlist=False
):
    artist = (
        info.get("artist")
        if info.get("artist")
        else info.get("uploader").replace(" - Topic", "")
    )
    artist = ", ".join(dict.fromkeys(artist.split(", ")))
    caption = CAPTION.format(
        title=info["title"],
        artist=artist,
    )

    final_song_path = glob.glob(os.path.join(song_path, "*m4a"))
    thumb_path = glob.glob(os.path.join(song_path, "*jpg"))

    if not final_song_path and not thumb_path:
        if playlist:
            return await bot.send_photo(
                chat_id=reply.chat.id,
                photo=choice(ICONS),
                caption=f"<b>{info['title']} Not Uploaded -</b> {user.mention()}",
            )
        else:
            return await reply.edit_media(
                InputMediaPhoto(
                    media=choice(ICONS),
                    caption=f"<b>{info['title']} Not Uploaded -</b> {user.mention()}",
                ),
            )

    final_song_path = final_song_path[0]
    thumb_path = thumb_path[0]

    if not playlist:
        try:
            song = await reply.edit_media(
                InputMediaAudio(
                    media=final_song_path,
                    thumb=thumb_path,
                    caption=caption,
                    duration=info["duration"],
                    performer=artist,
                    title=info["title"],
                )
            )
        except:
            return await reply.edit_media(
                InputMediaPhoto(
                    media=choice(ICONS),
                    caption=f"<b>{info['title']} Not Uploaded -</b> {user.mention()}",
                ),
            )

        song_upload_finish_time = get_readable_time(time() - song_upload_start_time)
        await asyncio.sleep(3)
        await song.reply_photo(
            photo=thumb_path,
            quote=True,
            caption=SONG_UPLOADED.format(
                song=info["title"], time=song_upload_finish_time, mention=user.mention()
            ),
        )

    else:
        try:
            song = await bot.send_audio(
                chat_id=reply.chat.id,
                audio=final_song_path,
                thumb=thumb_path,
                caption=caption,
                duration=info["duration"],
                performer=artist,
                title=info["title"],
            )
        except:
            return await bot.send_photo(
                chat_id=reply.chat.id,
                photo=choice(ICONS),
                caption=f"<b>{info['title']} Not Uploaded -</b> {user.mention()}",
            )

    dumped_song = await song.copy(
        chat_id=TeleConf.DUMP_CHANNEL,
        caption=caption,
    )

    await save_song_to_db(
        _id=info["id"],
        title=dumped_song.audio.title,
        artist=artist,
        msg_id=dumped_song.id,
        file_id=dumped_song.audio.file_id,
    )

    await bot.send_message(
        chat_id=TeleConf.LOG_CHANNEL,
        text=LOG_CHANNEL_MESSAGE.format(
            requested_by=user.mention(),
            song_name=info["title"],
            song_url=info["url"],
        ),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Song",
                        url=dumped_song.link,
                    )
                ]
            ]
        ),
    )

    os.remove(final_song_path)
    os.remove(thumb_path)
