from pyrogram import filters
import os

class Config:
    API_ID = "27798659"
    API_HASH = "26100c77cee02e5e34b2bbee58440f86"

     #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", "7573604459:AAGwUKl86kOEelpd7H7-oKJE942bRJHEn-I")
    MONGO_URL = "mongodb+srv://moni:moni@cluster0.bsscl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    START_PIC = "https://telegra.ph/file/0eba143d65f9413f9ae04.jpg"
    SUDOERS = filters.user(["5444362033"])
