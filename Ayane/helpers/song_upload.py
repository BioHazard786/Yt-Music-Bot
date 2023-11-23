from .__init__ import *


async def song_upload(reply, info, user, song_path, playlist=False):
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

    final_song_path = os.path.join(song_path, f"{info['title']}.mp3")
    thumb_path = os.path.join(song_path, f"{info['title']}.jpg")

    if not os.path.isfile(final_song_path):
        return

    if not playlist:
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

        await asyncio.sleep(3)
        await song.reply_photo(
            photo=thumb_path,
            quote=True,
            caption=f"<b>Your Song has been Uploaded -</b> {user.mention()}",
        )

    else:
        song = await bot.send_audio(
            chat_id=reply.chat.id,
            audio=final_song_path,
            thumb=thumb_path,
            caption=caption,
            duration=info["duration"],
            performer=artist,
            title=info["title"],
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

    os.remove(final_song_path)
    os.remove(thumb_path)
