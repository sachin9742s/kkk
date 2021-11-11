import os, time
from os import environ
from translation import Translation


## Main
APP_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", "30aedbb1eec5d7ef58cbd7a168e5c7e5") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "2110357670:AAFKMdz_X9PfmnV8m12sHawVOz8_ruAm5d0") 
USER_SESSION = os.environ.get("SESSION_FILE", "AQDA-BtwLjddpc-7ReG18iRLw0oUtaig1a0_Ipd6pXV6_plouVhzj6ShqMSAasdTpx-wJsob4BpU7zotLXpuoVcbQShUo8Ng_U5KfRcqwvdEGwdw9gMiGrgHTWktL1HwR3zR9iPbF3yn84cKrf8SRME3n0lQ7kwgYzl6412tOvnMLeAPoGQ_jT6M7EkNOR7yAHzLHJxK2LcSQevdbFpq0KJs7lTyeSLTHjsBax0gA_jO8CaMaaApj2evxDlLxz9Tafn2URKjNoJ_rcgtCQJHn_BsO_Mt1qTgw6Eo8yJinWpckPp5Tlan2Ew94a8Qx01j3c9osbhXggHPsLlHUHOL7ZJTbpIirAA")  
DATABASE = os.environ.get("DATABASE_URI", "mongodb+srv://1:1@cluster0.xu6wa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") 
BOT_NAME = os.environ.get("DONLEE_ROBOT", "FLES")
FORCE_CHANNEL = os.environ.get("FORCE_CHANNEL", "Sachin S")
SAVE_USER = os.environ.get("SAVE_USER", "no").lower()
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "gd_film")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "KR_AutoFilter_RoBoT")
DEV_NAME = os.environ.get("DEV_NAME", "SACHIN S")
DEV_USERNAME = os.environ.get("DEV_USERNAME", "sachin_official_admin")
OWNER_ID = set(int(x) for x in os.environ.get("DEV_ID", "2028425293").split())
GROUP = os.environ.get("GROUP", "♂️ Group")
CHANNEL = os.environ.get("CHANNEL", "📣 Updates")
GROUP_LINK = os.environ.get("GROUP_LINK", "https://t.me/KicchaRequest")
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", "t.me/gd_film")
FORCE_SUB_TEXT = os.environ.get("FORCE_TEXT", Translation.FSUB_TEXT)
name_button_welcome = "📣 JOIN MY FILM CHANNEL 📣"
welcome_text_custom = "Hey {mention}\nWelcome To {group_name}\n\nThanks For Your Support"
WELCOME_BUTTON_NAME = os.environ.get("WELCOME_BUTTON_NAME", name_button_welcome)
CUSTOM_WELCOME_TEXT = os.environ.get("WELCOME_TEXT", welcome_text_custom)
CUSTOM_WELCOME = os.environ.get("WELCOME_ENABLE_OR_DISABLE", "no").lower()
BOLD = os.environ.get("FILE_CAPTION", "mono")
PHOTO = (environ.get("PHOTOS", "https://telegra.ph/file/f072e5c3045bd63fd7225.jpg https://telegra.ph/file/0fe4c0533eb36c81af7d7.jpg")).split()
SPELLING_MODE = os.environ.get("SPELLING_MODE_TEXT", Translation.SPELLING_TEXT)
#BUTTON_SIZE = bool(os.environ.get("SIZE_BUTTON"))
BUTTON_MODE = os.environ.get("FILE_BUTTONS", "single").lower()
start_uptime = time.time()
