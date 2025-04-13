import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","8934899"))
API_HASH = getenv("API_HASH","bf3e98d2c351e4ad06946b4897374a1e")
SOURCE_PHOTO = getenv("SOURCE_PHOTO", "https://k.top4top.io/p_3390ni0g60.jpg")
DEV_URL = getenv("DEV_URL", "https://t.me/rr8r9")
UPDATES_URL = getenv("UPDATES_URL", "https://t.me/k3hbot")
SUPPORT_URL = getenv("SUPPORT_URL", "https://t.me/k3hbot")
BOT_TOKEN = getenv("BOT_TOKEN","7589453501:AAES1q_sBFHTu4XllDvuc5nuWRq1gAzvx54")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://omsnkok:muntazer@cluster0.ywxsjao.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 480))
LOGGER_ID = int(getenv("LOGGER_ID","-1002136390368"))
OWNER_ID = int(getenv("OWNER_ID","1854384004"))
OWNER = int(getenv("OWNER","1854384004"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/xl444")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/xl444")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT","")
CHANNEL_SUDO = getenv("CHANNEL_SUDO", "k3hbot")
YAFA_NAME = getenv("YAFA_NAME", "قناة الاشتراك")
YAFA_CHANNEL = getenv("YAFA_CHANNEL", "https://t.me/k3hbot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/k3hbot")
BOT_USERNAME = getenv("BOT_USERNAME", "net32bot")
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
STRING1 = getenv("STRING_SESSION", "AQCIVfMAJmsozL1DRTOKcWIReA8VVhIIObK9DSaub03sK85_59bxtF1ucQs7F-ZPuEx4y4zXqdPJ04v0nVCkeokkbjmdusi5bAd29Q6xmpKHeQ4PDoQaJzXnZFXZ1ZhyU7iBWXoeL_vFYfWVwQO6pV8nv87ecw-0uvoJSO6G6Wa8c8arafCzzKgoOHgAg14rRRShAr31fltchBx9ak_RXTfCcx_J5fqF5NOInmewnZThPaP6vwAVkyrPgoi8OAjy8cFWzTZUGJwU5CrRqoosd1RnsKaNT6FJxmjpeWAotxwiqxxXphF7FB3gkXoVZ35weOnjNcXV1XT2Vfkud7ZTB0JSlRiQxwAAAAF-OYKaAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv("START_IMG_URL", "https://k.top4top.io/p_3390ni0g60.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://telegra.ph/file/220034b1e9af0ee930981.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )