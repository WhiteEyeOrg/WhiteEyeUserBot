import time
from datetime import datetime

from WhiteEyeUserBot import CMD_HELP, Lastupdate
from WhiteEyeUserBot.utils import WhiteEye_on_cmd, edit_or_reply, sudo_cmd


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@WhiteEye.on(WhiteEye_on_cmd(pattern="ping$"))
@WhiteEye.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    starkislub = await edit_or_reply(event, "`Pong !`")
    if event.fwd_from:
        return
    hmm = await bot.get_me()
    rip = f"[{hmm.first_name}](tg://user?id={hmm.id})"
    if not hmm.username:
        hmm.username = hmm.id
    bothmm = await tgbot.get_me()
    botrip = f"[{bothmm.first_name}](tg://user?id={bothmm.id})"
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    await starkislub.edit(
        f"**█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄**\n➲ `{ms}` \n➲ `{uptime}` \n➲ {rip} \n➲ {botrip}"
    )


CMD_HELP.update(
    {
        "ping": "Ping**\
\n\n**Syntax : .ping\
\nUsage : Shows If The Bot Is Working Or Not"
    }
)
