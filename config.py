from pyrogram import filters
import os

class Config:
    API_ID =  "20611365"
API_HASH =  "424e183d2cf8a7f2c8bafeeaab1b5c8c"
    TOKEN = os.environ.get("TOKEN", "7573604459:AAGtbbye_5vZJb6Ezimlm-jJIQ2aogOQdEw")
    MONGO_URL = "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://telegra.ph/file/0eba143d65f9413f9ae04.jpg"
    SUDOERS = filters.user(["7290811275"])
