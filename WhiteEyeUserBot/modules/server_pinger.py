import requests
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from WhiteEyeUserBot.modules.sql_helper import server_pinger_sql as whiteeyeping
from WhiteEyeUserBot.utils import WhiteEye_on_cmd

if Config.PING_SERVERS:

    @WhiteEye.on(WhiteEye_on_cmd(pattern="aping"))
    async def _(event):
        if event.fwd_from:
            return
        await event.edit("`Processing..`")
        url = event.text.split(" ", maxsplit=1)[1]
        if whiteeyeping.is_ping_indb(str(url)):
            await event.edit("**Server Already Found In DataBase !**")
            return
        whiteeyeping.add_ping(url)
        await event.edit(f"**URL :** `{url}` **Sucessfully Added To Db**")

    @WhiteEye.on(WhiteEye_on_cmd(pattern="rping"))
    async def _(event):
        if event.fwd_from:
            return
        await event.edit("`Processing..`")
        url = event.text.split(" ", maxsplit=1)[1]
        if not whiteeyeping.is_ping_indb(str(url)):
            await event.edit("**Server Not Found In Db !**")
            return
        whiteeyeping.rmping(url)
        await event.edit(f"**URL :** `{url}` **Sucessfully Removed From DataBase**")

    async def ping_servers():
        hmm_p = 0
        url_s = whiteeyeping.get_all_url()
        header_s = {"User-Agent": "Server Pinged By @WhiteEyeDevs"}
        if len(url_s) == 0:
            return
        for i in url_s:
            try:
                ws = requests.get(url=i.url, headers=header_s).status_code
                logger.info(f"Pinged {i.url} // Status Code Recived : {ws}")
            except:
                hmm_p += 1
        success_l = len(url_s) - hmm_p
        logger.info(f"Sucessfully Pinged {success_l} Urls Out Of {len(url_s)}")

    scheduler = AsyncIOScheduler(
        executors={
            "threadpool": ThreadPoolExecutor(max_workers=9),
            "processpool": ProcessPoolExecutor(max_workers=3),
        }
    )
    scheduler.add_job(ping_servers, "interval", minutes=60, executor="threadpool")
    scheduler.start()
