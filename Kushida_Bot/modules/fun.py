from Kushida_Bot.modules.helper_function import fun_dict as f
from telegram import Bot, ParseMode
from telegram.ext import Updater
import random as r


bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

def weebify(update,context):
	m_args = update.message.text.lower()
	args = m_args.split(None, 1)
	if len(args) < 2:
		try:
			message = update.message.reply_to_message.text.lower()
			x = ''
			for i in message:
				if i == 'a':
					x = x + f.WEEBIFY[0]
				elif i == 'b':
					x = x + f.WEEBIFY[1]
				elif i == 'c':
					x = x + f.WEEBIFY[2]
				elif i == 'd':
					x = x + f.WEEBIFY[3]
				elif i == 'e':
					x = x + f.WEEBIFY[4]
				elif i == 'f':
					x = x + f.WEEBIFY[5]
				elif i == 'g':
					x = x + f.WEEBIFY[6]
				elif i == 'h':
					x = x + f.WEEBIFY[7]
				elif i == 'i':
					x = x + f.WEEBIFY[8]
				elif i == 'j':
					x = x + f.WEEBIFY[9]
				elif i == 'k':
					x = x + f.WEEBIFY[10]
				elif i == 'l':
					x = x + f.WEEBIFY[11]
				elif i == 'm':
					x = x + f.WEEBIFY[12]
				elif i == 'n':
					x = x + f.WEEBIFY[13]
				elif i == 'o':
					x = x + f.WEEBIFY[14]
				elif i == 'p':
					x = x + f.WEEBIFY[15]
				elif i == 'q':
					x = x + f.WEEBIFY[16]
				elif i == 'r':
					x = x + f.WEEBIFY[17]
				elif i == 's':
					x = x + f.WEEBIFY[18]
				elif i == 't':
					x = x + f.WEEBIFY[19]
				elif i == 'u':
					x = x + f.WEEBIFY[20]
				elif i == 'v':
					x = x + f.WEEBIFY[21]
				elif i == 'w':
					x = x + f.WEEBIFY[22]
				elif i == 'x':
					x = x + f.WEEBIFY[23]
				elif i == 'y':
					x = x + f.WEEBIFY[24]
				elif i == 'z':
					x = x + f.WEEBIFY[25]
				else:
					x = x + i
			update.message.reply_text('<b>{}</b>'.format(x), parse_mode = 'html')
		except:
			update.message.reply_text("<b>For using this command you have to send it on a reply. otherwise send it like this👇</b>\n\n🔹/weebify (<code>Your Text</code>)🔹\n\n<b>Please Try Again😊</b>", parse_mode = 'html')
	else:
		x = ''
		for i in args[1]:
			if i == 'a':
				x = x + f.WEEBIFY[0]
			elif i == 'b':
				x = x + f.WEEBIFY[1]
			elif i == 'c':
				x = x + f.WEEBIFY[2]
			elif i == 'd':
				x = x + f.WEEBIFY[3]
			elif i == 'e':
				x = x + f.WEEBIFY[4]
			elif i == 'f':
				x = x + f.WEEBIFY[5]
			elif i == 'g':
				x = x + f.WEEBIFY[6]
			elif i == 'h':
				x = x + f.WEEBIFY[7]
			elif i == 'i':
				x = x + f.WEEBIFY[8]
			elif i == 'j':
				x = x + f.WEEBIFY[9]
			elif i == 'k':
				x = x + f.WEEBIFY[10]
			elif i == 'l':
				x = x + f.WEEBIFY[11]
			elif i == 'm':
				x = x + f.WEEBIFY[12]
			elif i == 'n':
				x = x + f.WEEBIFY[13]
			elif i == 'o':
				x = x + f.WEEBIFY[14]
			elif i == 'p':
				x = x + f.WEEBIFY[15]
			elif i == 'q':
				x = x + f.WEEBIFY[16]
			elif i == 'r':
				x = x + f.WEEBIFY[17]
			elif i == 's':
				x = x + f.WEEBIFY[18]
			elif i == 't':
				x = x + f.WEEBIFY[19]
			elif i == 'u':
				x = x + f.WEEBIFY[20]
			elif i == 'v':
				x = x + f.WEEBIFY[21]
			elif i == 'w':
				x = x + f.WEEBIFY[22]
			elif i == 'x':
				x = x + f.WEEBIFY[23]
			elif i == 'y':
				x = x + f.WEEBIFY[24]
			elif i == 'z':
				x = x + f.WEEBIFY[25]
			else:
				x = x + i
		
		update.message.reply_text('<b>{}</b>'.format(x), parse_mode = 'html')

def decide(update,context):
	args = update.message.text.split(None,1)
	if len(args) < 2:
		try:
			message = update.message.reply_to_message.text
			update.message.reply_text(r.choice(f.DECIDE))
		except:
			update.message.reply_text("<b>What should i decide?, you haven't asked me any question. send this command to a reply otherwise send it like this👇</b>\n\n🔹/decide (<code>Your Question</code>🔹\n\n<b>Don't use brakets ;)</b>", parse_mode = 'html')	
	else:
		update.message.reply_text(r.choice(f.DECIDE))

def abuse(update,context):
	try:
		ids = update.message.reply_to_message.message_id
		update.message.reply_text(r.choice(f.ABUSE), reply_to_message_id = ids )
	except:
		update.message.reply_text("<b>Well! You haven't mentioned someone.\nSend it on a reply of someones previous sended message.</b>", parse_mode = 'html')

def slap(update,context):
	args = update.message.text.split(None, 1)
	user1 = update.effective_user.first_name
	if len(args) < 2:
		try:
			user2 = update.message.reply_to_message.from_user.first_name
			ids = update.message.reply_to_message.message_id
		except:
			user2 = user1
			user1 = bot.first_name
			ids = update.message.message_id
	else:
		user2 = args[1]
		ids = update.message.message_id
	
	hits = r.choice(f.HIT)
	throw = r.choice(f.THROW)
	item = r.choice(f.ITEMS)
	mes = r.choice(f.SLAP)
	reply = mes.format(user1 = user1, user2 = user2, hits = hits, item = item, throws = throw)
	
	try:
		update.message.reply_text(reply, parse_mode = ParseMode.HTML, reply_to_message_id = ids)
	except:
		update.message.reply_text("<b>Please Try again later.</b>", parse_mode = 'html')
		return

def pat(update,context):
	args = update.message.text.split(None,1)
	user1 = update.effective_user.first_name
	if len(args) < 2:
		try:
			user2 = update.message.reply_to_message.from_user.first_name
			ids = update.message.reply_to_message.message_id
		except:
			user2 = user1
			user1 = bot.first_name
			ids = update.message.message_id
	else:
		user2 = args[1]
		ids = update.message.message_id
	
	text = r.choice(f.PAT)
	mes = text.format(user1 = user1, user2 = user2)
	
	update.message.reply_animation(r.choice(f.GIFS), caption = '<b>{}</b>'.format(mes), parse_mode = ParseMode.HTML)

def shout(update,context):
	args = update.message.text.split(None,1)
	if len(args) < 2:
		try:
			texts = update.message.reply_to_message.text
		except:
			update.message.reply_text("<b>For Using this Command you have to send it on a reply. otherwise send it like this👇</b>\n\n🔹/shout (<code>Your Text</code>)🔹\n\n<b>Please Try Again😊</b>",parse_mode = 'html')
			return 
	else:
		texts = args[1]
	text = "".join(texts)
	result = []
	result.append(" ".join(list(text)))
	for pos, symbol in enumerate(text[1:]):
		result.append(symbol + " " + "  " * pos + symbol)
	result = list("\n".join(result))
	result[0] = text[0]
	result = "".join(result)
	
	try:
		update.message.reply_text('<code>{}</code>'.format(result), parse_mode = 'html')
	except:
		update.message.reply_text('<b>Something Wrong Heppen please try again after sometime</b>', parse_mode = 'html')