# Coded by @AbirHasan2005
# Telegram Group: http://t.me/linux_repo


import asyncio

from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.utils import WhiteEye_on_cmd


@WhiteEye.on(WhiteEye_on_cmd("inflag"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    await event.edit("Hello ")
    animation_chars = [
        "Happy Independence Day",
        "**๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง\n๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง\n๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง๐ง\nโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธ๐ฆ๐ฆ๐ฆโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธ\nโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธ๐ฆ๐ฆ๐ฆโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธ\nโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธ๐ฆ๐ฆ๐ฆโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธ\n๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ\n๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ\n๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ\n\nMade With Love ๐งก๐ค๐\n\nHappy Independence Day !!!!!**",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


CMD_HELP.update(
    {
        "indianflag": "**IndianFlag**\
\n\n**Syntax : **`.inflag`\
\n**Usage :** Downloads songs from ytmusic"
    }
)
