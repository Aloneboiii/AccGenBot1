import os
import logging
from telethon import TelegramClient, Button, events
from vars import var

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

APP_ID = var.APP_ID
API_HASH = var.API_HASH
BOT_TOKEN = var.BOT_TOKEN


BotzCity = TelegramClient('BotzCity', APP_ID, API_HASH).start(bot_token=BOT_TOKEN)

enjoy = "**Made with ❤️ by @BotzCity**"

BACK = [[Button.inline("⬅️ Back", data="gen")]]
