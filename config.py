## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BACbMHbpCWi_qSLzSRoQViMmUxlfUNTa6QmHj1_bHQOdfvslhLlrDczeoXWoBlLvG-r9nAtthkrZ725XbE0A3NjV_MbhWgXK9Tx9qGX6Yx6FPenTMySXhb5-LMHGUzHDVTgFDisnY9VQd7BQAODzORfKOgtHeDf2TbPfxejbnzF2br2cMxARV8ltPaBaXkTxm1MQgihtKy9XcVu7glBS1g5SG10ht7ga1ghtCYAZFpkquOcx2vvGnVxlgE9CVItOWuq7Ex_PfpUJfr_3ip_VW6S7LfSpDhSt4csN74rSKFe1XLS80rgSsCCvKgRnrrlOMu8gzAY9jefCGWoXSvkgMiXZAAAAAUZGEccA")
BOT_TOKEN = getenv("BOT_TOKEN", "5509082199:AAEDkfs0CjpP_l1sJqQrI7v82LG2IrRVjjs")
BOT_NAME = getenv("BOT_NAME", "𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 🎧")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "AHMED")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ku_kx")
ALIVE_NAME = getenv("ALIVE_NAME", "AHMED")
BOT_USERNAME = getenv("BOT_USERNAME", "v2u2bot")
OWNER_ID = getenv("OWNER_ID", "5297963487")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "YY3TT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "uxxx_u")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "uxxxu")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5297963487").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
