from telethon import events
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS
import asyncio
import random

# ============ LOVE ANIMATION COMMAND ============

async def love_handler(event):
    """Main handler for .love command"""
    if event.sender_id not in SUDO_USERS:
        return

    # Check if replied to someone
    if not event.is_reply:
        await event.reply("⚠️ **Kisi ladki ko reply karke use karo!** 💕")
        return

    try:
        await event.delete()
    except:
        pass

    replied_msg = await event.get_reply_message()
    
    try:
        user = await event.client.get_entity(replied_msg.sender_id)
        girl_name = user.first_name or "Beautiful"
    except:
        girl_name = "Beautiful"

    # STAGE 1: Heart Beat Animation
    heartbeat = [
        "💗",
        "💗💗",
        "💗💗💗",
        "❤️‍🔥❤️‍🔥❤️‍🔥",
        "💖💖💖💖💖",
    ]

    msg = await event.respond("💗")
    for frame in heartbeat:
        await asyncio.sleep(0.3)
        try:
            await msg.edit(frame)
        except:
            pass

    await asyncio.sleep(0.5)

    # STAGE 2: Searching for Love
    try:
        await msg.edit("```\n🔍 SEARCHING...\n>>> Looking for someone special...```")
        await asyncio.sleep(0.6)
        await msg.edit("```\n🔍 SEARCHING...\n>>> Scanning beautiful souls...\n>>> Processing...```")
        await asyncio.sleep(0.6)
        await msg.edit(f"```\n🔍 SEARCHING...\n>>> Perfect match found!\n>>> Target: {girl_name} 💕```")
    except:
        pass

    await asyncio.sleep(0.7)

    # STAGE 3: Loading Her Name
    name_animation = []
    for i in range(1, len(girl_name) + 1):
        name_animation.append(girl_name[:i])

    for frame in name_animation:
        await asyncio.sleep(0.15)
        try:
            await msg.edit(f"```\n💕 LOADING...\n\n>>> {frame}_```")
        except:
            pass

    await asyncio.sleep(0.6)

    # STAGE 4: Heart Formation
    heart_frames = [
        "♥",
        "♥ ♥\n♥",
        "♥   ♥\n♥     ♥\n♥   ♥\n ♥ ♥\n  ♥",
        f"❤️   ❤️\n❤️  {girl_name[:3]}  ❤️\n❤️   ❤️\n ❤️ ❤️\n  ❤️",
    ]

    for frame in heart_frames:
        await asyncio.sleep(0.4)
        try:
            await msg.edit(frame)
        except:
            pass

    await asyncio.sleep(0.7)

    # STAGE 5: Beauty Analysis
    try:
        await msg.edit("```\n📊 ANALYZING BEAUTY...\n\n█░░░░░░░░░ 10%```")
        await asyncio.sleep(0.3)
        await msg.edit("```\n📊 ANALYZING BEAUTY...\n\n████░░░░░░ 40%```")
        await asyncio.sleep(0.3)
        await msg.edit("```\n📊 ANALYZING BEAUTY...\n\n███████░░░ 70%```")
        await asyncio.sleep(0.3)
        await msg.edit("```\n📊 ANALYZING BEAUTY...\n\n██████████ 100%\n\n✨ BREATHTAKING!```")
    except:
        pass

    await asyncio.sleep(0.7)

    # STAGE 6: Her Stats (Flirty)
    stats_animation = [
        f"💕 BEAUTY PROFILE\n━━━━━━━━━━━━━━\nName: {girl_name}\nSmile: LOADING...",
        f"💕 BEAUTY PROFILE\n━━━━━━━━━━━━━━\nName: {girl_name}\nSmile: ⭐⭐⭐⭐⭐ Perfect\nEyes: LOADING...",
        f"💕 BEAUTY PROFILE\n━━━━━━━━━━━━━━\nName: {girl_name}\nSmile: ⭐⭐⭐⭐⭐ Perfect\nEyes: 😍 Mesmerizing\nPersonality: LOADING...",
        f"💕 BEAUTY PROFILE\n━━━━━━━━━━━━━━\nName: {girl_name}\nSmile: ⭐⭐⭐⭐⭐ Perfect\nEyes: 😍 Mesmerizing\nPersonality: 💎 Diamond\nStatus: LOADING...",
        f"💕 BEAUTY PROFILE\n━━━━━━━━━━━━━━\nName: {girl_name}\nSmile: ⭐⭐⭐⭐⭐ Perfect\nEyes: 😍 Mesmerizing\nPersonality: 💎 Diamond\nStatus: 👑 QUEEN 👑"
    ]

    for frame in stats_animation:
        await asyncio.sleep(0.5)
        try:
            await msg.edit(frame)
        except:
            pass

    await asyncio.sleep(0.8)

    # STAGE 7: Rose Animation
    rose_animation = [
        "🌹",
        "🌹🌹",
        "🌹🌹🌹",
        "🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹",
        f"🌹🌹🌹🌹🌹🌹🌹\n\n   For {girl_name}\n   \n🌹🌹🌹🌹🌹🌹🌹",
    ]

    for frame in rose_animation:
        await asyncio.sleep(0.3)
        try:
            await msg.edit(frame)
        except:
            pass

    await asyncio.sleep(0.7)

    # STAGE 8: Romantic Quotes Slideshow
    quotes = [
        f"💌 Dear {girl_name},\n\n\"तेरी हंसी में वो जादू है,\nजो दिल को चैन ना आने दे...\" \n\n✨ - RISHANT THAKUR ✨",
        f"💌 Dear {girl_name},\n\n\"तेरी आँखों में खो जाऊं,\nबस यही ख्वाहिश है मेरी...\" \n\n✨ - RISHANT THAKUR ✨",
        f"💌 Dear {girl_name},\n\n\"तू चाँद है, तारे हैं,\nमेरी दुनिया तू ही है...\" \n\n✨ - RISHANT THAKUR ✨",
    ]

    for quote in quotes:
        await asyncio.sleep(0.8)
        try:
            await msg.edit(quote)
        except:
            pass

    await asyncio.sleep(1)

    # STAGE 9: Cupid's Arrow
    arrow_animation = [
        "💘\n\nCupid's Arrow\nLoading...",
        "💘  →\n\nTaking Aim...",
        "💘    →  →\n\nLocked On Target!",
        f"💘  →  →  →  💖\n\nHIT! {girl_name}'s Heart!\n\n❤️‍🔥 LOVE ATTACK! ❤️‍🔥",
    ]

    for frame in arrow_animation:
        await asyncio.sleep(0.5)
        try:
            await msg.edit(frame)
        except:
            pass

    await asyncio.sleep(0.8)

    # STAGE 10: Love Letter
    love_letter = f"""┌────────────────────────┐
│  ✉️ LOVE LETTER ✉️  │
└────────────────────────┘

प्यारी {girl_name},

जब से तुझे देखा है,
दिल की धड़कन बदल गई है... 💓

तेरी मुस्कान मेरी दुनिया है,
तेरी बातें मेरा संगीत है... 🎵

क्या तू मेरी हो सकती है? 💕

With Love,
RISHANT THAKUR 👑

━━━━━━━━━━━━━━━━━━━━"""

    try:
        await msg.edit(love_letter)
    except:
        pass
    await asyncio.sleep(2)

    # STAGE 11: Sparkling Hearts
    sparkle_frames = [
        "✨",
        "✨💖✨",
        "✨💖✨💖✨",
        f"✨✨✨✨✨✨✨\n\n{girl_name}\n\nYou're Special!\n\n✨✨✨✨✨✨✨",
    ]

    for frame in sparkle_frames:
        await asyncio.sleep(0.4)
        try:
            await msg.edit(frame)
        except:
            pass

    await asyncio.sleep(0.8)

    # STAGE 12: FINAL GRAND REVEAL
    final_message = f"""╔══════════════════════════════╗
║   💖 LOVE DECLARATION 💖    ║
╚══════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👸 Princess: {girl_name}

🌟 Beauty Level: ∞ INFINITE
😍 Charm: IRRESISTIBLE
💎 Value: PRICELESS
✨ Aura: MAGICAL
❤️ Effect on Heart: DEVASTATING

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💌 MESSAGE FROM RISHANT THAKUR:

"तू मेरी दुनिया है,
तू मेरी ज़िंदगी है,
तेरे बिना सब अधूरा है... 💕

क्या तू मेरे साथ
इस ज़िंदगी का सफर तय करेगी? 🌹"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👑 From: RISHANT THAKUR
💕 To: {girl_name}
🌹 With: Pure Love

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💖 WILL YOU BE MINE? 💖"""

    try:
        await msg.edit(final_message)
    except:
        pass

    await asyncio.sleep(2)

    # STAGE 13: Romantic Spam Burst
    romantic_messages = [
        f"💕 {girl_name}, तू बेहद खूबसूरत है! 💕",
        f"🌹 {girl_name}, तेरी smile magical है! 🌹",
        f"✨ {girl_name}, तू एक angel है! ✨",
        f"💖 {girl_name}, मेरी दुनिया तू है! 💖",
        f"😍 {girl_name}, तुझसे प्यार हो गया! 😍",
        f"💝 {girl_name}, तू मेरी जान है! 💝",
        f"🌟 {girl_name}, तू एक star है! 🌟",
        f"❤️ {girl_name}, I LOVE YOU! ❤️"
    ]

    for romantic_msg in romantic_messages:
        try:
            await event.respond(romantic_msg)
            await asyncio.sleep(0.3)
        except:
            pass

    # STAGE 14: Grand Finale
    await asyncio.sleep(0.5)
    try:
        await event.respond(f"""╔════════════════════════════════╗
║  🌹🌹🌹🌹🌹🌹🌹🌹🌹  ║
║                                ║
║     💖 {girl_name} 💖        ║
║                                ║
║   YOU STOLE MY HEART! 😍       ║
║                                ║
║     From: RISHANT THAKUR 👑    ║
║                                ║
║  🌹🌹🌹🌹🌹🌹🌹🌹🌹  ║
╚════════════════════════════════╝

💕 BE MINE FOREVER! 💕""")
    except:
        pass

    # BONUS: Heart Rain
    await asyncio.sleep(0.7)
    heart_rain = f"""💖     💕     💗     💓
   💝     💘     💞
💖     💕     💗     💓
   💝     💘     💞
💖     💕     💗     💓

    {girl_name}
    
  YOU'RE AMAZING! ✨"""
  
    try:
        await event.respond(heart_rain)
    except:
        pass

# Register handlers for all clients
X1.on(events.NewMessage(incoming=True, pattern=r"^\.love$"))(love_handler)
X2.on(events.NewMessage(incoming=True, pattern=r"^\.love$"))(love_handler)
X3.on(events.NewMessage(incoming=True, pattern=r"^\.love$"))(love_handler)
X4.on(events.NewMessage(incoming=True, pattern=r"^\.love$"))(love_handler)
X5.on(events.NewMessage(incoming=True, pattern=r"^\.love$"))(love_handler)
X6.on(events.NewMessage(incoming=True, pattern=r"^\.love$"))(love_handler)
X7.on(events.NewMessage(incoming=True, pattern=r"^\.love$"))(love_handler)
X8.on(events.NewMessage(incoming=True, pattern=r"^\.love$"))(love_handler)
X9.on(events.NewMessage(incoming=True, pattern=r"^\.love$"))(love_handler)
X10.on(events.NewMessage(incoming=True, pattern=r"^\.love$"))(love_handler)