import pyjokes

from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.utils import WhiteEye_on_cmd


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"cjoke"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(pyjokes.get_joke(category="all"))


CMD_HELP.update(
    {
        "coders_joke": "**Coders Joke**\
\n\n**Syntax : **`.cjoke`\
\n**Usage :** Get programmer jokes."
    }
)
