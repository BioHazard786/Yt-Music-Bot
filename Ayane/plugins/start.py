from .__init__ import *


@bot.on_message(command_creator("start"))
async def start(app: Client, message: Message):
    await bot.send_message(message.chat.id, "<code>Alive :)</code>")
