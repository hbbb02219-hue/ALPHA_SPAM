from telethon import events
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS
import asyncio
import random

BOSS_MESSAGES = [
    # Devil Style
    "😈 𝗥𝗜𝗦𝗛𝗔𝗡𝗧 𝗧𝗛𝗔𝗞𝗨𝗥 😈\n👿 THE DEVIL HIMSELF 👿",
    "☠️ ℝ𝕀𝕊ℍ𝔸ℕ𝕋 𝕋ℍ𝔸𝕂𝕌ℝ ☠️\n💀 DANGER ZONE 💀",
    "🔥 𝑹𝑰𝑺𝑯𝑨𝑵𝑻 𝑻𝑯𝑨𝑲𝑼𝑹 🔥\n🌋 HELL'S KING 🌋",
    "👹 ＲＩＳＨＡＮＴ ＴＨＡＫＵＲ 👹\n⚰️ DEATH DEALER ⚰️",
    "💎 ᖇIᔕᕼᗩᑎT TᕼᗩKᑌᖇ 💎\n👑 THE BOSS 👑",
    "⚡ 尺ノ丂んﾑ刀ｲ ｲんﾑズひ尺 ⚡\n💪 UNSTOPPABLE 💪",
    "🗡️ 𝓡𝓘𝓢𝓗𝓐𝓝𝓣 𝓣𝓗𝓐𝓚𝓤𝓡 🗡️\n⚔️ WARRIOR 🔪",
    "🎯 ꋪꀤꌗꃅꍏꈤ꓄ ꓄ꃅꍏꀘꀎꋪ 🎯\n🔫 SHOOTER 🔫",
    "👿 RISHANT THAKUR आ गया 👿\n😈 शैतान की औलाद 😈",
    "☠️ RISHANT THAKUR से पंगा? ☠️\n💀 मौत के करीब आ गए 💀",
    "🔥 RISHANT THAKUR का नाम सुना है? 🔥\n👹 डर के मारे भाग जाओ 👹",
    "💣 RISHANT THAKUR बम फोड़ेगा 💣\n🧨 तबाही मचा देगा 🧨",
    "⚠️ 𝗗𝗔𝗡𝗚𝗘𝗥 ⚠️\n🚨 RISHANT THAKUR 🚨\n⚠️ 𝗦𝗧𝗔𝗬 𝗔𝗪𝗔𝗬 ⚠️",
    "🚫 WARNING 🚫\n⛔ RISHANT THAKUR ZONE ⛔\n🚷 ENTRY NOT ALLOWED 🚷",
    "☢️ TOXIC ☢️\n☣️ RISHANT THAKUR ☣️\n☢️ POISON ☢️",
    "💪 RISHANT THAKUR बोला तो सब चुप 💪",
    "😎 RISHANT THAKUR की औकात देख 😎",
    "🤘 RISHANT THAKUR रॉक करता है 🤘",
    "🔥 RISHANT THAKUR आग लगा देगा 🔥",
    "⚡ RISHANT THAKUR बिजली है ⚡",
    "🚬 𝗥𝗜𝗦𝗛𝗔𝗡𝗧 𝗧𝗛𝗔𝗞𝗨𝗥 🚬\n🔫 REAL GANGSTER 🔫",
    "🕶️ RISHANT THAKUR 🕶️\n💼 MAFIA BOSS 💼",
    "🎩 RISHANT THAKUR 🎩\n🃏 GODFATHER 🃏",
    "💥 RISHANT THAKUR का जलवा 💥",
    "⚡ RISHANT THAKUR की बिजली ⚡",
    "🌪️ RISHANT THAKUR का तूफान 🌪️",
    "🔥 RISHANT THAKUR की आग 🔥",
    "💣 RISHANT THAKUR का धमाका 💣",
    "👿 शैतान से दोस्ती है मेरी\n😈 RISHANT THAKUR मेरा नाम 😈",
    "☠️ मौत से खेलता हूं मैं\n💀 RISHANT THAKUR हूं मैं 💀",
    "🔥 नरक से आया हूं\n👹 RISHANT THAKUR 👹",
    "⚰️ कब्र खोद दूंगा\n☠️ RISHANT THAKUR ☠️",
]

async def boss_handler(event):
    """Main handler for .boss command"""
    if event.sender_id not in SUDO_USERS:
        return

    try:
        # Parse counter from command
        parts = event.text.split()
        if len(parts) > 1:
            counter = int(parts[1])
        else:
            counter = 40  # Default
    except (IndexError, ValueError):
        counter = 40

    await event.delete()

    # Epic Entry
    try:
        await event.respond("🚨 **WARNING! DEVIL IS COMING** 🚨")
        await asyncio.sleep(1)
        await event.respond("😈 **RISHANT THAKUR ENTERING...** 😈")
        await asyncio.sleep(1)
        await event.respond("💥 **BOSS MODE ACTIVATED!** 💥")
        await asyncio.sleep(1)

        # Send messages
        for i in range(counter):
            msg = random.choice(BOSS_MESSAGES)
            await event.respond(msg)
            await asyncio.sleep(0.5)
            
    except Exception as e:
        print(f"Error in boss command: {e}")

# Register handlers for all clients
X1.on(events.NewMessage(incoming=True, pattern=r"^\.boss(\s+\d+)?$"))(boss_handler)
X2.on(events.NewMessage(incoming=True, pattern=r"^\.boss(\s+\d+)?$"))(boss_handler)
X3.on(events.NewMessage(incoming=True, pattern=r"^\.boss(\s+\d+)?$"))(boss_handler)
X4.on(events.NewMessage(incoming=True, pattern=r"^\.boss(\s+\d+)?$"))(boss_handler)
X5.on(events.NewMessage(incoming=True, pattern=r"^\.boss(\s+\d+)?$"))(boss_handler)
X6.on(events.NewMessage(incoming=True, pattern=r"^\.boss(\s+\d+)?$"))(boss_handler)
X7.on(events.NewMessage(incoming=True, pattern=r"^\.boss(\s+\d+)?$"))(boss_handler)
X8.on(events.NewMessage(incoming=True, pattern=r"^\.boss(\s+\d+)?$"))(boss_handler)
X9.on(events.NewMessage(incoming=True, pattern=r"^\.boss(\s+\d+)?$"))(boss_handler)
X10.on(events.NewMessage(incoming=True, pattern=r"^\.boss(\s+\d+)?$"))(boss_handler)