from telegram import Bot, ParseMode
from telegram.ext import Updater, DispatcherHandlerStop
import random as r
from Kushida_Bot.modules.helper_function import list_dict as l_file
import html

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)
			
afk_dict = {1:1}

def afk(update,context):
	args = update.message.text.split(None, 1)
	user = update.message.from_user
	
	if len(args) >= 2:
		afk_dict[user.id] = args[1]
		update.message.reply_text(r.choice(l_file.AWAY).format(user['first_name']))
	else:
		afk_dict[user.id] = " "
		update.message.reply_text(r.choice(l_file.AWAY).format(user['first_name']))

def return_afk(update,context):
	user = update.message.from_user
	if user.id in afk_dict.keys():
		update.message.reply_text(r.choice(l_file.BACK_AFK).format(user['first_name']))
		afk_dict.pop(user.id)
	try:
		reply = update.message.reply_to_message.from_user
	except:
		return 
	
	if reply.id in afk_dict.keys():
		if user.id in afk_dict.keys():
			update.message.reply_text(r.choice(l_file.BACK_AFK).format(reply['first_name']))
		else:
			if afk_dict[reply.id] == ' ':
				update.message.reply_text(r.choice(l_file.REPLY_AWAY).format(reply['first_name']))
			else:
				res = r.choice(l_file.REPLY_AWAY) + "afk reason: <code>{}</code>"
				res1 = res.format(reply['first_name'], html.escape(afk_dict[reply.id]))
				update.message.reply_text(res1, parse_mode = "html")	