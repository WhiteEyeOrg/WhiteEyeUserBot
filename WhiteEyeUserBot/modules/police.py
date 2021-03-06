import asyncio

from WhiteEyeUserBot import ALIVE_NAME, CMD_HELP
from WhiteEyeUserBot.utils import WhiteEye_on_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "WhiteEyeUserbot"


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"police"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    await event.edit("Police")

    animation_chars = [
        "š“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ",
        "šµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“",
        "š“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ",
        "šµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“",
        "š“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ",
        "šµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“",
        "š“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ",
        "šµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“",
        "š“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ",
        "šµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“\nšµšµšµā¬ā¬ā¬š“š“š“",
        "š“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ\nš“š“š“ā¬ā¬ā¬šµšµšµ",
        "[WhiteEye](https://www.github.com/mrdayamzaidi/WhiteEye) **Police Service Here**",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])


CMD_HELP.update(
    {
        "police": "Police\
\n\nSyntax : .police \
\nUsage : Yet Another Fun Plugin"
    }
)
