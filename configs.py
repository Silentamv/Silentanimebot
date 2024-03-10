import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "27505575"))
  API_HASH = os.environ.get("API_HASH", "03bbc5e15dbddfb03fb953435b5eb028")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7028356497:AAFtBVcZE4N5dYUGSa2B8awtSuFETLxUkuA")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "silentfilestorebot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002007510451"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "Ziplinker.net")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "760615c59a2a8723d5b2e85a8ccc42f58170fecc")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6459102722"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Aru:xitheIzcM2MVw9Lf@aru.brkfhe9.mongodb.net/?retryWrites=true&w=majority&appName=Aru")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002084706768")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002132361598"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
 ʜᴇʀᴇ ᴡᴇ ɢᴏ ᴄʜᴇᴄᴋᴏᴜᴛ ᴍʏ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ✔
  
 🚩 ʟᴏᴏᴋ ʙᴇʟᴏᴡ ᴍʏ ꜰʀɪᴇɴᴅ 🚩

▶ ᴍʏ ɴᴀᴍᴇ : ꜰɪʟᴇ ꜱᴛᴏʀᴇ
▶ ꜱᴇʀᴠᴇʀ : ʜᴇʀᴏᴋᴜ

🌿 ɴᴇᴠᴇʀꜰᴏʟᴅ ɴᴇᴠᴇʀ ʙᴀᴄᴋᴅᴏᴡɴ 🌿
"""
  ABOUT_DEV_TEXT = f"""
ᴍʏ ᴅᴇᴠ: [➡](https://telegram.me/silent_amv)
 
 I am Super noob Please Support My Hard Work. 🐸
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **File Store Bot**.

📢 ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ & ɪᴛ ᴡɪʟʟʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ & ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴛʜᴇ (ꜱʜᴏʀᴛᴇɴᴇᴅ) ꜰɪʟᴇ ʟɪɴᴋ.
"""
