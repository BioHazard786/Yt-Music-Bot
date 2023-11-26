from .__init__ import *


@bot.on_inline_query()
async def inlineSearch(client: Client, query: InlineQuery):
    results = []
    if query.query and len(query.query) > 1:
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
        async for result in initial_search_result():
            if result:
                results.append(
                    InlineQueryResultCachedAudio(
                        audio_file_id=result["file_id"],
                    )
                )
        if results:
            await query.answer(results)
