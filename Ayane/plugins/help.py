from .__init__ import *


@bot.on_message(command_creator("help"))
async def help(app: Client, message: Message):
    await message.reply(HELP)
