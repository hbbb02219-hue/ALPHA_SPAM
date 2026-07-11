import asyncio
import random

import requests
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *
from pyrogram.types import Message


from RAUSHAN.helper.basic import edit_or_reply, get_text
from RAUSHAN.helper.constants import MEMES

from RAUSHAN.plugins.help import *

DEFAULTUSER = "Man"


NOBLE = [
    "╲╲╲┏━━┓╭━━━╮╱╱╱\n╲╲╲┗┓┏┛┃╭━╮┃╱╱╱\n╲╲╲╲┃┃┏┫┃╭┻┻┓╱╱\n╱╱╱┏╯╰╯┃╰┫┏━╯╱╱\n╱╱┏┻━┳┳┻━┫┗┓╱╱╱\n╱╱╰━┓┃┃╲┏┫┏┛╲╲╲\n╱╱╱╱┃╰╯╲┃┃┗━╮╲╲\n╱╱╱╱╰━━━╯╰━━┛╲╲",
    "┏━╮\n┃▔┃▂▂┏━━┓┏━┳━━━┓\n┃▂┣━━┻━╮┃┃▂┃▂┏━╯\n┃▔┃▔╭╮▔┃┃┃▔┃▔┗━┓\n┃▂┃▂╰╯▂┃┗╯▂┃▂▂▂┃\n┃▔┗━━━╮┃▔▔▔┃▔┏━╯\n┃▂▂▂▂▂┣╯▂▂▂┃▂┗━╮\n┗━━━━━┻━━━━┻━━━┛",
    "┏┓┏━┳━┳━┳━┓\n┃┗┫╋┣┓┃┏┫┻┫\n┗━┻━┛┗━┛┗━┛\n────­­­­­­­­­YOU────",
    "╦──╔╗─╗╔─╔ ─\n║──║║─║║─╠ ─\n╚═─╚╝─╚╝─╚ ─\n╦─╦─╔╗─╦╦   \n╚╦╝─║║─║║ \n─╩──╚╝─╚╝",
    "╔══╗....<3 \n╚╗╔╝..('\../') \n╔╝╚╗..( •.• ) \n╚══╝..(,,)(,,) \n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "░I░L░O░V░E░Y░O░U░",
    "┈┈╭━╱▔▔▔▔╲━╮┈┈┈\n┈┈╰╱╭▅╮╭▅╮╲╯┈┈┈\n╳┈┈▏╰┈▅▅┈╯▕┈┈┈┈\n┈┈┈╲┈╰━━╯┈╱┈┈╳┈\n┈┈┈╱╱▔╲╱▔╲╲┈┈┈┈\n┈╭━╮▔▏┊┊▕▔╭━╮┈╳\n┈┃┊┣▔╲┊┊╱▔┫┊┃┈┈\n┈╰━━━━╲╱━━━━╯┈╳",
    "╔ღ═╗╔╗\n╚╗╔╝║║ღ═╦╦╦═ღ\n╔╝╚╗ღ╚╣║║║║╠╣\n╚═ღ╝╚═╩═╩ღ╩═╝",
    "╔══╗ \n╚╗╔╝ \n╔╝(¯'v'¯) \n╚══'.¸./\n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "╔╗ \n║║╔═╦═╦═╦═╗ ╔╦╗ \n║╚╣╬╠╗║╔╣╩╣ ║║║ \n╚═╩═╝╚═╝╚═╝ ╚═╝ \n╔═╗ \n║═╬═╦╦╦═╦═╦═╦═╦═╗ \n║╔╣╬║╔╣╩╬╗║╔╣╩╣╔╝ \n╚╝╚═╩╝╚═╝╚═╝╚═╩╝",
    "╔══╗ \n╚╗╔╝ \n╔╝╚╗ \n╚══╝ \n╔╗ \n║║╔═╦╦╦═╗ \n║╚╣║║║║╚╣ \n╚═╩═╩═╩═╝ \n╔╗╔╗ ♥️ \n║╚╝╠═╦╦╗ \n╚╗╔╣║║║║ \n═╚╝╚═╩═╝",
    "╔══╗╔╗  ♡ \n╚╗╔╝║║╔═╦╦╦╔╗ \n╔╝╚╗║╚╣║║║║╔╣ \n╚══╝╚═╩═╩═╩═╝\n­­­─────­­­­­­­­­YOU─────",
    "╭╮╭╮╮╭╮╮╭╮╮╭╮╮ \n┃┃╰╮╯╰╮╯╰╮╯╰╮╯ \n┃┃╭┳━━┳━╮╭━┳━━╮ \n┃┃┃┃╭╮┣╮┃┃╭┫╭╮┃ \n┃╰╯┃╰╯┃┃╰╯┃┃╰┻┻╮ \n╰━━┻━━╯╰━━╯╰━━━╯",
    "┊┊╭━╮┊┊┊┊┊┊┊┊┊┊┊ \n━━╋━╯┊┊┊┊┊┊┊┊┊┊┊ \n┊┊┃┊╭━┳╮╭┓┊╭╮╭━╮ \n╭━╋━╋━╯┣╯┃┊┃╰╋━╯ \n╰━╯┊╰━━╯┊╰━┛┊╰━━",
]

R = "❤️"
W = "🤍"

heart_list = [
    W * 9,
    W * 2 + R * 2 + W + R * 2 + W * 2,
    W + R * 7 + W,
    W + R * 7 + W,
    W + R * 7 + W,
    W * 2 + R * 5 + W * 2,
    W * 3 + R * 3 + W * 3,
    W * 4 + R + W * 4,
    W * 9,
]
joined_heart = "\n".join(heart_list)
heartlet_len = joined_heart.count(R)
SLEEP = 0.1


async def _wrap_edit(message, text: str):
    """Floodwait-safe utility wrapper for edit"""
    try:
        await message.edit(text)
    except FloodWait as fl:
        await asyncio.sleep(fl.x)


async def phase1(message):
    """Big scroll"""
    BIG_SCROLL = "🧡💛💚💙💜🖤🤎"
    await _wrap_edit(message, joined_heart)
    for heart in BIG_SCROLL:
        await _wrap_edit(message, joined_heart.replace(R, heart))
        await asyncio.sleep(SLEEP)


async def phase2(message):
    """Per-heart randomiser"""
    ALL = ["❤️"] + list("🧡💛💚💙💜🤎🖤")  # don't include white heart

    format_heart = joined_heart.replace(R, "{}")
    for _ in range(5):
        heart = format_heart.format(*random.choices(ALL, k=heartlet_len))
        await _wrap_edit(message, heart)
        await asyncio.sleep(SLEEP)


async def phase3(message):
    """Fill up heartlet matrix"""
    await _wrap_edit(message, joined_heart)
    await asyncio.sleep(SLEEP * 2)
    repl = joined_heart
    for _ in range(joined_heart.count(W)):
        repl = repl.replace(W, R, 1)
        await _wrap_edit(message, repl)
        await asyncio.sleep(SLEEP)


async def phase4(message):
    """Matrix shrinking"""
    for i in range(7, 0, -1):
        heart_matrix = "\n".join([R * i] * i)
        await _wrap_edit(message, heart_matrix)
        await asyncio.sleep(SLEEP)


@Client.on_message(filters.command(["heart", "love"], ".") & filters.me)
async def hearts(client: Client, message: Message):
    await phase1(message)
    await asyncio.sleep(SLEEP * 3)
    await message.edit("❤️ I")
    await asyncio.sleep(0.5)
    await message.edit("❤️ I Love")
    await asyncio.sleep(0.5)
    await message.edit("❤️ I Love You")
    await asyncio.sleep(3)
    await message.edit("❤️ I Love You <3")


@Client.on_message(
    filters.me & (filters.command(["loveyou"], ".") | filters.regex("^loveyou "))
)
async def _(client: Client, message: Message):
    noble = random.randint(1, len(NOBLE) - 2)
    reply_text = NOBLE[noble]
    await edit_or_reply(message, reply_text)


@Client.on_message(filters.command("wink", ".") & filters.me)
async def wink(client: Client, message: Message):
    hmm_s = "https://some-random-api.ml/animu/wink"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    await message.delete()


@Client.on_message(filters.command("hug", ".") & filters.me)
async def hug(client: Client, message: Message):
    hmm_s = "https://some-random-api.ml/animu/hug"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    await message.delete()


@Client.on_message(filters.command("pat", ".") & filters.me)
async def pat(client: Client, message: Message):
    hmm_s = "https://some-random-api.ml/animu/pat"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    await message.delete()


@Client.on_message(filters.command("pikachu", ".") & filters.me)
async def pikachu(client: Client, message: Message):
    hmm_s = "https://some-random-api.ml/img/pikachu"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    if image_s.endswith(".png"):
        await client.send_photo(message.chat.id, image_s)
        return
    if image_s.endswith(".jpg"):
        await client.send_photo(message.chat.id, image_s)
        return
    await message.delete()


@Client.on_message(filters.command("cool", ".") & filters.me)
async def hello_world(client: Client, message: Message):
    mg = await edit_or_reply(
        message,
" ᴀʙᴇ ɢᴀɴᴅᴜ😂😂...ᴘᴀʜᴄʜᴀɴᴀ ʀɪsʜᴀɴᴛ ᴘᴀᴘᴀ ʜᴜ ᴛᴜᴍʜᴀʀᴀ👻 ",
    )


@Client.on_message(
    filters.me & (filters.command(["alpha"], ".") | filters.regex("^alpha"))
)
async def hello_world(client: Client, message: Message):
    mg = await edit_or_reply(message, "ᴀʟᴘʜᴀ")
    await asyncio.sleep(0.3)
    await mg.edit("sʙᴋᴀ ʙᴀᴀᴘ")
    await asyncio.sleep(0.4)
    await mg.edit("ᴏᴘ")
    await asyncio.sleep(0.3)
    await mg.edit("ʙᴀᴋᴋɪ")
    await asyncio.sleep(0.4)
    await mg.edit("sᴀʙ")
    await asyncio.sleep(0.3)
    await mg.edit("ʟᴀɴᴅ ᵏⁱ")
    await asyncio.sleep(0.4)
    await mg.edit("ᴛᴏᴘɪ")
    await asyncio.sleep(0.3)
    await mg.edit(" ᴊᴏʀ sᴇ ʙᴏʟᴏ ʀɪsʜᴀɴᴛ ᴘᴀᴘᴀ ᴊɪ ᴊᴀɪ💘")


@Client.on_message(filters.command("brain", ".") & filters.me)
async def pijtau(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    await message.edit("brain")
    animation_chars = [
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 14])


@Client.on_message(filters.command("bomb", ".") & filters.me)
async def gahite(client: Client, message: Message):
    if message.forward_from:
        return
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await message.edit("`𝐑ɪᴘ ᴍᴀʀ ɢʏᴀ ʙsᴅᴋ😂😂......`")
    await asyncio.sleep(2)


@Client.on_message(filters.command("call", ".") & filters.me)
async def hajqag(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 18)
    await message.edit("Calling ㅤ ʀɪsʜᴀɴᴛ (𝐁ᴀᴀᴘ of telegram)......")
    animation_chars = [
        "`Connecting To Telegram #_ʀɪsʜᴀɴᴛ`",
        "`Call Connected.`",
        "`ʀɪsʜᴀɴᴛ: Hello ʙᴏʟ ᴍᴄ. ᴋᴏɴ ʀᴀɴᴅɪ ᴋᴀ ᴘɪʟʟᴀ ʜᴀɪ ᴛᴜ...ʙsᴅᴋᴇ ᴋʏᴀ ᴋᴀᴀᴍ ʜᴀɪ ᴛᴇʀᴀ..?`",
        f"`Me:  ᴍᴇ ʜᴜɴ ᴛᴇʀᴀ` {DEFAULTUSER} ,`ᴍᴜᴛʜᴇ    ᴇᴋ ʀᴀɴᴅɪ ᴋɪ ɢᴀᴀɴᴅ🍃 ᴋɪ ɢᴀɴᴅ ᴍᴀʀɴɪ ʜᴀɪ..😁😁`",
        "`User Authorised.`",
        "`Calling ㅤ ʀᴀɴᴅɪ ᴋᴀ ᴘɪʟʟᴀ🍃`  `At +916969696969`",
        "`Private  Call Connected...`",
        "`Me:ʜᴇʟʟᴏ ᴍᴄ, ʀᴀɴᴅɪ ᴋᴀ ᴘɪʟʟᴀ🍃...ᴛᴇʀɪ ᴍᴀ ᴋɪ ᴄʜᴜᴛ...🤣🤣😂.`",
        "ㅤ ʀᴀɴᴅɪ ᴋᴀ ᴘɪʟʟᴀ🍃 :ᴏᴋᴀʏ sɪʀ ʙᴜᴛ ᴘᴇʜʟᴇ #_ʀɪsʜᴀɴᴛ ᴋᴀ ʙᴇᴛᴀ ᴋᴏɴ ʜᴀɪ ᴛᴜ?...😎`",
        f"`ᴍᴇ: ᴀʙᴇ ᴢʜᴀᴛᴜ, ɪ ᴀᴍ` {DEFAULTUSER} ",
        "`ㅤ ʀɪsʜᴀɴᴛ🍃 : ᴀʙᴇ ғᴀᴛᴇ ʜᴜʏᴇ ᴄᴏɴᴅᴀᴍ ᴋᴇ ɴᴀᴛɪᴊᴇ...🤣🤣\nʙsᴅᴋᴇ ɢʜᴀʀ ᴍᴇ ɢʜᴜsᴋᴇ ᴛᴇʀɪ ᴀᴍᴍᴀ ʙᴇʜᴇɴ ᴋᴀ ʀᴇᴘ ᴋᴀʀᴅᴜɴɢᴀ ᴢʜᴀᴛᴜ😜.`",
        "`ᴍᴇ: ᴀʙᴇ ʙsᴅᴋᴇ... ᴛᴇʟᴇɢʀᴀᴍ #_ʀɪsʜᴀɴᴛ ᴋᴏ ᴄʜᴀʟᴀ ʀᴀʜᴀ ᴋɪ #_ʀɪsʜᴀɴᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴋᴏ ᴄʜᴀʟᴀ ʀᴀʜᴀ...?😜.`",
        "`ㅤ ʀɪsʜᴀɴᴛ🍃 : ʙᴇᴛᴇ...!! ɴᴀᴀ ᴊᴀᴍɪɴ ᴘᴇ ɴᴀ ᴀᴀsᴍᴀɴ ᴘᴇ...😉😉 ᴛᴇʀɪ ᴍᴀʏʏᴀ ᴋᴏ ᴄʜʜᴏᴅᴜɴɢᴀ ᴍᴇ #_ʀɪsʜᴀɴᴛᴡᴏʀʟᴅ ᴋᴇ ʜᴀᴠᴇʟɪ ᴘᴇ...🥵🥵.`",
        "`ᴍᴇ: ʙʜᴀɪ...ʏᴀᴀʀ ᴍᴇʀɪ ɢᴀᴀɴᴅ ᴍᴀʀᴏ ʙᴜᴛ ᴍᴜᴊʜᴇ ᴍᴀғ ᴋᴀʀᴏ...🤯`",
        "`ㅤ ʀɪsʜᴀɴᴛ🍃 : ʜɪʜɪʜɪ... ʏᴇ ʜᴜɪ ɴᴀ ʙᴀᴀᴛ....😁😁\nᴄʜᴀʟ ᴀᴀʙ ᴀᴀᴘɴɪ ʀᴀɴᴅɪ ᴍᴀʏʏᴀ ᴋᴏ #_ʀɪsʜᴀɴᴛᴡᴏʀʟᴅ ᴋᴇ ᴠᴄ ᴘᴇ ʙᴜʟᴀ ᴋᴇ ʟᴏᴠᴇ ᴜ ʙᴏʟɴᴇ  ᴋᴏ ʙᴏʟ😛😛.`",
        "`ᴍᴇ: ʙʜᴀɪ ᴘʟᴢ ɢᴀʟɪ ᴍᴛ ᴅᴏ😥.`",
        "`ㅤ ʀɪsʜᴀɴᴛ🍃 : ᴛᴏ #_ʀɪsʜᴀɴᴛ ᴋᴏ ʙᴀᴀᴘ ʙᴏʟ ᴀᴜʀ...ᴄʜᴀʟ ʙʜᴀɢ ʏᴀʜᴀ sᴇ ᴍᴄ..ʙsᴅᴋᴇ ᴋᴇ ᴘʜɪʀ ᴄᴀʟʟ ᴋɪʏᴀ ᴛᴏ #_ʀɪsʜᴀɴᴛ ᴋɪ ᴠᴄ ᴘᴇ ᴛᴇʀᴇ ʙᴀᴀᴘ ᴋɪ ᴄʜᴜᴛ ᴍᴀʀᴜɴɢᴀ..🤣🤣  \n🙈𝐓ɢ 𝐏ᴇ 𝐑ᴇʜɴᴀ 𝐇ᴀɪ 𝐓ᴏ🧐 Rɪsʜᴀɴᴛ 𝐊ᴏ 𝐁ᴀᴀᴘ 💞 𝐁ᴏʟɴᴀ 𝐇ᴀɪ🤪 @oye_babyy 👻 :)`",
        "`ᴘʀɪᴠᴀᴛᴇ ᴄᴀʟʟ ᴅɪsᴄᴏɴɴᴇᴄᴛᴇᴅ....ᴊᴏʀ sᴇ ʙᴏʟᴏ ʀɪsʜᴀɴᴛ ᴘᴀᴘᴀ ᴊɪ ᴊᴀɪ🤣🤣🤣`",
    ] 
