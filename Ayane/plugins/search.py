from .__init__ import *


@bot.on_message(command_creator("search"))
async def search(app: Client, message: Message):
    args = message.text.split(" ", maxsplit=1)

    if len(args) == 1:
        return await message.reply("<b>Use like this : </b><code>/search query</code>")
    elif len(args) == 2:
        query = args[-1].strip()
    else:
        return await message.reply("<b>Use like this : </b><code>/search query</code>")

    await search_helper(query, message)


@bot.on_message(
    filters.regex(pattern=r"^\w+\s?")
    & ~filters.regex(pattern=REGEX_PT)
    & ~filters.regex(pattern=REGEX_PT_SPOTIFY)
    & filters.private
)
async def ytmusicdl(app, message):
    query = message.text.strip()
    await search_helper(query, message)


async def search_helper(query: str, message: Message):
    buttons = []
    reply = await message.reply_photo(
        photo=choice(ICONS),
        caption=STATUS.format(title=query, status="Searching...🔎"),
    )
    search_results = await loop.run_in_executor(
        ThreadPoolExecutor(1),
        lambda: YT_MUSIC.search(query=query, filter="songs"),
    )
    if len(search_results) == 0:
        return await reply.edit_media(
            InputMediaPhoto(
                media=choice(ICONS), caption=f"➜ 𝗡𝗼 𝗥𝗲𝘀𝘂𝗹𝘁𝘀 𝗙𝗼𝘂𝗻𝗱 𝗳𝗼𝗿 - <i>{query}</i>"
            )
        )

    for result in search_results:
        artist = ", ".join(list(map(lambda a: a["name"], result["artists"])))
        callback_data = (
            f"d|{message.from_user.id}|{result['title']}|{result['videoId']}"
        )
        if len(callback_data) > 64:
            callback_data = f"d|{message.from_user.id}|Song ({result['videoId']})|{result['videoId']}"
        buttons.append(
            [
                InlineKeyboardButton(
                    text=f"{result['title']} - {artist}",
                    callback_data=callback_data,
                )
            ]
        )

    await reply.edit_media(
        InputMediaPhoto(
            media=choice(ICONS), caption=f"➜ 𝗛𝗲𝗿𝗲 𝗮𝗿𝗲 𝘀𝗼𝗺𝗲 𝗿𝗲𝘀𝘂𝗹𝘁𝘀 - <i>{query}</i>"
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
