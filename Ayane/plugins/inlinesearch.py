from .__init__ import *


@bot.on_inline_query()
async def inlineSearch(client: Client, query: InlineQuery):
    results = []
    if query.query and len(query.query) > 1:
        async for result in song_title_matching(query.query):
            if result:
                results.append(
                    InlineQueryResultCachedAudio(
                        audio_file_id=result["file_id"],
                    )
                )

        if results:
            await query.answer(results)

    else:
        async for result in initial_search_result():
            if result:
                results.append(
                    InlineQueryResultCachedAudio(
                        audio_file_id=result["file_id"],
                    )
                )
        if results:
            await query.answer(results)
