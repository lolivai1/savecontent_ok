#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("14000256", default=None, cast=int)
API_HASH = config("61158815c58e158cfa9520c85676a450", default=None)
BOT_TOKEN = config("5361708656:AAGpuTtWO_xTgMyfEjIAifshFpGY-5yYMAw", default=None)
SESSION = config("AQCXThtP3dP80ILlK6e6jhsIQ1eBVIm4P7O1ZDxvqTxOwB-ySw4vWJK9NwRYqPxyVW6ym_NSPlnbuh3OSv4vZaamu7D0NgRID-JrhZHvnhauwbRfbpOt5eOsNSOD11Ql2jYiI5QPGVuDw7HGWbSUe-cfeJbgXNfwvHcmAMQIf9NDEdBPXV-26KZr8oOJzzHaH4npyqZVoG4HcM62BvtyQqGUV9w0y0mvhfeDXODtYTA8qxF9zEMt9WPJo5a0pJ6Pw6IxVmxXfbKJE1SUR-jM5HjzE_TTWrmjuijCFlrB1jL5gWYS9GxSppRBdsjE496jIkyKA9HK9FeaBzQiy_rK7tYIK5WsJAA", default=None)
FORCESUB = config("cont_blo_bot", default=None)
AUTH = config("731229220", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
