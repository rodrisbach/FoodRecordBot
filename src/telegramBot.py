from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import os

def showDays(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Lunes", callback_data="LU"),
            InlineKeyboardButton("Martes", callback_data="MA"),
            InlineKeyboardButton("Miercoles", callback_data="MI"),
            InlineKeyboardButton("Jueves", callback_data="JU"),
            InlineKeyboardButton("Viernes", callback_data="VI"),
            InlineKeyboardButton("Sabado", callback_data="SA"),
            InlineKeyboardButton("Domingo", callback_data="DO"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def chooseDay(update, context):
    days = {
            "LU": "Lunes",
            "MA": "Martes",
            "MI": "Miercoles",
            "JU": "Jueves",
            "VI": "Viernes",
            "SA": "Sabado",
            "DO": "Domingo",
            }
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"El dia seleccionado es: {days[query.data]}")

def main():
    TOKEN = os.getenv('TOKEN')
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start',showDays))
    dispatcher.add_handler(CallbackQueryHandler(chooseDay))
    updater.start_polling()


    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start')]
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
