
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

TOKEN = "8177328605:AAFOuntR5Cn0D87a1iUGplsnBB3jPo8CXbg"
CHANNEL_ID = "@TheNewTwo"

last_post_id = None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📢 Привет! Отправь мне сообщение (текст, фото или файл) — и я опубликую его в канале.")

async def post_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_post_id
    if update.message.text:
        msg = await context.bot.send_message(chat_id=CHANNEL_ID, text=update.message.text)
    elif update.message.photo:
        msg = await context.bot.send_photo(chat_id=CHANNEL_ID, photo=update.message.photo[-1].file_id, caption=update.message.caption or "")
    elif update.message.document:
        msg = await context.bot.send_document(chat_id=CHANNEL_ID, document=update.message.document.file_id, caption=update.message.caption or "")
    else:
        await update.message.reply_text("❗ Я могу публиковать только текст, фото или документы.")
        return
    last_post_id = msg.message_id
    keyboard = [[InlineKeyboardButton("📌 Закрепить", callback_data="pin")], [InlineKeyboardButton("🗑 Удалить", callback_data="delete")]]
    await update.message.reply_text("✅ Опубликовано. Что дальше?", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_post_id
    query = update.callback_query
    await query.answer()
    if query.data == "pin" and last_post_id:
        await context.bot.pin_chat_message(chat_id=CHANNEL_ID, message_id=last_post_id)
        await query.edit_message_text("📌 Пост закреплён.")
    elif query.data == "delete" and last_post_id:
        await context.bot.delete_message(chat_id=CHANNEL_ID, message_id=last_post_id)
        await query.edit_message_text("🗑 Пост удалён.")
        last_post_id = None
    else:
        await query.edit_message_text("⚠️ Нет последнего поста для действия.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), post_to_channel))
    app.run_polling()
