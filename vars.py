import os

class var(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    API_HASH = os.environ.get("API_HASH", None)
    APP_ID = int(os.environ.get("APP_ID", 6))
    CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME", None)
    CHANNEL_URL = os.environ.get("CHANNEL_URL", None)
    LOGS = int(os.environ.get("LOGS", False))
