from pyrogram import filters
import os

class Config:
API_ID = "20611365"
API_HASH = "424e183d2cf8a7f2c8bafeeaab1b5c8c"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
TOKEN = os.environ.get("TOKEN", "7573604459:AAGtbbye_5vZJb6Ezimlm-jJIQ2aogOQdEw")
MONGO_URL = "mongodb+srv://monivps5:monivps5@cluster0.kmbq8we.mongodb.net/?retryWrites=true&w=majority"
START_PIC = "https://telegra.ph/file/0eba143d65f9413f9ae04.jpg"
SUDOERS = filters.user(["7290811275"])
