## WhiteEyeUserBot
# EXAMPLE CODE !
```python3
from WhiteEyeUserBot.utils import WhiteEye_on_cmd, sudo_cmd, edit_or_reply
from WhiteEyeUserBot.Configs import Config
@WhiteEye.on(WhiteEye_on_cmd(pattern="alive"))
@WhiteEye.on(sudo_cmd(pattern="alive", allow_sudo=True))
async def hello_world(event):
    if event.fwd_from:
        return
    WhiteEye = await edit_or_reply(event, "Finding My Controllers....")
    await WhiteEye.edit("**HELLO WORLD**\n\nThe following is controlling me too!\n" + Config.SUDO_USERS)
```
