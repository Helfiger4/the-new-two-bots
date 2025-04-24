from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7501309246:AAGUougXq-AHc48E0D0ChkSLtm6NRMQ2kYg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎓 Программы!", callback_data="programs")],
        [InlineKeyboardButton("📝 Заявка!", url="https://thenewtwo.netlify.app/study.html")],
        [InlineKeyboardButton("💬 Задать вопрос!", url="https://t.me/AskTheNewTwo")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите, что вас интересует:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "programs":
        keyboard = [[InlineKeyboardButton("Malta", callback_data="malta")]]
        await query.edit_message_text("Выберите страну:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "malta":
        keyboard = [[InlineKeyboardButton("LSCM", callback_data="lscm")]]
        await query.edit_message_text("Выберите школу:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "lscm":
        keyboard = [
            [InlineKeyboardButton("English", url="https://lscmalta.edu.mt/courses/academic-english/")],
            [InlineKeyboardButton("MBA", url="https://lscmalta.edu.mt/courses/master-of-business-administration/")],
            [InlineKeyboardButton("Bachelor", url="https://lscmalta.edu.mt/courses/bachelor-with-honours-in-business/")]
        ]
        await query.edit_message_text("Выберите курс:", reply_markup=InlineKeyboardMarkup(keyboard))

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
