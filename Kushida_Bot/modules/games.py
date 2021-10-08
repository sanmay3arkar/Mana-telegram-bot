from telegram import Bot, ParseMode
from telegram.ext import Updater
import random
from Kushida_Bot.modules.helper_function import g_list
import time

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

def toss(update,context):
	m = update.message.reply_text('*🧩Flipping the coin🪙...*', parse_mode=ParseMode.MARKDOWN)
	for i in range(2):
		time.sleep(1)
	m.edit_text('<b>Result is 🔹<code>{}</code>🔹</b>'.format(random.choice(g_list.TOSS)), parse_mode = 'html')

def dice(update,context):
	m = update.message.reply_text('<b>🧩Rolling the Dice🎲...</b>', parse_mode = 'html')
	for i in range(1):
		time.sleep(1)
	m.edit_text('<b>🎲🎲🎲Roool...</b>', parse_mode = 'html')
	for i in range(2):
		time.sleep(1)
	m.edit_text('<b>Result is 🔹<code>{}</code>🔹</b>'.format(random.choice(g_list.DICE)), parse_mode = 'html')

def truth(update,context):
	m = update.message.reply_text('*Thinking a Question🤔...*', parse_mode = ParseMode.MARKDOWN)
	
	for i in range(3):
		time.sleep(0.6)
		
	m.edit_text('<b>🔽Your Question is🔽\n\n🔹{}🔹\n\n Make Sure you tell the truth😉</b>'.format(random.choice(g_list.TRUTH)), parse_mode = 'html')

def dare(update,context):
	m = update.message.reply_text('*Thinking What should i tell you do🤔...*', parse_mode = ParseMode.MARKDOWN)
	
	for i in range(3):
		time.sleep(0.6)
		
	m.edit_text('<b>🔽Here your Work🔽\n\n🔹{}🔹\n\nNo Escaping You have to do this😁</b>'.format(random.choice(g_list.DARE)), parse_mode = 'html')