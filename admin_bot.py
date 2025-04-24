
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "YOUR_ADMIN_BOT_TOKEN"

async def notify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📩 New form submitted!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("notify", notify))
    app.run_polling()
