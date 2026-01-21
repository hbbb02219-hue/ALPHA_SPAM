import sys
import glob
import asyncio
import logging
import importlib
import urllib3


from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID
from telethon import events


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_plugins(plugin_name):
    path = Path(f"RAUSHAN/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"RAUSHAN.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["RAUSHAN.modules." + plugin_name] = load
    print("Altron has Imported " + plugin_name)


files = glob.glob("RAUSHAN/modules/*.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\n𝐀𝐥𝐩𝐡𝐚 𝐒𝐩𝐚𝐦 𝐁𝐨𝐭𝐬 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ⚡\nMy Master ---> @ll_ALPHA_BABY_lll")


# ==================== SUDO MANAGEMENT COMMANDS ====================

# Add Sudo User by tagging
@X1.on(events.NewMessage(pattern=r"\.sudo"))
@X2.on(events.NewMessage(pattern=r"\.sudo"))
@X3.on(events.NewMessage(pattern=r"\.sudo"))
@X4.on(events.NewMessage(pattern=r"\.sudo"))
@X5.on(events.NewMessage(pattern=r"\.sudo"))
@X6.on(events.NewMessage(pattern=r"\.sudo"))
@X7.on(events.NewMessage(pattern=r"\.sudo"))
@X8.on(events.NewMessage(pattern=r"\.sudo"))
@X9.on(events.NewMessage(pattern=r"\.sudo"))
@X10.on(events.NewMessage(pattern=r"\.sudo"))
async def add_sudo_user(event):
    # Check if sender is owner
    if event.sender_id != OWNER_ID:
        return await event.reply("❌ **Only Owner Can Use This Command!**")
    
    # Check if user is tagged/replied
    if event.reply_to_msg_id:
        replied_msg = await event.get_reply_message()
        user_id = replied_msg.sender_id
        try:
            user = await event.client.get_entity(user_id)
            user_name = user.first_name
        except:
            user_name = "User"
    elif event.message.entities:
        for entity in event.message.entities:
            if entity.type == "mention" or entity.type == "text_mention":
                if entity.type == "text_mention":
                    user_id = entity.user.id
                    user_name = entity.user.first_name
                else:
                    # For @username mentions
                    username = event.message.text[entity.offset:entity.offset + entity.length]
                    try:
                        user = await event.client.get_entity(username)
                        user_id = user.id
                        user_name = user.first_name
                    except:
                        return await event.reply("❌ **User Not Found!**")
                break
        else:
            return await event.reply("⚠️ **Please Reply To A User Or Tag Someone!**\n\n**Usage:**\n`.sudo` (reply to user)\n`.sudo @username`")
    else:
        return await event.reply("⚠️ **Please Reply To A User Or Tag Someone!**\n\n**Usage:**\n`.sudo` (reply to user)\n`.sudo @username`")
    
    # Check if already sudo
    if user_id in SUDO_USERS:
        return await event.reply(f"⚠️ **{user_name}** (`{user_id}`) **Is Already A Sudo User!**")
    
    # Add to sudo
    SUDO_USERS.append(user_id)
    await event.reply(f"✅ **Successfully Added** {user_name} (`{user_id}`) **To Sudo Users!**")


# Remove Sudo User
@X1.on(events.NewMessage(pattern=r"\.rmsudo"))
@X2.on(events.NewMessage(pattern=r"\.rmsudo"))
@X3.on(events.NewMessage(pattern=r"\.rmsudo"))
@X4.on(events.NewMessage(pattern=r"\.rmsudo"))
@X5.on(events.NewMessage(pattern=r"\.rmsudo"))
@X6.on(events.NewMessage(pattern=r"\.rmsudo"))
@X7.on(events.NewMessage(pattern=r"\.rmsudo"))
@X8.on(events.NewMessage(pattern=r"\.rmsudo"))
@X9.on(events.NewMessage(pattern=r"\.rmsudo"))
@X10.on(events.NewMessage(pattern=r"\.rmsudo"))
async def remove_sudo_user(event):
    if event.sender_id != OWNER_ID:
        return await event.reply("❌ **Only Owner Can Use This Command!**")
    
    if event.reply_to_msg_id:
        replied_msg = await event.get_reply_message()
        user_id = replied_msg.sender_id
        try:
            user = await event.client.get_entity(user_id)
            user_name = user.first_name
        except:
            user_name = "User"
    elif event.message.entities:
        for entity in event.message.entities:
            if entity.type == "mention" or entity.type == "text_mention":
                if entity.type == "text_mention":
                    user_id = entity.user.id
                    user_name = entity.user.first_name
                else:
                    username = event.message.text[entity.offset:entity.offset + entity.length]
                    try:
                        user = await event.client.get_entity(username)
                        user_id = user.id
                        user_name = user.first_name
                    except:
                        return await event.reply("❌ **User Not Found!**")
                break
        else:
            return await event.reply("⚠️ **Please Reply To A User Or Tag Someone!**\n\n**Usage:**\n`.rmsudo` (reply to user)\n`.rmsudo @username`")
    else:
        return await event.reply("⚠️ **Please Reply To A User Or Tag Someone!**\n\n**Usage:**\n`.rmsudo` (reply to user)\n`.rmsudo @username`")
    
    if user_id == OWNER_ID:
        return await event.reply("❌ **Cannot Remove Owner From Sudo!**")
    
    if user_id not in SUDO_USERS:
        return await event.reply(f"⚠️ **{user_name}** (`{user_id}`) **Is Not A Sudo User!**")
    
    SUDO_USERS.remove(user_id)
    await event.reply(f"✅ **Successfully Removed** {user_name} (`{user_id}`) **From Sudo Users!**")


# List Sudo Users
@X1.on(events.NewMessage(pattern=r"\.listsudo"))
@X2.on(events.NewMessage(pattern=r"\.listsudo"))
@X3.on(events.NewMessage(pattern=r"\.listsudo"))
@X4.on(events.NewMessage(pattern=r"\.listsudo"))
@X5.on(events.NewMessage(pattern=r"\.listsudo"))
@X6.on(events.NewMessage(pattern=r"\.listsudo"))
@X7.on(events.NewMessage(pattern=r"\.listsudo"))
@X8.on(events.NewMessage(pattern=r"\.listsudo"))
@X9.on(events.NewMessage(pattern=r"\.listsudo"))
@X10.on(events.NewMessage(pattern=r"\.listsudo"))
async def list_sudo_users(event):
    if event.sender_id not in SUDO_USERS:
        return
    
    sudo_list = "**📋 Sudo Users List:**\n\n"
    for i, uid in enumerate(SUDO_USERS, 1):
        try:
            user = await event.client.get_entity(uid)
            sudo_list += f"{i}. [{user.first_name}](tg://user?id={uid}) - `{uid}`\n"
        except:
            sudo_list += f"{i}. `{uid}`\n"
    
    await event.reply(sudo_list)


# ==================== END SUDO COMMANDS ====================


async def main():
    await X1.run_until_disconnected()
    await X2.run_until_disconnected()
    await X3.run_until_disconnected()
    await X4.run_until_disconnected()
    await X5.run_until_disconnected()
    await X6.run_until_disconnected()
    await X7.run_until_disconnected()
    await X8.run_until_disconnected()
    await X9.run_until_disconnected()
    await X10.run_until_disconnected()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())