from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


# 🌈 Colorful Start Buttons
START_BUTTON = [
    [
        Button.inline("🟢 • ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
    ],
    [
        Button.url("🔵 • ᴄʜᴀɴɴᴇʟ •", "https://t.me/ganaasupport"),
        Button.url("🟣 • sᴜᴘᴘᴏʀᴛ •", "https://t.me/ganaasupport")
    ],
    [
        Button.url("🟠 • ʀᴇᴘᴏ •", "https://t.me/ganaasupport")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):

    if not event.is_private:
        return

    AltBot = await event.client.get_me()

    bot_name = AltBot.first_name
    bot_id = AltBot.id

    user_name = event.sender.first_name
    user_id = event.sender.id

    TEXT = (
        f"🟢 **ʜᴇʏ [{user_name}](tg://user?id={user_id})!**\n\n"
        f"🔵 **ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n"
        f"━━━━━━━━━━━━━━━━━━━\n\n"

        f"🟣 **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ : "
        f"[ʜɪɴᴅᴜ ᴄᴏᴍᴍᴜɴɪᴛʏ ™](https://t.me/ganaasupport)**\n\n"

        f"🟠 **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ :** `M3.3`\n\n"

        f"🩵 **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n\n"

        f"🩷 **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** "
        f"`{__version__}`\n"

        f"━━━━━━━━━━━━━━━━━━━\n"
        f"✨ **ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀʟᴘʜᴀ sᴘᴀᴍ**"
    )

    await event.client.send_file(
        event.chat_id,
        "https://files.catbox.moe/marscv.jpg",
        caption=TEXT,
        buttons=START_BUTTON
    )