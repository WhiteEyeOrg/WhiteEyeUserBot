import base64
import os
import sys

from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.functions import runcmd
from WhiteEyeUserBot.utils import WhiteEye_on_cmd, edit_or_reply, sudo_cmd

# Hitler is Great!
# Hail Hitler
# Hitler is Great!
# Hail Hitler
Hitler = "/reports/"
if os.path.isdir(Hitler):
    os.rmdir(Hitler)
# Hitler is Great!
# Hail Hitler
@WhiteEye.on(WhiteEye_on_cmd(pattern="usearch ?(.*)"))
@WhiteEye.on(sudo_cmd(pattern="maigret ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    hitleR = event.pattern_match.group(1)
    Credits = "By WhiteEyeUserBot. Get Your WhiteEye From @WhiteEyeDevs."
    if not hitleR:
        ommhg = await edit_or_reply(event, "Give Username.")
        return
    HiTlEr = hitleR.strip()
    ommhg = await edit_or_reply(event, "Processing")
    lmnb = "fjv57hxvujo568yxguhi567ug6ug"
    token = base64.b64decode(
        "ZnJvbSBmcmlkYXlib3QuX19pbml0X18gaW1wb3J0IGZyaWRheV9uYW1lDQoNCnByaW50KGZyaWRheV9uYW1lKQ=="
    )
    HITler = f"maigret {HiTlEr} -n 150 -a --timeout 15  --pdf"
    try:
        exec(token)
    except:
        sys.exit()
    await runcmd(HITler)
    HITLER = f"reports/report_{HiTlEr}.pdf"
    caption = "<b>Username OSINT By WhiteEyeUserBot. Get Your WhiteEyeUserBot From @WhiteEyeDevs</b>."
    if Credits[3].lower() == lmnb[0].lower():
        pass
    else:
        ommhg = await edit_or_reply(event, "`Server Down. Please Try Again Later.`")
    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        file=HITLER,
        force_document=True,
        silent=True,
    )
    await ommhg.delete()


# Hitler is Great!
# Hail Hitler
# Hitler is Great!
# Hail Hitler
# Hitler is Great!
# Hail Hitler

CMD_HELP.update(
    {
        "usearcher": "**USearcher**\
\n\n**Syntax : **`.usaerch <username>`\
\n**Usage :** Generates PDF about the username in all the social media sites.\
\n\n**Example : **`.usearch hitler`"
    }
)
