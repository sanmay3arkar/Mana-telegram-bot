from telegram import Bot, ParseMode
from telegram.ext import Updater
from telegram.error import BadRequest
from telegram.utils.helpers import mention_html
import time

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

def ban(update,context):
	chat = update.effective_chat
	user = update.effective_user.id
	if chat.type == 'private':
		update.message.reply_text("<b>Sorry but this command only work's on group's. Add me on your group to try this😊</b>", parse_mode = 'html')
		return 
	member = chat.get_member(user)
	if (not (member.status == 'administrator' or member.status == 'creator')):
		update.message.reply_text('*I am really Sorry. but you dont have necessary rights to do that.\n\nPlease become an admin first!*', parse_mode = ParseMode.MARKDOWN )
		return
	try:
		user_id = update.message.reply_to_message.from_user
	except:
		update.message.reply_text("<b>For using this command you have to send it on a reply someone's previous message. Otherwise it won't work\n\nPlease try again😊</b>", parse_mode = 'html')
		return
	if user_id.id == bot.id:
		update.message.reply_text('*WoW! Ban myself, Dumb Brilient ;)*', parse_mode = ParseMode.MARKDOWN )
		return
	prom = chat.get_member(user_id.id)
	if prom.status == 'administrator':
		update.message.reply_text("*I can't ban Admins be more careful already! :(*", parse_mode = ParseMode.MARKDOWN)
		return 
	if prom.status == 'creator':
		update.message.reply_text("*Well, Well! Going to ban the group creator, how funny it can be : |*", parse_mode = ParseMode.MARKDOWN)
		return 
	if not user_id:
		update.message.reply_text('*I am not sure this user even exist!*', parse_mode = ParseMode.MARKDOWN)
		return
	try:
		chat.get_member(user_id.id)
	except BadRequest as bdr:
		if bdr.message == 'User not found':
			update.message.reply_text("*Can't seem to find this person!*", parse_mode = ParseMode.MARKDOWN)
			return
		else:
			update.message.reply_text("*Can't find this user!*", parse_mode = ParseMode.MARKDOWN)
			return
	
	try:
		lnk = mention_html(user_id.id, user_id.first_name)
		chat.ban_member(user_id.id)
		update.message.reply_text('<b>{} Got his punishment!</b>'.format(lnk), parse_mode = 'html', disable_web_page_preview=True)
	except:
		update.message.reply_text('<b>Something wrong heppen!! plese try again later!</b>', parse_mode = 'html')

def tban(update,context):	
	args = update.message.text.split(None, 1)
	chat = update.effective_chat
	user = update.effective_user.id
	if chat.type == 'private':
		update.message.reply_text("<b>Sorry but this command only work's on group's. Add me on your group to try this😊</b>", parse_mode = 'html')
		return 
	member = chat.get_member(user)
	if (not (member.status == 'administrator' or member.status == 'creator')):
		update.message.reply_text('*I am really Sorry. but you dont have necessary rights to do that.\n\nPlease become an admin first!*', parse_mode = ParseMode.MARKDOWN )
		return
	try:
		user_id = update.message.reply_to_message.from_user
	except:
		update.message.reply_text("<b>For using this command you have to send it on a reply someone's previous message. Otherwise it won't work\n\nPlease try again😊</b>", parse_mode = 'html')
		return
	if user_id.id == bot.id:
		update.message.reply_text('*WoW! Ban myself, Dumb Brilient ;)*', parse_mode = ParseMode.MARKDOWN )
		return
	prom = chat.get_member(user_id.id)
	if prom.status == 'administrator':
		update.message.reply_text("*I can't ban Admins be more careful already! :(*", parse_mode = ParseMode.MARKDOWN)
		return 
	if prom.status == 'creator':
		update.message.reply_text("*Well, Well! Going to ban the group creator, how funny it can be : |*", parse_mode = ParseMode.MARKDOWN)
		return 
	if not user_id:
		update.message.reply_text('*I am not sure this user even exist!*', parse_mode = ParseMode.MARKDOWN)
		return
	try:
		chat.get_member(user_id.id)
	except BadRequest as bdr:
		if bdr.message == 'User not found':
			update.message.reply_text("*Can't seem to find this person!*", parse_mode = ParseMode.MARKDOWN)
			return
		else:
			update.message.reply_text("*Can't find this user!*", parse_mode = ParseMode.MARKDOWN)
			return
	if len(args) < 2:
		update.message.reply_text("<b>For using this command you have to send it Like this👇\n\n🔹/tban (<code>00 00 00</code>)🔹\n\nHere the first 2 zeros is day and second 2 zeros is hour and the third 2 zeros is minute. but don't use brakets its just for showing\n\nPlease try again😊</b>", parse_mode = 'html')
		return
	
	args1 = args[1].split()
	if len(args1) > 3:
		update.message.reply_text("<b>Invalid time entered! as correction you entered more then expected number or spaces. Please enter like this👇\n\n🔹/tban (<code>00 00 00</code>)🔹\n\nHere the first 2 zeros is day and second 2 zeros is hour and the third 2 zeros is minute. but don't use brakets its just for showing\n\nPlease try again😊</b>", parse_mode = 'html')
		return 
	if len(args1) < 3:
		update.message.reply_text("<b>Invalid time entered! as correction you entered less then expected number or spaces. Please enter like this👇\n\n🔹/tban (<code>00 00 00</code>)🔹\n\nHere the first 2 zeros is day and second 2 zeros is hour and the third 2 zeros is minute. but don't use brakets its just for showing\n\nPlease try again😊</b>", parse_mode = 'html')
		return
	if len(args1[0]) > 2:
		update.message.reply_text("<b>Invalid time entered! as correction you entered more then expected number on the ‘DAY’ Section. Please enter like this👇\n\n🔹/tban (<code>00 00 00</code>)🔹\n\nHere the first 2 zeros is day and second 2 zeros is hour and the third 2 zeros is minute. but don't use brakets its just for showing\n\nPlease try again😊</b>", parse_mode = 'html')
		return 
	if len(args1[0]) < 2:
		update.message.reply_text("<b>Invalid time entered! as correction you entered less then expected number on the ‘DAY’ Section. Please enter like this👇\n\n🔹/tban (<code>00 00 00</code>)🔹\n\nHere the first 2 zeros is day and second 2 zeros is hour and the third 2 zeros is minute. but don't use brakets its just for showing\n\nPlease try again😊</b>", parse_mode = 'html')
		return
	if len(args1[1]) > 2:
		update.message.reply_text("<b>Invalid time entered! as correction you entered more then expected number on the ‘HOUR’ Section. Please enter like this👇\n\n🔹/tban (<code>00 00 00</code>)🔹\n\nHere the first 2 zeros is day and second 2 zeros is hour and the third 2 zeros is minute. but don't use brakets its just for showing\n\nPlease try again😊</b>", parse_mode = 'html')
		return
	if len(args1[1]) < 2:
		update.message.reply_text("<b>Invalid time entered! as correction you entered less then expected number on the ‘HOUR’ Section. Please enter like this👇\n\n🔹/tban (<code>00 00 00</code>)🔹\n\nHere the first 2 zeros is day and second 2 zeros is hour and the third 2 zeros is minute. but don't use brakets its just for showing\n\nPlease try again😊</b>", parse_mode = 'html')
		return 
	if len(args1[2]) > 2:
		update.message.reply_text("<b>Invalid time entered! as correction you entered more then expected number on the ‘MINUTE’ Section. Please enter like this👇\n\n🔹/tban (<code>00 00 00</code>)🔹\n\nHere the first 2 zeros is day and second 2 zeros is hour and the third 2 zeros is minute. but don't use brakets its just for showing\n\nPlease try again😊</b>", parse_mode = 'html')
		return
	if len(args1[2]) < 2:
		update.message.reply_text("<b>Invalid time entered! as correction you entered less then expected number on the ‘MINUTE’ Section. Please enter like this👇\n\n🔹/tban (<code>00 00 00</code>)🔹\n\nHere the first 2 zeros is day and second 2 zeros is hour and the third 2 zeros is minute. but don't use brakets its just for showing\n\nPlease try again😊</b>", parse_mode = 'html')
		return 
		
	try:
		d = int(args1[0])
		h = int(args1[1])
		m = int(args1[2])
		if h > 60:
			update.message.reply_text("<b>😅Well! if you count minutes its total 60 not more than that. but you entered more then 60. its not thst tough isn't it.</b>", parse_mode = 'html')
			return
		if m > 60:
			update.message.reply_text("*Are you even did study in your hole life?! because how seconds are more then 60?.*", parse_mode = ParseMode.MARKDOWN)
			return
	except:
		update.message.reply_text("*Wrong Keyword entered!. it's because it's possible that you enterd any alphabet or any other symbols. make sure you only enter numbers.\n\nPlease try again after correction😊*", parse_mode = ParseMode.MARKDOWN)
		return
	
	day = 60 * 60 * 24 * d
	hour = 60 * 60 * h
	minute = 60 * m
	tot_t = (day + hour + minute)
	if tot_t < 0:
		update.message.reply_text("<b>For Using this command you have to Use minimum 1 minute.\notherwise you can use /ban command to ban a user for forever.</b>", parse_mode = 'html')
		return 
	if tot_t == 0:
		update.message.reply_text("<b>For Using this command you have to Use minimum 1 minute.\notherwise you can use /ban command to ban a user for forever.</b>", parse_mode = 'html')
		return 
	tot_t = int(time.time() + int(tot_t))
	
	try:
		chat.ban_member(user_id.id, until_date=tot_t)
	except:
		update.message.reply_text("*Can't ban the member. meybe its because i am not admin in here or you entered details wrong. otherwise try again later :)*", parse_mode = ParseMode.MARKDOWN)
		return
	link = mention_html(user_id.id, user_id.first_name)
	update.message.reply_text('<b>{} Is now banned for <code>{}</code>Days, <code>{}</code>Hours, <code>{}</code>Minutes</b>'.format(link,d,h,m), parse_mode = 'html', disable_web_page_preview=True)

def unban(update,context):
	chat = update.effective_chat
	user = update.effective_user.id
	if chat.type == 'private':
		update.message.reply_text("<b>Sorry but this command only work's on group's. Add me on your group to try this😊</b>", parse_mode = 'html')
		return 
	member = chat.get_member(user)
	if (not (member.status == 'administrator' or member.status == 'creator')):
		update.message.reply_text('*I am really Sorry. but you dont have necessary rights to do that.\n\nPlease become an admin first!*', parse_mode = ParseMode.MARKDOWN )
		return
	try:
		user_id = update.message.reply_to_message.from_user
	except:
		update.message.reply_text("<b>For using this command you have to send it on a reply someone's previous message. Otherwise it won't work\n\nPlease try again😊</b>", parse_mode = 'html')
		return
	if user_id.id == bot.id:
		update.message.reply_text('*Well! I am already unbanned otherwise how can i sending messages here dummy ;)*', parse_mode = ParseMode.MARKDOWN )
		return
	prom = chat.get_member(user_id.id)
	if prom.status == 'administrator':
		update.message.reply_text("*No one can ban, unban admins.*", parse_mode = ParseMode.MARKDOWN)
		return 
	if prom.status == 'creator':
		update.message.reply_text("*Well, Well! No one can ban group creator so how can i unban him?*", parse_mode = ParseMode.MARKDOWN)
		return 
	if not user_id:
		update.message.reply_text('*I am not sure this user even exist!*', parse_mode = ParseMode.MARKDOWN)
		return
	try:
		chat.get_member(user_id.id)
	except BadRequest as bdr:
		if bdr.message == 'User not found':
			update.message.reply_text("*Can't seem to find this person!*", parse_mode = ParseMode.MARKDOWN)
			return
		else:
			update.message.reply_text("*Can't find this user!*", parse_mode = ParseMode.MARKDOWN)
			return
	
	try:
		lnk = mention_html(user_id.id, user_id.first_name)
		chat.get_member(user_id.id)
		chat.unban_member(user_id.id)
		update.message.reply_text('<b>{} is now unbanned.</b>'.format(lnk), parse_mode = 'html', disable_web_page_preview=True)
	except:
		update.message.reply_text('<b>Something wrong heppen!! plese try again later!</b>', parse_mode = 'html')