# main.py

from telegram.ext import Updater, CommandHandler
import os
from keep_alive import keep_alive

def start(update, context):
    update.message.reply_text("✅ Hello! MEV bot is alive.")

def main():
    # Start keep_alive server
    keep_alive()

    # Get token from environment
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN not set")
        return

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))

    # Start polling and keep the bot running
    print("🚀 Bot started...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"🔥 ERROR: {e}")

