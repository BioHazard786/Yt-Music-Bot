from .__init__ import *
from Ayane.helpers.thumbnail_downloader import dl_thumbnail_image


async def song_upload(message, reply, info, song_path):
    executor = ThreadPoolExecutor(1)
    artist = (
        info.get("artist")
        if info.get("artist")
        else info.get("uploader").replace(" - Topic", "")
    )
    caption = CAPTION.format(
        title=info["title"],
        artist=artist,
    )

    thumbnail_path = await loop.run_in_executor(
        executor,
        lambda: dl_thumbnail_image(
            YT_THUMB_LINK.format(id=info["id"]), message.from_user.id
        ),
    )
    for song_file in os.listdir(song_path):
        fpath = os.path.join(song_path, song_file)
        if not song_file.endswith(".mp3"):
            os.remove(fpath)
        else:
            if thumbnail_path:
                song = await reply.edit_media(
                    InputMediaAudio(
                        media=fpath,
                        thumb=thumbnail_path,
                        caption=caption,
                        duration=info["duration"],
                        performer=artist,
                        title=info["title"],
                    )
                )
                await song.reply_photo(
                    photo=thumbnail_path,
                    quote=True,
                    caption=f"<b>Your Song has been Uploaded -</b> {message.from_user.mention()}",
                )
            else:
                song = await reply.edit_media(
                    InputMediaAudio(
                        media=fpath,
                        caption=caption
                        + f"\n\n<b>Your Song has been Uploaded -</b> {message.from_user.mention()}",
                        duration=info["duration"],
                        performer=artist,
                        title=info["title"],
                    )
                )

            print(song.audio.title, song.audio.file_name)

            dumped_song = await song.copy(
                chat_id=DUMP_CHANNEL,
                caption=caption,
            )
            await save_song_to_db(
                _id=info["id"],
                title=dumped_song.audio.title,
                msg_id=dumped_song.id,
                file_id=dumped_song.audio.file_id,
            )
            os.remove(fpath)
