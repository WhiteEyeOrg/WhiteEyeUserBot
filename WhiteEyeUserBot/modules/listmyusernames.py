# For @UniBorg
# (c) Shrimadhav U K

from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from uniborg.util import WhiteEye_on_cmd

from WhiteEyeUserBot import CMD_HELP


@WhiteEye.on(WhiteEye_on_cmd("listmyusernames"))
async def mine(event):
    """For .reserved command, get a list of your reserved usernames."""
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    if event.fwd_from:
        return
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)


CMD_HELP.update(
    {
        "listmyusernames": "**Listmyusernames**\
\n\n**Syntax : **`.listmyusernames`\
\n**Usage :** it lists all your usernames you are holding"
    }
)
