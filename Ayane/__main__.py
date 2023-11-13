from Ayane import loop, bot
import os
from time import time
from Ayane.helpers.utils import get_readable_time


async def restart_notification():
    if os.path.isfile(".restartmsg"):
        with open(".restartmsg") as f:
            restart_started, chat_id, msg_id = map(float, f)
        current_time = get_readable_time(time() - restart_started)
        await bot.edit_message_text(
            chat_id=int(chat_id),
            message_id=int(msg_id),
            text=f"<b>‣ Task  :  </b><code>Restarted Successfully!</code>\n\n<b>‣ Time Taken  :</b><code>  {current_time}</code>",
        )
        os.remove(".restartmsg")
    else:
        return


loop.run_until_complete(restart_notification())
loop.run_forever()
