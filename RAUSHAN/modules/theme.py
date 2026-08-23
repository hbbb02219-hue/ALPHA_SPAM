from telethon import Button


# =========================
# 🌈 ALPHA COLOR THEME
# =========================

COLORS = {
    "success": "🟢",
    "error": "🔴",
    "warning": "🟡",
    "info": "🔵",
    "admin": "🟣",
    "love": "🩷",
    "important": "🟠",
    "cool": "🩵",
    "normal": "⚪",
}


def theme_message(text, color="info"):
    emoji = COLORS.get(color, COLORS["info"])

    return (
        f"{emoji} **rishant • {color.upper()}**\n"
        f"━━━━━━━━━━━━━━━━━━\n\n"
        f"{text}\n\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"✨ **rishant SPAM**"
    )


def success(text):
    return theme_message(text, "success")


def error(text):
    return theme_message(text, "error")


def warning(text):
    return theme_message(text, "warning")


def info(text):
    return theme_message(text, "info")


def admin(text):
    return theme_message(text, "admin")


def love(text):
    return theme_message(text, "love")


def important(text):
    return theme_message(text, "important")


# =========================
# 🌈 COLORFUL BUTTONS
# =========================

def colorful_buttons():
    return [
        [
            Button.inline("🟢 • COMMANDS •", data="help_back"),
        ],
        [
            Button.url("🔵 • CHANNEL •", "https://t.me/ganaasupport"),
            Button.url("🟣 • SUPPORT •", "https://t.me/ganaasupport"),
        ],
        [
            Button.url("🟠 • REPOSITORY •", "https://t.me/ganaasupport"),
        ],
    ]