import asyncio
from datetime import datetime

from WhiteEyeUserBot.utils import WhiteEye_on_cmd, sudo_cmd

WhiteEyethumb = "./resources/20201201_001148.jpg"


@WhiteEye.on(WhiteEye_on_cmd(pattern="send ?(.*)"))
@WhiteEye.on(sudo_cmd(pattern="send ?(.*)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    the_plugin_file = "./WhiteEyeUserBot/modules/{}.py".format(input_str)
    end = datetime.now()
    (end - start).seconds
    men = f"Plugin Name - {input_str}.py \nUploaded By WhiteEye"
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        thumb=WhiteEyethumb,
        caption=men,
        force_document=True,
        allow_cache=False,
        reply_to=message_id,
    )
    await asyncio.sleep(5)
    await event.delete()
