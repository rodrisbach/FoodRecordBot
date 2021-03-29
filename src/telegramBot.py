from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    CallbackContext,
    ConversationHandler,
    MessageHandler,
    Filters,
)
import os


OPTIONS, FOOD, FIRST_DATE, LAST_DATE = range(4)

def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Record food", callback_data="Record food"),
            InlineKeyboardButton("Download PDF", callback_data="Download PDF"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose an option:', reply_markup=reply_markup)
    return OPTIONS

def creatingPDF(update, context):
    query = update.callback_query
    bot = context.bot
    bot.edit_message_text(
       chat_id=query.message.chat_id,
       message_id=query.message.message_id,
       text="Creating PDF"
    )

def showDays(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Monday", callback_data="Monday"),
            InlineKeyboardButton("Tuesday", callback_data="Tuesday"),
            InlineKeyboardButton("Wednesday", callback_data="Wednesday"),
            InlineKeyboardButton("Thursday", callback_data="Thursday"),
            InlineKeyboardButton("Friday", callback_data="Friday"),
            InlineKeyboardButton("Saturday", callback_data="Saturday"),
            InlineKeyboardButton("Sunday", callback_data="Sunday"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    bot = context.bot
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Choose a day:",
        reply_markup=reply_markup
    )
    return FOOD

def writeFoodMessage(update, context):
    query = update.callback_query
    bot = context.bot
    query.answer()
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f"Write your food record"
    )

def cancel(update, context):
    update.message.reply_text('Adios')
    return ConversationHandler.END

def main():
    TOKEN = os.getenv('TOKEN')
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={
            OPTIONS: [
                CallbackQueryHandler(showDays,pattern='^Record food'),
                CallbackQueryHandler(creatingPDF,pattern='^Download PDF')
            ],
            FOOD: [
                CallbackQueryHandler(writeFoodMessage,pattern='^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)$'),

            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
