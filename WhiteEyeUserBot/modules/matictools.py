#    Copyright (C) @WhiteEyeBots 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from uniborg.util import WhiteEye_on_cmd, edit_or_reply, sudo_cmd

from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.functions.matic_tool import auto_bio, auto_name, auto_pic

scheduler = AsyncIOScheduler(executors={"default": AsyncIOExecutor()})


@WhiteEye.on(WhiteEye_on_cmd(pattern="autoname(?: |$)(.*)"))
@WhiteEye.on(sudo_cmd(pattern="autoname(?: |$)(.*)", allow_sudo=True))
async def autoname(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "`Started AutoName Your Name Will Be Changed Every 1 Min, According To TimeZone Given. To Terminate This Process Use .stop Cmd`",
    )
    scheduler.add_job(
        auto_name,
        "interval",
        args=[event.pattern_match.group(1)],
        minutes=1,
        id="autoname",
    )


@WhiteEye.on(WhiteEye_on_cmd(pattern="autopic$"))
@WhiteEye.on(sudo_cmd(pattern="autopic$", allow_sudo=True))
async def autopic(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "`Started AutoPic Your Name Will Be Changed Every 1 Min, According To TimeZone Given. To Terminate This Process Use .stop Cmd`",
    )
    scheduler.add_job(auto_pic, "interval", minutes=1, id="autopic")


@WhiteEye.on(WhiteEye_on_cmd(pattern="autobio(?: |$)(.*)"))
@WhiteEye.on(sudo_cmd(pattern="autobio(?: |$)(.*)", allow_sudo=True))
async def autobio(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "`Started AutoBio Your Bio Will Be Changed Every 1 Min, According To TimeZone Given. To Terminate This Process Use .stop Cmd`",
    )
    scheduler.add_job(
        auto_bio,
        "interval",
        args=[event.pattern_match.group(1)],
        minutes=1,
        id="autobio",
    )


@WhiteEye.on(WhiteEye_on_cmd(pattern="stop$"))
@WhiteEye.on(sudo_cmd(pattern="stop$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    sed = await edit_or_reply(event, "`Checking Recived Input :)`")
    try:
        scheduler.remove_all_jobs()
    except:
        await event.edit("`Are You Fking Insane?`")
        return
    logger.info("Matic Tools Has Been Terminated")
    await sed.edit("`All Matic Tools Has Been Terminated`")


scheduler.start()

CMD_HELP.update(
    {
        "autoname": "**Autoname**\
\n\n**Syntax : **`.autoname`\
\n**Usage :** Change your Name With Time"
    }
)
