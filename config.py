## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCtu9wVjpOZ5oNv71oOeh6ZdTEffuQvBZXBoQFNIzbmEXCR2RuLDsAtO6oTd7T6mdgYeAR4cOJSMQPVbvcrb6lOCMcqvIvf5y3nTigJrmlpKfdEB-LHNRxnccNKsog8uDp-uoRH1KA1lLDIKsB4UDDTHTZmX_cTVavV-PY3inyjCJ4J73FVopS-17qhm_rn2ryVpXQKNvuBIr3R4Ucrs97EgYvWg1QoLvPyl1iDLWCzfLECB1lClsH3_JVYFXWLo1YEPl-Rai1fEtwj519DbdtA01mEri1XDXk2pGQhGmNIHKCpnhHlHqKeRB_2F9dJM3GvXlrlGw1wzoAuhK164VrNAAAAASwNfq0A")
BOT_TOKEN = getenv("BOT_TOKEN", "5255513822:AAFGFO49HGQBTOcXu6PX4QAOG6koNZU64yo")
BOT_NAME = getenv("BOT_NAME", "C4")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "c4")
OWNER_USERNAME = getenv("OWNER_USERNAME", "P_i16")
ALIVE_NAME = getenv("ALIVE_NAME", "c4")
BOT_USERNAME = getenv("BOT_USERNAME", "F_c4bot")
OWNER_ID = getenv("OWNER_ID", "5284259786")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "P_i16")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Y7YYYYJ")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Y7YYYYJ")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5034049197").split()))
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
