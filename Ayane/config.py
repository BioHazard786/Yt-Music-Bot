from os import getenv
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env")
except:
    pass

botStartTime = time()


class TeleConf(object):
    BOT_TOKEN = getenv("BOT_TOKEN")
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    DUMP_CHANNEL = int(getenv("DUMP_CHANNEL"))


class MongoConf(object):
    MONGODB = getenv("MONGODB")
    DB_NAME = getenv("DB_NAME", "MusicDump")


REGEX_PT = r"(youtu.*be.*)\/(watch\?v=|embed\/|v|shorts|)(.*?((?=[&#?])|$))"
YT_THUMB_LINK = "https://i.ytimg.com/vi/{id}/mqdefault.jpg"
CAPTION = """
<b>Title</b> - <code>{title}</code>
<b>Artist</b> - <code>{artist}</code>
"""
STATUS = """
<b>➜ Title : </b><code>{title}</code>
<b>➜ Status : </b><code>{status}</code>
"""
PLAYLIST_UPLOADED = """
<b>➜ Status : </b><code>Your Playlist has been uploaded</code>
<b>➜ Total : </b><code>{song_num} Songs</code>
"""


HELP = f"""
/start: Check bot is alive or not
/stats: Show stats of the machine where the bot is hosted in.
/yt [yt_url]: Download song and dump it in channel
/help: To get this message
"""
ICONS = [
    "https://telegra.ph//file/451a9169cb4bca927080f.jpg",
    "https://telegra.ph//file/9fc8c8de06567f8ae2c2b.jpg",
    "https://telegra.ph//file/c529f35aacc3d2abc8506.jpg",
    "https://telegra.ph//file/510f122c639b622ff58d5.jpg",
    "https://telegra.ph//file/dd4c7a696ad93f61b8237.jpg",
    "https://telegra.ph//file/3dd35884409726bb73b36.jpg",
    "https://telegra.ph//file/8eb078168134871566d30.jpg",
    "https://telegra.ph//file/8d1d4b4a1ed2de4830273.jpg",
    "https://telegra.ph//file/1d28bcea826cc2a2c9799.jpg",
    "https://telegra.ph//file/89bac63888fedc062ccf9.jpg",
    "https://telegra.ph//file/e130508fd1c5a7afbce1d.jpg",
    "https://telegra.ph//file/78c87763cb140992f5ad6.jpg",
    "https://telegra.ph//file/dc92d039fa693acf5d979.jpg",
    "https://telegra.ph//file/e5cf0a4c1ce9e2c309bfe.jpg",
    "https://telegra.ph//file/50392bef6764d8b38b0bf.jpg",
    "https://telegra.ph//file/9206d428a468856bf1e0d.jpg",
    "https://telegra.ph//file/9d6efcb7813d9643067a7.jpg",
    "https://telegra.ph//file/f1a3d6b5a7f7f4ca36ee2.jpg",
    "https://telegra.ph//file/f07947ec8ee7c8560e19e.jpg",
    "https://telegra.ph//file/6660dc2786d6d4788d187.jpg",
    "https://telegra.ph//file/061fd49c54a12bb67e8f9.jpg",
    "https://telegra.ph//file/c1cbb94f2494d1aa528a3.jpg",
    "https://telegra.ph//file/0861d0d95232c6ff6adcd.jpg",
    "https://telegra.ph//file/1f6420b86cc6a4fc877c0.jpg",
    "https://telegra.ph//file/a78a305f1267b00f22ed4.jpg",
    "https://telegra.ph//file/73da3b58b9ce339670474.jpg",
    "https://telegra.ph//file/7a49738026138a2c062d9.jpg",
    "https://telegra.ph//file/fbe0918db37e0f48f30ba.jpg",
    "https://telegra.ph//file/6b07361706ff748816601.jpg",
    "https://telegra.ph//file/a8ec9b2c6db0f9bd6b3a8.jpg",
    "https://telegra.ph//file/7288b5da0fb688414deef.jpg",
    "https://telegra.ph//file/53a816b088124d3c66bc5.jpg",
    "https://telegra.ph//file/6ac56221904580d5d3441.jpg",
    "https://telegra.ph//file/f83b2d99b76e0ac35887d.jpg",
    "https://telegra.ph//file/390e16dcc796cfeb83577.jpg",
    "https://telegra.ph//file/4afbcbaba868f54e7a978.jpg",
    "https://telegra.ph//file/0b6fb808a8e24dae9ec1c.jpg",
    "https://telegra.ph//file/9e2d0a0af022d5ce1f29e.jpg",
    "https://telegra.ph//file/3411143bae8a8172af7e5.jpg",
    "https://telegra.ph//file/82a86dfb865384f3a7605.jpg",
    "https://telegra.ph//file/1649a05bfac2fe427c899.jpg",
    "https://telegra.ph//file/641f50719aa46c861b03b.jpg",
    "https://telegra.ph//file/195692b21de0a08c98e67.jpg",
    "https://telegra.ph//file/8893b4eafc1482fa1a9cc.jpg",
    "https://telegra.ph//file/dc3a6a9d4515bcba92738.jpg",
    "https://telegra.ph//file/3b67fbb27ec76733300d2.jpg",
    "https://telegra.ph//file/68b61bb9247d97e790a18.jpg",
    "https://telegra.ph//file/671337718cd6890dc6fc0.jpg",
    "https://telegra.ph//file/e3727d2204d61c5dde803.jpg",
    "https://telegra.ph//file/1f181a8a26415255079d7.jpg",
    "https://telegra.ph//file/7d74a6ffc20bb32c5965f.jpg",
    "https://telegra.ph//file/df934bd669d3fdce27c47.jpg",
    "https://telegra.ph//file/123c52599b60144a59a9c.jpg",
    "https://telegra.ph//file/7812a61812f1d21e87899.jpg",
    "https://telegra.ph//file/59a4a4e80675ef245772f.jpg",
    "https://telegra.ph//file/8f060e468a55b19d8b7f6.jpg",
    "https://telegra.ph//file/4b84bc8651f1712112755.jpg",
    "https://telegra.ph//file/65e0fe1f2d1bb2a3064ce.jpg",
    "https://telegra.ph//file/40a291550d830b600a052.jpg",
    "https://telegra.ph//file/f62474ef87f87c5f9c098.jpg",
    "https://telegra.ph//file/72f2a02a64218c0d04537.jpg",
    "https://telegra.ph//file/4133a958b124a519c6020.jpg",
    "https://telegra.ph//file/9abf5c4c8d35472536e0a.jpg",
    "https://telegra.ph//file/a846f83e78b5d84b6215f.jpg",
    "https://telegra.ph//file/6fd2b95a54bed69de5add.jpg",
    "https://telegra.ph//file/437f905fe9a8988d07f41.jpg",
    "https://telegra.ph//file/e1ebebf52ce8b2a749707.jpg",
    "https://telegra.ph//file/b877ee2028ebe45a41493.jpg",
    "https://telegra.ph//file/c7af99a1e5809772cafb2.jpg",
    "https://telegra.ph//file/54c502e96ce8505ae876e.jpg",
    "https://telegra.ph//file/d4174f0cdfb15f76f14b5.jpg",
    "https://telegra.ph//file/9859e28b47d7d7734b8f5.jpg",
    "https://telegra.ph//file/a396fb2e8771c5c4360a9.jpg",
    "https://telegra.ph//file/ff63898dcb9f74cdac179.jpg",
    "https://telegra.ph//file/84f57c7b814c33474231c.jpg",
    "https://telegra.ph//file/08a464bed5c135c212fb8.jpg",
    "https://telegra.ph//file/7282ef0777321f6e72a58.jpg",
    "https://telegra.ph//file/470058f042fba90717404.jpg",
    "https://telegra.ph//file/f1e1e9d31bc2a4d1e6798.jpg",
    "https://telegra.ph//file/15719217d3ad505f1346b.jpg",
    "https://telegra.ph//file/9c5aba59a85f1de92bd59.jpg",
    "https://telegra.ph//file/dde366c5b307679b25b1f.jpg",
    "https://telegra.ph//file/25d6e249f017b5c2a25e6.jpg",
    "https://telegra.ph//file/f042b7d173a57ec750082.jpg",
    "https://telegra.ph//file/7e7c20474b2f8601dce8f.jpg",
    "https://telegra.ph//file/fbb6e28a3b311dbb7df3b.jpg",
    "https://telegra.ph//file/79862f5ec9525f367f698.jpg",
    "https://telegra.ph//file/ca1d306c80e0ac0d524e5.jpg",
    "https://telegra.ph//file/04d7c9df026c3c2b75cfe.jpg",
    "https://telegra.ph//file/5da622b0a0b356cea1a4c.jpg",
]
