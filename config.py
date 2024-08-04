from pyrogram import filters
import os

class Config:
    API_ID = "12380656"
    API_HASH = "d927c13beaaf5110f25c505b7c071273"

     #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", "7265494810:AAGJa4E8PpkCRBPSE3C2ckoh6do8TB0WCTs")
    MONGO_URL = "mongodb+srv://bikash:bikash@bikash.3jkvhp7.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://telegra.ph/file/0eba143d65f9413f9ae04.jpg"
    SUDOERS = filters.user(["7355470487"])
