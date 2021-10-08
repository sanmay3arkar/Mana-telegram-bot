'''from telegram import Bot
from telegram.ext import Updater, dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from Kushida_Bot.modules import console

bot = Bot("1759027838:AAFy9NjdgPUryqK0cuRQrelpCnghyxn5uEU")

updates = Updater("1759027838:AAFy9NjdgPUryqK0cuRQrelpCnghyxn5uEU", use_context = True)

updates.dispatcher.add_handler(CommandHandler('afk', console.afk))
updates.dispatcher.add_handler(MessageHandler(Filters.all, console.tuser))

updates.start_polling()'''