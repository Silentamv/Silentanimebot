import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "25435105"))
  API_HASH = os.environ.get("API_HASH", "011126265844f2d7cc7dc1a024f6bc78")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6734734174:AAFlFe2iqB7WDjzYksB_ZWC0ZGqjPsZ_qyo")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "@fileeestorebot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002053044713"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "zxlink.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "89e367badb1ee93eab04dd64450e18393d77d302")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6459102722"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://SINGER:SINGER@cluster0.1dt9hoe.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001963382900")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001956959333"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 ᴍʏ ɴᴀᴍᴇ: (https://t.me/{BOT_USERNAME})
│
├🔸 ʟᴀɴɢᴜᴀɢᴇ : [Python 3](https://www.python.org)
│
├🔹 ᴏᴡɴᴇʀ : [Khandudon302](t.me/khandudon302)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
ᴍʏ ᴅᴇᴠ: [➡](https://telegram.me/badal6667rai)
 
 I am Super noob Please Support My Hard Work. 🐸
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also.
"""
