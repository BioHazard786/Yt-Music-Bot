from .__init__ import *
from Ayane.plugins.youtube import yt_music_dl_helper


@bot.on_inline_query()
async def inlineSearch(client: Client, query: InlineQuery):
    results = []
    if query.query and len(query.query) > 1:
        if ".online" not in query.query:
            offset = int(query.offset or 0)
            async for result, next_offset in song_title_matching(query.query, offset):
                if result:
                    results.append(
                        InlineQueryResultCachedAudio(
                            audio_file_id=result["file_id"],
                        )
                    )

            if results:
                await query.answer(results, next_offset=str(next_offset))
        else:
            args = query.query.strip().split(" ", maxsplit=1)

            if len(args) > 1:
                song_name = args[-1]
                search_results = await loop.run_in_executor(
                    ThreadPoolExecutor(1),
                    lambda: YT_MUSIC.search(query=song_name, filter="songs"),
                )
                for result in search_results:
                    buttons = [
                        InlineKeyboardButton(
                            text="📥 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱", callback_data=f"d|{query.from_user.id}|{result['videoId']}"
                        ),
                        InlineKeyboardButton(
                            text="🔎 𝗦𝗲𝗮𝗿𝗰𝗵 𝗔𝗴𝗮𝗶𝗻", switch_inline_query_current_chat=".online "
                        ),
                    ]
                    markup = InlineKeyboardMarkup([buttons])
                    if result:
                        artist = ", ".join(
                            list(map(lambda a: a["name"], result["artists"]))
                        )
                        duration = get_readable_time(
                            result["duration_seconds"])
                        results.append(
                            InlineQueryResultPhoto(
                                photo_url=YT_THUMB_LINK.format(
                                    id=result["videoId"]),
                                title=result["title"],
                                description=f"{artist} | {duration}",
                                reply_markup=markup,
                                caption=SEARCH_RESULT.format(
                                    title=result["title"],
                                    artist=artist,
                                    duration=duration,
                                ),
                            ),
                        )
                if results:
                    await query.answer(results)
            else:
                await query.answer(
                    [
                        InlineQueryResultArticle(
                            title="Give a Name to Search",
                            description="Download Songs without leaving Telegram",
                            thumb_url=choice(ICONS),
                            input_message_content=InputTextMessageContent(
                                message_text="𝗖𝗹𝗶𝗰𝗸 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻 𝗯𝗲𝗹𝗼𝘄 𝘁𝗼 𝘀𝗲𝗮𝗿𝗰𝗵 𝗳𝗼𝗿 𝘀𝗼𝗻𝗴𝘀 𝘃𝗶𝗮 𝗶𝗻𝗹𝗶𝗻𝗲.",
                            ),
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                                text="𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗿𝗲", switch_inline_query_current_chat=".online Starboy"
                            )]])
                        )
                    ]
                )

    else:
        results.append(
            InlineQueryResultArticle(
                title="Search for Songs Online",
                description="Download Songs without leaving Telegram",
                thumb_url=choice(ICONS),
                input_message_content=InputTextMessageContent(
                    message_text="𝗖𝗹𝗶𝗰𝗸 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻 𝗯𝗲𝗹𝗼𝘄 𝘁𝗼 𝘀𝗲𝗮𝗿𝗰𝗵 𝗳𝗼𝗿 𝘀𝗼𝗻𝗴𝘀 𝘃𝗶𝗮 𝗶𝗻𝗹𝗶𝗻𝗲.",
                ),
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                    text="𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗿𝗲", switch_inline_query_current_chat=".online Starboy"
                )]])
            )
        )
        async for result in initial_search_result():
            if result:
                results.append(
                    InlineQueryResultCachedAudio(
                        audio_file_id=result["file_id"],
                    )
                )
        if results:
            await query.answer(results)


@bot.on_callback_query(filters.create(lambda _, __, query: query.data.startswith("d|")))
async def song_download(client: Client, query: CallbackQuery):
    _, user_id, video_id = query.data.split('|')
    url = f"https://youtu.be/{video_id}"
    if query.from_user.id != int(user_id):
        return await query.answer("Not Allowed...❎")
    else:
        await query.answer("Downloading...📥")
        await yt_music_dl_helper(url, query, query.from_user)
