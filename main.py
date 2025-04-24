
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7501309246:AAGUougXq-AHc48E0D0ChkSLtm6NRMQ2kYg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎓 Программы!", callback_data="programs")],
        [InlineKeyboardButton("📝 Заявка!", url="https://cheerful-twilight-d5bb87.netlify.app/study_request_form.html")],
        [InlineKeyboardButton("💬 Задать вопрос!", url="https://t.me/AskTheNewTwo")]
    ]
    await update.message.reply_text("👋 Добро пожаловать в TheNewTwo!\nВыберите, что вас интересует:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "programs":
        keyboard = [[InlineKeyboardButton("🇲🇹 Malta", callback_data="malta")]]
        await query.edit_message_text("🌐 Страны:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "malta":
        keyboard = [[InlineKeyboardButton("🏫 LSCM", callback_data="lscm")]]
        await query.edit_message_text("🏫 Учебные заведения в Мальте:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "lscm":
        keyboard = [
            [InlineKeyboardButton("🇬🇧 English", url="https://lscmalta.edu.mt/courses/academic-english/")],
            [InlineKeyboardButton("🎓 MBA", url="https://lscmalta.edu.mt/courses/master-of-business-administration/")],
            [InlineKeyboardButton("🎓 Bachelor", url="https://lscmalta.edu.mt/courses/bachelor-with-honours-in-business/")]
        ]
        await query.edit_message_text("📚 Программы в LSCM:", reply_markup=InlineKeyboardMarkup(keyboard))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()
