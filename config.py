from pyrogram import filters
import os

class Config:
    API_ID = int(getenv("API_ID","9181844"))
     API_HASH = getenv("API_HASH","996a3e7194a4f07576fda5c20bb1138b")

    
     TOKEN = os.environ.get("TOKEN", "7293989365:AAEQdlSr66POVnmWJpewxTGIgL2iZ1iKcpU")
    MONGO_URL = "mongodb+srv://hakermoni732:hakermoni732@cluster0.e914k0n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    START_PIC = "https://telegra.ph/file/0eba143d65f9413f9ae04.jpg"
    SUDOERS = filters.user(["6649395836"])
