from pyrogram import filters
import os

class Config:
    API_ID = "27798659"
    API_HASH = "26100c77cee02e5e34b2bbee58440f86"

     #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", "7573604459:AAGtbbye_5vZJb6Ezimlm-jJIQ2aogOQdEw")
    MONGO_URL = "mongodb+srv://ChikuAiDb:MysticalDevs@chikuaidb.1pfxx.mongodb.net/?retryWrites=true&w=majority&appName=ChikuAiDB"
    START_PIC = "https://telegra.ph/file/0eba143d65f9413f9ae04.jpg"
    SUDOERS = filters.user(["5444362033"])
