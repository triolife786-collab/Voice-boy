import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Yahan apna naya testing bot token daal dena
TOKEN = "8939709568:AAFjf5rBuGe5bhyPnVGd66TWyBZRQUNJegA"

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.voice:
        file_id = update.message.voice.file_id
        await update.message.reply_text(f"Voice ID:\n`{file_id}`", parse_mode="Markdown")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.VOICE, get_id))

    print("Bot started...")
    application.run_polling()

if __name__ == '__main__':
    main()
