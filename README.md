# WhiteEyeUserBot
![Python Version](https://img.shields.io/badge/Python-v3.8-blue)
![Repo Size](https://img.shields.io/github/repo-size/WhiteEye-Org/WhiteEyeUserBot)
[![Commit Activity](https://img.shields.io/github/commit-activity/w/WhiteEye-Org/WhiteEyeUserBot)](https://github.com/WhiteEye-Org/WhiteEyeUserBot/pulse)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b10d40c60fc549299eeb7bda1c7501aa)](https://app.codacy.com/manual/WhiteEye-Org/WhiteEyeUserBot?utm_source=github.com&utm_medium=referral&utm_content=athphane/userbot&utm_campaign=Badge_Grade_Settings)
[![HitCount](http://hits.dwyl.com/WhiteEye-Org/WhiteEyeUserBot.svg)](http://hits.dwyl.com/WhiteEye-Org/WhiteEyeUserBot)
[![Contributors](https://img.shields.io/github/contributors/WhiteEye-Org/WhiteEyeUserBot)](https://github.com/WhiteEye-Org/WhiteEyeUserBot/graphs/contributors)
![Last Commit](https://img.shields.io/github/last-commit/WhiteEye-Org/WhiteEyeUserBot/master)
![Issues](https://img.shields.io/github/issues/WhiteEye-Org/WhiteEyeUserBot)
![Pull Requests](https://img.shields.io/github/issues-pr/WhiteEye-Org/WhiteEyeUserBot)
[![StyleCI](https://github.styleci.io/repos/216083990/shield?branch=master)](https://github.styleci.io/repos/216083990)
[![License](https://img.shields.io/github/license/WhiteEye-Org/WhiteEyeUserBot)](LICENSE)

<img src="https://telegra.ph/file/28d9b7eb6ef941325bc64.jpg" width="190" align="right">





# SUPPORT

<a href="https://t.me/Whiteeyedevs"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>

<a href="https://t.me/WhiteEyeDevs"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>



# Tutorial (Explained How To Deploy WhiteEyeUserBot With Tutorial Video)

<a href="https://youtu.be/2QkKREW0nOE"><img src="https://img.shields.io/badge/HEROKU-TUTORIAL-brightgreen"></a> <a href="https://studio.youtube.com/channel/UCHzrSYy9-R594Ywgba_F7kQ/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"><img src="https://img.shields.io/badge/UFFIZZI-TUTORIAL-brightgreen"></a>





# GET APP_ID AND API_HASH

[![APP_ID](https://img.shields.io/badge/API__HASH--APP__ID-HERE-brightgreen)](https://my.telegram.org/auth)






# DEPLOY

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/WhiteEye-Org/WhiteEyeUserBot)
# String

[![Run on Repl.it](https://img.shields.io/badge/run-string__session.py-red?style=for-the-badge&logo=repl.it)](https://repl.it/@mrdayamzaidi/WhiteEyeUserbot)

# DEPLOY TO UFFIZZI

[![Deploy To Uffizzi](https://img.shields.io/badge/-Deploy%20To%20Uffizzi-informational)](https://app.uffizzi.com/dashboard)

# DATABASE_URL

[![DATABASE_URL](https://img.shields.io/badge/DATABASE__URL-HERE-success)](https://customer.elephantsql.com/login)



## Simply clone the repository and run the main file:
```sh
# Install Git First // (Else You Can Download And Upload to Your Local Server)
$ git clone https://github.com/WhiteEye-Org/WhiteEyeUserBot
# Open Git Cloned File
$ cd WhiteEyeUserBot
# Config Virtual Env (Skip is already Done.)
$ virtualenv -p /usr/bin/python3 venv
$ . ./venv/bin/activate
# Install All Requirements 
$ pip(3) install -r requirements.txt
# Create local.env with variables as given below
# Start Bot 
$ python(3) -m WhiteEyeUserBot
```

# Mandatory Configs
```
[+] Make Sure You Add All These Mandatory Vars. 
    [-] ALIVE_NAME : Your Name Here
    [-] APP_ID:   You can get this value from https://my.telegram.org
    [-] API_HASH :   You can get this value from https://my.telegram.org
    [-] STRING_SESSION : Your String Session, You can get this From Repl or BY running StringGen File Locally
    [-] TG_BOT_TOKEN : Your Bot Token Obtained From @BotFather 
    [-] TG_BOT_USERNAME : Your Bot UserName Obtained From @BotFather
    [-] PRIVATE_GROUP_ID : Id of group where you wanna log important logs, Private group is recommended for this
    [-] DATABASE_URL: Data Base Url, You Can Make You Own By Following This Tutorial - https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04, Else Get this from Elephant Sql, Or You can even make a heroku app to get Free DataBase.
[+] The WhiteEyeUserBot will not work without setting the mandatory vars.
```


## An Example Of "local.env" File.
```
APP_ID=2877510
API_HASH="fb6e6a1d96f3e6ea1b8e293912bd2edf"
STRING_SESSION="1AZWarzkBu6awXELYNW1w9xUMBt4OKtuOyMXX50ut5fUZ0oMo-0Qcp-GPDDc6YomgR7YdIL4woqQPHxpIvq6AXfPVbSeMN4nj_89Y03NSuDcEVOMhuJkfA6tTVUVPlkh4cQDgIwygG9GUYCAyntL4OvDIjLjNpkI68aSIrB9xChqa6T4uqn74AgRoUvN_5SQ0Y5F2Z6fz7UluwC33j0TuPMOWAdrcSooiIcjxe3WKtao6xz6-dWd0085sND8liyAdDrSQymzSC98kXx1Evo2GJG9matA6aGEyxNW_awuKB5Djjm6wkLszuYVuc03oeD9WNlyFtA-d_bd9Ge-TIScItpkiM8r4CCo="
TG_BOT_TOKEN="1651787609:AAFT8tyKb_h1kSS7zFLJ8Uqx3wmesqIUjls"
TG_BOT_USERNAME="yourbotusername"
PRIVATE_GROUP_ID=-100535552668
DATABASE_URL="postgres://jchzxwhkwuhbldjnxqfp:142.compute1.amazonaws.com:5432/d14c1pas7r1clf"
```







# Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

WhiteEyeUserbot is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 
