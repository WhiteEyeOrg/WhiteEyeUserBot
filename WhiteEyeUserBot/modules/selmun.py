# Credit To @Kraken_The_BadASS . Keep credit if you are going to edit it.


import asyncio

from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.utils import WhiteEye_on_cmd


@WhiteEye.on(WhiteEye_on_cmd(pattern="selmun ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("πSelmun Bhoi wants to go on a Rideπ¨")
        await asyncio.sleep(2)
        await event.edit("πππ\nπππ\nπππ\nπππ")
        await asyncio.sleep(1)
        await event.edit("πππ\nπππ\nπππ\nπππ")
        await asyncio.sleep(1)
        await event.edit("πππ\nπππ\nπππ\nπππ")
        await asyncio.sleep(1)
        await event.edit("πππ\nπππ\nπππ\nπππ")
        await asyncio.sleep(1)
        await event.edit(
            "πSelmun Bhoi Iz feeling Hungryπ \nAlso he iz big fan of Bear Grillsπ€«π¬"
        )
        await asyncio.sleep(2.4)
        await event.edit("A Blackbuck iz spootedπ¦")
        await asyncio.sleep(1.9)
        await event.edit("π¨Bhoi takes Out his Crossbow?πΉ")
        await asyncio.sleep(1.8)
        await event.edit("Rest Iz Mysteryπ€« \nThat blackbuckπ¦ was never found againπ¨")
        await asyncio.sleep(2)
        await event.edit("Bhoi Iz going back to his home")
        await asyncio.sleep(2)
        await event.edit("I don't know howπ¨ \nBut he iz no more hungryπ€«π¦")
        await asyncio.sleep(2)
        await event.edit("He iz heading back to his home")
        await asyncio.sleep(2)
        await event.edit("πππ\nπππ\nπππ\nπππ")
        await asyncio.sleep(1)
        await event.edit("πππ\nπππ\nπππ\nπππ")
        await asyncio.sleep(1)
        await event.edit("πππ\nπππ\nπππ\nπππ")
        await asyncio.sleep(1)
        await event.edit("πππ\nπππ\nπππ\nπππ")
        await asyncio.sleep(1)
        await event.edit("Selmun Bhoi reached homeπ \nAnd went to sleepπ΄π")
        await asyncio.sleep(2)
        await event.edit(
            "Next Day \n2 Poor people \nWho used to sleep on foothpath \nWere reported dedβ°οΈπ₯"
        )
        await asyncio.sleep(2.5)
        await event.edit(
            "Selmun bhoi drove his car from that road last nightπ \nRest is a mystery......."
        )
        await asyncio.sleep(2.2)
        await event.edit("**R**")
        await asyncio.sleep(0.2)
        await event.edit("**R** \n**I**")
        await asyncio.sleep(0.2)
        await event.edit("**R** \n**I** \n**P**")
        await asyncio.sleep(0.2)
        await event.edit("**β°οΈπ¦RIPπ¦β°οΈ**")


CMD_HELP.update(
    {
        "selmun": "Selmun\
\n\nSyntax : .selmun\
\nUsage : Try YourSelf"
    }
)
