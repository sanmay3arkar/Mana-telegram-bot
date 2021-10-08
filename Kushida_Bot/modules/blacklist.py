from telegram import Bot
from telegram.ext import Updater

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

lst = {}

def adblklist(update,context):
	args = update.message.text.split(None, 1)
	chat = update.effective_chat
	user = update.effective_user
	
	if chat.type == 'private':
		update.message.reply_text('<b>I am really sorry! but this command only work on groups. add me on your group for using it! ;)</b>', parse_mode = 'html')
		return
	
	member = chat.get_member(user.id)
	if (not (member.status == 'administrator' or member.status == 'creator')):
		update.message.reply_text('<b>I am really sorry! but you dont have necessary rights to do that!. please become an admin first.</b>', parse_mode = 'html')
		return 
	
	if len(args) < 2:
		try:
			text = update.message.reply_to_message.text
		except:
			update.message.reply_text('<b>For using this command you have to send it on a reply of someones previous message. otherwise send it like this👇</b>\n\n🔹/adblklist (<code>Your Word</code>)🔹\n\n<b>Dont use brakets its just for showing. please try again😊</b>', parse_mode = 'html')
			return
	else:
		text = args[1]
	
	if text == None:
		update.message.reply_text("<b>I am really sorry. but None type object or media cant be added to blacklist. Please Try again😊</b>", parse_mode = 'html')
		return
	
	if chat.id not in lst.keys():
		lst[chat.id] = []
		lst[chat.id].append(text)
	elif text in lst[chat.id]:
		update.message.reply_text('<b>This text has been already added to the Blacklist. please try a new text.</b>', parse_mode = 'html')
		return 
	else:
		lst[chat.id].append(text)
	
	update.message.reply_text("<b>The text</b> [<code>{}</code>]\n <b>has been successfully added to the blacklist✅.</b>".format(text), parse_mode = 'html')

def blklist(update,context):
	user = update.effective_user
	chat = update.effective_chat
	
	if chat.type == 'private':
		update.message.reply_text('<b>I am really sorry! but this command only work on groups. add me on your group for using it! ;)</b>', parse_mode = 'html')
		return
	
	member = chat.get_member(user.id)
	
	if (not (member.status == 'administrator' or member.status == 'creator')):
		update.message.reply_text('<b>I am really sorry! but you dont have necessary rights to view it!. please become an admin first.</b>', parse_mode = 'html')
		return 
	
	if chat.id not in lst.keys():
		update.message.reply_text("<b>There are not blacklist word added on this chat.</b>", parse_mode = 'html')
		return 
	
	elif lst[chat.id] == []:
		update.message.reply_text("<b>There are not blacklist word added on this chat.</b>", parse_mode = 'html')
		return 
		
	else:
		text = ''
		for word in lst[chat.id]:
			text = text + '🔹' + word + '\n'
	
	update.message.reply_text("<b>Blacklisted words of\n🔹{}🔹</b>\n\n<code>{}</code>".format(chat.title, text), parse_mode = 'html')

def rmblklist(update,context):
	args = update.message.text.split(None,1)
	user = update.effective_user
	chat = update.effective_chat
	
	if chat.type == 'private':
		update.message.reply_text('<b>I am really sorry but this command only work on groups. add me on your group for try this. ;)</b>', parse_mode = 'html')
		return 
	
	member = chat.get_member(user.id)
	
	if (not (member.status == 'administrator' or member.status == 'creator')):
		update.message.reply_text('<b>I am really sorry! but you dont have necessary rights to do that!. please become an admin first.</b>', parse_mode = 'html')
		return 
	
	if len(args) < 2:
		update.message.reply_text('<b>For using this command you have to send it like this👇</b>\n\n🔹/rmblklist (<code>Your Word</code>🔹\n\n<b>Dont use brakets its just for showing. Please try again</b>', parse_mode = 'html')
		return 
	
	if chat.id not in lst.keys():
		update.message.reply_text("<b>i am really sorry but this world isnt added to the black list.</b>", parse_mode = 'html')
		return
	
	if args[1] not in lst[chat.id]:
		update.message.reply_text('<b>i am really sorry but this word not available on blacklist</b> ', parse_mode = 'html')
		return 
	
	try:
		lst[chat.id].remove(args[1])
		update.message.reply_text("<b>Word</b>[<code>{}</code>]\n<b>Has been successfully removed from blacklist</b>".format(args[1]), parse_mode = 'html')
	except:
		update.message.reply_text("<b>I am really sorry! i cant remove this word from blacklist. Please re check your word otherwise try again later</b>", parse_mode = 'html')
		return 