from asyncio import wait

from WhiteEyeUserBot.utils import WhiteEye_on_cmd


@WhiteEye.on(WhiteEye_on_cmd("repeat ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    message = event.text[10:]
    count = int(event.text[8:10])
    repmessage = message * count
    await wait([event.respond(repmessage) for i in range(count)])
    await event.delete()
