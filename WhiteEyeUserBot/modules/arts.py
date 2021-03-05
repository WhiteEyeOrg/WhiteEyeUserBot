from WhiteEyeUserBot import ALIVE_NAME, CMD_HELP
from WhiteEyeUserBot.utils import WhiteEye_on_cmd

n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

# @command(outgoing=True, pattern="^.ded$")
@WhiteEye.on(WhiteEye_on_cmd(pattern=r"ded"))
async def bluedevilded(ded):
    if event.fwd_from:
        return
    await ded.edit(
        n + " ==             |\n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n"
    )


M = (
    "▄███████▄\n"
    "█▄█████▄█\n"
    "█▼▼▼▼▼█\n"
    "██________█▌\n"
    "█▲▲▲▲▲█\n"
    "█████████\n"
    "_████\n"
)
P = (
    "┈┈┏━╮╭━┓┈╭━━━━╮\n"
    "┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
    "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
    "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
)
K = "_/﹋\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉ - -\n" "_/﹋\_\n"
G = (
    "........___________________\n"
    "....../ `-___________--_____|] - - - - - -\n"
    " - - ░ ▒▓▓█D \n"
    "...../==o;;;;;;;;______.:/\n"
    ".....), -.(_(__) /\n"
    "....// (..) ), —\n"
    "...//___//\n"
)
D = (
    "╥━━━━━━━━╭━━╮━━┳\n"
    "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
    "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
    "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
    "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
    "╨━━┗┛┗┛━━┗┛┗┛━━┻\n"
)
H = (
    "▬▬▬.◙.▬▬▬ \n"
    "═▂▄▄▓▄▄▂ \n"
    "◢◤ █▀▀████▄▄▄▄◢◤ \n"
    "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
    "◥█████◤ \n"
    "══╩══╩══ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ Hello, my friend :D \n"
    "╬═╬☻/ \n"
    "╬═╬/▌ \n"
    "╬═╬/ \\n"
)


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"monster"))
async def bluedevilmonster(monster):
    if event.fwd_from:
        return
    await monster.edit(M)


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"pig"))
async def bluedevipig(pig):
    if event.fwd_from:
        return
    await pig.edit(P)


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"kiler"))
async def bluedevikiller(kiler):
    if event.fwd_from:
        return
    await kiler.edit(K)


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"gun"))
async def bluedevigun(gun):
    if event.fwd_from:
        return
    await gun.edit(G)


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"dog"))
async def bluedevidog(dog):
    if event.fwd_from:
        return
    await dog.edit(D)


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"hmf"))
async def bluedevihmf(hmf):
    if event.fwd_from:
        return
    await hmf.edit(H)


CMD_HELP.update(
    {
        "arts": "**Arts**\
\n\n**Syntax : **`.ded, .monster, .pig, .kiler, .gun, .dog, .hmf`\
\n**Usage :** Makes Anime"
    }
)
