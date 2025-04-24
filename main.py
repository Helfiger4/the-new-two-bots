
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "YOUR_USER_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎓 Программы!", callback_data="programs")],
        [InlineKeyboardButton("📝 Заявка!", callback_data="request")],
        [InlineKeyboardButton("💬 Задать вопрос!", callback_data="question")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Что вас интересует:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "programs":
        keyboard = [[InlineKeyboardButton("Malta", callback_data="malta")]]
        await query.edit_message_text("Выберите страну:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "malta":
        keyboard = [
            [InlineKeyboardButton("English", url="https://lscmalta.edu.mt/courses/academic-english/")],
            [InlineKeyboardButton("MBA", url="https://lscmalta.edu.mt/courses/master-of-business-administration/")],
            [InlineKeyboardButton("Bachelor", url="https://lscmalta.edu.mt/courses/bachelor-with-honours-in-business/")]
        ]
        await query.edit_message_text("Выберите курс:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "request":
        await query.edit_message_text("Заполните форму: https://thenewtwo.netlify.app/study_request_form.html")
    elif query.data == "question":
        await query.edit_message_text("Задайте вопрос: https://t.me/AskTheNewTwo")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()
