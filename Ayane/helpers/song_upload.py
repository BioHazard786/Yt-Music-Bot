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
        if not playlist:
            if not isinstance(reply, CallbackQuery):
                return await reply.edit_media(
                    InputMediaPhoto(
                        media=choice(ICONS),
                        caption=f"{info['title']} 𝗡𝗼𝘁 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 - {user.mention()}",
                    ),
                )
            else:
                return await reply.edit_message_media(
                    InputMediaPhoto(
                        media=choice(ICONS),
                        caption=f"{info['title']} 𝗡𝗼𝘁 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 - {user.mention()}",
                    ),
                )

        else:
            return await bot.send_photo(
                chat_id=reply.chat.id,
                photo=choice(ICONS),
                caption=f"{info['title']} 𝗡𝗼𝘁 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 - {user.mention()}",
            )

    final_song_path = final_song_path[0]
    thumb_path = thumb_path[0]

    if not playlist:
        try:
            if not isinstance(reply, CallbackQuery):
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
            else:
                song = await reply.edit_message_media(
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
            if not isinstance(reply, CallbackQuery):
                return await reply.edit_media(
                    InputMediaPhoto(
                        media=choice(ICONS),
                        caption=f"{info['title']} 𝗡𝗼𝘁 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 - {user.mention()}",
                    ),
                )
            else:
                return await reply.edit_message_media(
                    InputMediaPhoto(
                        media=choice(ICONS),
                        caption=f"{info['title']} 𝗡𝗼𝘁 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 - {user.mention()}",
                    ),
                )

        song_upload_finish_time = get_readable_time(time() - song_upload_start_time)
        await asyncio.sleep(3)
        if not isinstance(reply, CallbackQuery):
            await song.reply_photo(
                photo=thumb_path,
                quote=True,
                caption=SONG_UPLOADED.format(
                    song=info["title"],
                    time=song_upload_finish_time,
                    mention=user.mention,
                ),
            )
        else:
            await reply.edit_message_caption(
                caption=INLINE_SONG_UPLOADED.format(
                    title=info["title"],
                    artist=artist,
                    time=song_upload_finish_time,
                    mention=user.mention,
                )
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
                caption=f"{info['title']} 𝗡𝗼𝘁 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 - {user.mention()}",
            )

    if not isinstance(reply, CallbackQuery):
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
    else:
        dumped_song = await bot.send_audio(
            chat_id=TeleConf.DUMP_CHANNEL,
            audio=final_song_path,
            thumb=thumb_path,
            caption=caption,
            duration=info["duration"],
            performer=artist,
            title=info["title"],
        )
        await save_song_to_db(
            _id=info["id"],
            title=dumped_song.audio.title,
            artist=artist,
            msg_id=dumped_song.id,
            file_id=dumped_song.audio.file_id,
        )

    if not playlist:
        await bot.send_message(
            chat_id=TeleConf.LOG_CHANNEL,
            text=LOG_CHANNEL_MESSAGE.format(
                requested_by=user.mention,
                song_name=info["title"],
                song_url=info["original_url"],
                time_taken=song_upload_finish_time,
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="𝗦𝗼𝗻𝗴",
                            url=dumped_song.link,
                        )
                    ]
                ]
            ),
        )

    os.remove(final_song_path)
    os.remove(thumb_path)
