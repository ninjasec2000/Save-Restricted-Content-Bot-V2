# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21268963"))
API_HASH = getenv("API_HASH", "60239424717807c61aa7e446d443984f")
BOT_TOKEN = getenv("BOT_TOKEN", "7483825602:AAHkUSZmC_qlJzR62MnOhO5udo9EPdU2-fg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5955963998").split()))
MONGO_DB = getenv("MONGO_DB", None)
LOG_GROUP = getenv("LOG_GROUP", "-1002363247735")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002438586582"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  
