from telethon import events
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS
import asyncio

# ============ LEGEND ANIMATION COMMAND ============

@X1.on(events.NewMessage(incoming=True, pattern=r"\.legend"))
@X2.on(events.NewMessage(incoming=True, pattern=r"\.legend"))
@X3.on(events.NewMessage(incoming=True, pattern=r"\.legend"))
@X4.on(events.NewMessage(incoming=True, pattern=r"\.legend"))
@X5.on(events.NewMessage(incoming=True, pattern=r"\.legend"))
@X6.on(events.NewMessage(incoming=True, pattern=r"\.legend"))
@X7.on(events.NewMessage(incoming=True, pattern=r"\.legend"))
@X8.on(events.NewMessage(incoming=True, pattern=r"\.legend"))
@X9.on(events.NewMessage(incoming=True, pattern=r"\.legend"))
@X10.on(events.NewMessage(incoming=True, pattern=r"\.legend"))
async def legend_animation(event):
    if event.sender_id not in SUDO_USERS:
        return
    
    await event.delete()
    
    # STAGE 1: Warning Sirens
    animation_frames = [
        "🚨",
        "🚨🚨",
        "🚨🚨🚨",
        "🚨🚨🚨🚨",
        "🚨🚨🚨🚨🚨",
        "⚠️ WARNING ⚠️",
        "⚠️⚠️ ALERT ⚠️⚠️",
        "⚠️⚠️⚠️ DANGER ⚠️⚠️⚠️",
    ]
    
    msg = await event.respond("🚨")
    for frame in animation_frames:
        await asyncio.sleep(0.3)
        await msg.edit(frame)
    
    await asyncio.sleep(0.5)
    
    # STAGE 2: System Initialization
    await msg.edit("```\n⚙️ INITIALIZING SYSTEM...\n[▓▓░░░░░░░░] 20%```")
    await asyncio.sleep(0.4)
    await msg.edit("```\n⚙️ INITIALIZING SYSTEM...\n[▓▓▓▓░░░░░░] 40%```")
    await asyncio.sleep(0.4)
    await msg.edit("```\n⚙️ INITIALIZING SYSTEM...\n[▓▓▓▓▓▓░░░░] 60%```")
    await asyncio.sleep(0.4)
    await msg.edit("```\n⚙️ INITIALIZING SYSTEM...\n[▓▓▓▓▓▓▓▓░░] 80%```")
    await asyncio.sleep(0.4)
    await msg.edit("```\n⚙️ INITIALIZING SYSTEM...\n[▓▓▓▓▓▓▓▓▓▓] 100%\n\n✅ SYSTEM READY!```")
    
    await asyncio.sleep(0.5)
    
    # STAGE 3: Scanning
    await msg.edit("```\n🔍 SCANNING DATABASE...\n>>> Searching for LEGENDS...```")
    await asyncio.sleep(0.6)
    await msg.edit("```\n🔍 SCANNING DATABASE...\n>>> Analyzing 10000 records...\n>>> Processing...```")
    await asyncio.sleep(0.6)
    await msg.edit("```\n🔍 SCANNING DATABASE...\n>>> Match found!\n>>> Loading profile...```")
    
    await asyncio.sleep(0.5)
    
    # STAGE 4: Building Name Animation
    name_animation = [
        "R",
        "RI",
        "RIS",
        "RISH",
        "RISHA",
        "RISHAN",
        "RISHANT",
        "RISHANT ",
        "RISHANT T",
        "RISHANT TH",
        "RISHANT THA",
        "RISHANT THAK",
        "RISHANT THAKU",
        "RISHANT THAKUR"
    ]
    
    for frame in name_animation:
        await asyncio.sleep(0.15)
        await msg.edit(f"```\n⚡ LOADING...\n\n>>> {frame}_```")
    
    await asyncio.sleep(0.5)
    
    # STAGE 5: Epic Reveal
    reveal_frames = [
        "💥",
        "💥💥",
        "💥💥💥",
        """
💥💥💥💥💥
    
    LOADING...
    
💥💥💥💥💥
""",
        """
⚡⚡⚡⚡⚡⚡⚡
    
  RISHANT THAKUR
    
⚡⚡⚡⚡⚡⚡⚡
""",
    ]
    
    for frame in reveal_frames:
        await asyncio.sleep(0.4)
        await msg.edit(frame)
    
    await asyncio.sleep(0.7)
    
    # STAGE 6: Power Level Rising
    await msg.edit("```\n⚠️ POWER LEVEL DETECTING...\n\n█░░░░░░░░░ 10%```")
    await asyncio.sleep(0.3)
    await msg.edit("```\n⚠️ POWER LEVEL DETECTING...\n\n████░░░░░░ 40%```")
    await asyncio.sleep(0.3)
    await msg.edit("```\n⚠️ POWER LEVEL DETECTING...\n\n███████░░░ 70%```")
    await asyncio.sleep(0.3)
    await msg.edit("```\n⚠️ POWER LEVEL DETECTING...\n\n██████████ 100%\n\n🚨 WARNING: POWER LEVEL EXCEEDED!```")
    
    await asyncio.sleep(0.6)
    
    # STAGE 7: Stats Display
    stats_animation = [
        """
📊 PROFILE STATS
━━━━━━━━━━━━━━
Name: LOADING...
""",
        """
📊 PROFILE STATS
━━━━━━━━━━━━━━
Name: RISHANT THAKUR
Power: LOADING...
""",
        """
📊 PROFILE STATS
━━━━━━━━━━━━━━
Name: RISHANT THAKUR
Power: ∞ UNLIMITED
Level: LOADING...
""",
        """
📊 PROFILE STATS
━━━━━━━━━━━━━━
Name: RISHANT THAKUR
Power: ∞ UNLIMITED
Level: GOD TIER
Status: LOADING...
""",
        """
📊 PROFILE STATS
━━━━━━━━━━━━━━
Name: RISHANT THAKUR
Power: ∞ UNLIMITED
Level: GOD TIER
Status: 👑 LEGEND 👑
"""
    ]
    
    for frame in stats_animation:
        await asyncio.sleep(0.5)
        await msg.edit(frame)
    
    await asyncio.sleep(0.8)
    
    # STAGE 8: ASCII Art Animation
    ascii_frames = [
        """
    ⠀⠀⠀⢀⣀⣀⣀⠀⠀
    ⠀⠀⣴⣿⣿⣿⣿⣷⠀
    ⠀⠀⣿⣿⣿⣿⣿⣿⡀
    ⠀⠀⠙⠿⠿⠿⠿⠋⠀
    
    LOADING...
""",
        """
    ⠀⠀⢀⣴⣶⣶⣦⡀⠀
    ⠀⢠⣿⣿⣿⣿⣿⣿⡄
    ⠀⢸⣿⣿⣿⣿⣿⣿⡇
    ⠀⠈⠻⢿⣿⣿⡿⠟⠁
    
    ⚡ RISHANT ⚡
""",
        """
    ⠀⣠⣾⣿⣿⣿⣿⣷⣄
    ⢰⣿⣿⣿⣿⣿⣿⣿⣿
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿
    ⠈⠻⣿⣿⣿⣿⣿⠟⠁
    
    👑 THAKUR 👑
"""
    ]
    
    for frame in ascii_frames:
        await asyncio.sleep(0.5)
        await msg.edit(frame)
    
    await asyncio.sleep(0.7)
    
    # STAGE 9: Explosion Effect
    explosion = [
        "💥",
        "💥💥💥",
        "💥💥💥💥💥",
        """
💥💥💥💥💥💥💥
💥💥💥💥💥💥💥
💥💥💥💥💥💥💥
""",
        """
🔥🔥🔥🔥🔥🔥🔥
🔥🔥🔥🔥🔥🔥🔥
🔥🔥🔥🔥🔥🔥🔥
    
  ULTIMATE POWER!
"""
    ]
    
    for frame in explosion:
        await asyncio.sleep(0.3)
        await msg.edit(frame)
    
    await asyncio.sleep(0.8)
    
    # STAGE 10: FINAL REVEAL - EPIC!
    final_message = """
╔═══════════════════════════╗
║                           ║
║    ⚡ LEGEND DETECTED ⚡    ║
║                           ║
╚═══════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 Name: RISHANT THAKUR

🏆 Title: THE ULTIMATE LEGEND

⚡ Power Level: ∞ UNLIMITED

💪 Strength: MAXIMUM

🧠 Intelligence: GENIUS

😎 Coolness: OFF THE CHARTS

🔥 Danger Level: EXTREME

━━━━━━━━━━━━━━━━━━━━━━━━━━

🌟 ACHIEVEMENTS:
  ✅ Undefeated Champion
  ✅ King of Kings
  ✅ God Tier Level
  ✅ Most Feared Legend
  ✅ Supreme Commander

━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ WARNING ⚠️
This person is TOO POWERFUL!
Approach with EXTREME caution!

━━━━━━━━━━━━━━━━━━━━━━━━━━

👑 RISHANT THAKUR 👑
THE ONE AND ONLY LEGEND!

🔥 RESPECT THE KING 🔥
"""
    
    await msg.edit(final_message)
    
    await asyncio.sleep(2)
    
    # STAGE 11: Final Fireworks
    fireworks = [
        "🎆",
        "🎆🎆🎆",
        "🎆🎆🎆🎆🎆",
        """
🎆🎆🎆🎆🎆🎆🎆
    
RISHANT THAKUR
THE LEGEND!
    
🎆🎆🎆🎆🎆🎆🎆
""",
        """
🎉🎉🎉🎉🎉🎉🎉
👑 LEGEND CONFIRMED 👑
🎉🎉🎉🎉🎉🎉🎉
"""
    ]
    
    for frame in fireworks:
        await asyncio.sleep(0.4)
        await msg.edit(frame)
    
    # BONUS: Spam Effect
    await asyncio.sleep(1)
    
    spam_messages = [
        "⚡ RISHANT THAKUR ⚡",
        "👑 THE KING 👑",
        "🔥 UNSTOPPABLE 🔥",
        "💪 UNBEATABLE 💪",
        "😎 LEGENDARY 😎",
        "🌟 SUPREME 🌟",
        "💥 POWERFUL 💥",
        "🏆 CHAMPION 🏆"
    ]
    
    for spam_msg in spam_messages:
        await event.respond(spam_msg)
        await asyncio.sleep(0.2)
    
    # Final Epic Message
    await asyncio.sleep(0.5)
    await event.respond("""
╔════════════════════════════╗
║  ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡  ║
║                            ║
║   🔥 RISHANT THAKUR 🔥    ║
║                            ║
║      👑 LEGEND 👑          ║
║                            ║
║  ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡  ║
╚════════════════════════════╝

💀 FEAR THE LEGEND! 💀
""")