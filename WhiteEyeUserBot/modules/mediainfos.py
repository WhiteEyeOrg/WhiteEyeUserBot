# Originally By @DeletedUser420
# Ported - @StarkxD

import asyncio
import os
import shlex
from typing import Tuple

from telegraph import Telegraph

from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.Configs import Config
from WhiteEyeUserBot.utils import WhiteEye_on_cmd

telegraph = Telegraph()
tgnoob = telegraph.create_account(short_name="WhiteEye 🇮🇳")


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """run command in terminal"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


@WhiteEye.on(WhiteEye_on_cmd(pattern="mediainfo$"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if reply_message is None:
        await event.edit("Reply To a Media.")
    await event.edit("`Processing...`")
    file_path = await borg.download_media(reply_message, Config.TMP_DOWNLOAD_DIRECTORY)
    out, err, ret, pid = await runcmd(f"mediainfo '{file_path}'")
    media_info = f"""
    <code>           
    {out}                  
    </code>"""
    title_of_page = "Media Info 🎬"
    response = telegraph.create_page(title_of_page, html_content=media_info)
    km = response["path"]
    await event.edit(f"`This MediaInfo Can Be Found` [Here](https://telegra.ph/{km})")
    if os.path.exists(file_path):
        os.remove(file_path)


CMD_HELP.update(
    {
        "mediainfos": "**MediaInfos**\
\n\n**Syntax : **`.MediaInfo`\
\n**Usage :** Reply To Image."
    }
)
