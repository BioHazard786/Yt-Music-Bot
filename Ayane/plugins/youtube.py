from .__init__ import *


@bot.on_message(command_creator("yt"))
async def ytmusicdl(app, message):
    args = message.text.split(" ")

    if len(args) == 1:
        return await message.reply("<b>Use like this : </b><code>/yt link</code>")
    elif len(args) == 2:
        url = args[-1].strip()
    else:
        return await message.reply("<b>Use like this : </b><code>/yt link</code>")

    if "playlist" in url.lower():
        return await message.reply("<b>Playlist are not supported currently :(</b>")

    reply = await message.reply_animation(
        animation="https://i.pinimg.com/originals/48/6a/a0/486aa0fa1658b7522ecd8918908ece40.gif",
        caption=f"<code>Extarcting YT Link ID...</code>",
    )

    try:
        yt_id = extract_yt_id(url)
    except:
        return await message.reply(f"<b>Link is invalid : </b><code>{url}</code>")

    await reply.edit_media(
        InputMediaAnimation(
            media="https://i.pinimg.com/originals/48/6a/a0/486aa0fa1658b7522ecd8918908ece40.gif",
            caption=f"<code>Checking Song in Database...</code>",
        )
    )

    if saved_song := await check_song(yt_id):
        await reply.delete()
        return await message.reply_cached_media(
            saved_song["file_id"],
            caption=f"<b>Your Song has been Uploaded -</b> {message.from_user.mention}",
        )

    song_path = os.path.join(os.getcwd(), f"music_{message.from_user.id}")

    await reply.edit_media(
        InputMediaAnimation(
            media="https://i.pinimg.com/originals/48/6a/a0/486aa0fa1658b7522ecd8918908ece40.gif",
            caption=f"<code>Downloading from YT...</code>",
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
        return await reply.edit_media(
            InputMediaPhoto(
                media="https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg",
                caption=f"<b>Link is invalid : </b><code>{url}</code>",
            )
        )
    try:
        await reply.edit_media(
            InputMediaAnimation(
                media="https://i.pinimg.com/originals/48/6a/a0/486aa0fa1658b7522ecd8918908ece40.gif",
                caption="<code>Download completed, Sending to telegram...</code>",
            )
        )
    except:
        pass

    await song_upload(message, reply, info, song_path)
