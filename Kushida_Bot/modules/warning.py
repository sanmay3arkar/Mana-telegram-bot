from telegram import Bot
from telegram.ext import Updater
import random
from Kushida_Bot.modules.helper_function.list_dict import WARN
from telegram.utils.helpers import mention_html

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

def warn(update,context):
	args = update.message.text.split(None, 1)
	user = update.effective_user
	chat = update.effective_chat
	
	if chat.type == 'private':
		update.message.reply_text("<b>I am really sorry this command only works on groups. add me on your group for trying this. ;)</b>", parse_mode = 'html')
		return 
	
	member = chat.get_member(user.id)
	
	if (not (member.status == 'administrator' or member.status == 'creator')):
		update.message.reply_text('<b>I am really sorry! but you dont have necessary rights to do that!. please become an admin first.</b>', parse_mode = 'html')
		return 
	
	try:
		user_id = update.message.reply_to_message.from_user
		msg = update.message.reply_to_message.message_id
	except:
		update.message.reply_text("<b>For Using this command you have to send this command on a reply of someones previous message. otherwise it wont work. Please Try again😊</b>", parse_mode = 'html')
		return 
	
	member1 = chat.get_member(user_id.id)
	if member1.status == 'administrator':
		update.message.reply_text("<b>I cant warn Admins on this group. Whats wrong with you?</b>", parse_mode = 'html')
		return 
	elif member1.status == 'creator':
		update.message.reply_text("<b>How can i warn a person who created this group? be more careful already!</b>", parse_mode = 'html')
		return
	elif user_id.id == bot.id:
		update.message.reply_text("<b>WoW warn myself. What do you think i have mental issues to doing it ;)</b>", parse_mode = 'html')
		return
	elif not user_id:
		update.message.reply_text('<b>I am not sure this user even exist!</b>', parse_mode = 'html')
		return
	
	if len(args) < 2:
		update.message.reply_text("<b>⚠️WARNING⚠️\n\n‼️User {}‼️\n\n{}</b>".format(mention_html(user_id.id, user_id.first_name), random.choice(WARN)), parse_mode = 'html', reply_to_message_id = msg, disable_web_page_preview = True)
	else:
		update.message.reply_text("<b>⚠️WARNING⚠️\n\n‼️User : {}‼️\n\nMessage From Admin : </b><i>{}</i>".format(mention_html(user_id.id, user_id.first_name), args[1]), parse_mode = 'html', reply_to_message_id = msg, disable_web_page_preview = True)
		

def report(update,context):
	chat = update.effective_chat
	if chat.type == 'private':
		update.message.reply_text("<b>I am really sorry but this command only work on groups. add me on your group to try this ;)</b>", parse_mode = 'html')
		return
	args = update.message.text.split(None, 1)
	try:
		user = update.message.reply_to_message.from_user
	except:
		update.message.reply_text("<b>I am really sorry. but for using this command you have to send this on a reply of someones previous message.\n\nOr you can send it on reply like this too👇\n\n/report (<code>Report Reason</code>)\n\nplease try again😊</b>", parse_mode = 'html')
		return
	txt = ''
		
	for adm in bot.get_chat_administrators(chat.id):
		m_user = adm.user
		txt += mention_html(m_user.id,'​')
	
	if len(args) < 2:
		update.message.reply_text("<b>User: {}‼️\nID:</b><code>{}</code>\n\n<b>Has been Successfully reported to admins✅</b>{}.".format(mention_html(user.id, user.first_name), user.id, txt), parse_mode = 'html')
	else:
		update.message.reply_text("<b>User: {}‼️\nID:</b><code>{}</code>\n\n<b>Has been Successfully reported to admins✅\n\nReason: </b><i>{}</i>{}.".format(mention_html(user.id, user.first_name), user.id,args[1], txt), parse_mode = 'html')