

from telegram.ext import Updater, CommandHandler
import os
from keep_alive import keep_alive

def start(update, context):
    update.message.reply_text("✅ Hello! MEV bot is alive.")

def main():
    keep_alive()

    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN not set")
        return

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    print("🚀 Bot started...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"🔥 ERROR: {e}")
