from motor.motor_asyncio import AsyncIOMotorClient
from Ayane.config import MongoConf


class MongoDB:
    def __init__(self, coll):
        self.coll = coll
        self.update = coll.update_one
        self.get = coll.find_one
        self.insert = coll.insert_one
        self.delete = coll.delete_one

    async def get(self, doc):
        return await self.get(doc)

    async def insert(self, doc):
        await self.insert(doc)

    async def delete(self, query):
        await self.delete(query)

    async def update(self, _id: dict, update_item: dict):
        await self.update(_id, update_item)


mongo = AsyncIOMotorClient(MongoConf.MONGODB)
DB = mongo[MongoConf.DB_NAME]
INDEX = MongoDB(DB["INDEX"])


async def save_song_to_db(_id, title, artist, msg_id, file_id):
    doc = {
        "_id": _id,
        "title": title,
        "artist": artist,
        "msg_id": msg_id,
        "file_id": file_id,
    }
    await INDEX.insert(doc)


async def check_song(_id):
    return await INDEX.get({"_id": _id})


async def song_title_matching(query: str):
    pipeline = [
        {
            "$search": {
                "index": "title_search",
                "text": {"query": query, "path": ["title", "artist"]},
            },
        },
        {"$limit": 50},
    ]
    async for doc in DB.INDEX.aggregate(pipeline):
        yield doc


async def initial_search_result():
    async for doc in DB.INDEX.find().sort("_id", -1).limit(20):
        yield doc
