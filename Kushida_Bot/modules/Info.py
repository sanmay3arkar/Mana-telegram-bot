from telegram import Bot
from telegram.ext import Updater
import os
from telegram.utils.helpers import mention_html
from Kushida_Bot.modules import console, afk

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

me = {}

def setme(update,context):
	args = update.message.text.split(None,1)
	user = update.effective_user
	if len(args) < 2:
		try:
			text = update.nessage.reply_to_message.text
		except:
			update.message.reply_text("<b>For using this command you have to send it on a reply of someones previous message. Otherwise send it like this👇</b>\n\n🔹/setme (<code>Your Bio</code>)🔹\n\n<b>Please Try Again😊</b>", parse_mode = 'html')
			return 
	else:
		text = args[1]
	
	me[user.id] = text
	update.message.reply_text('<b>Your Bio has been successfully seted✅</b>', parse_mode = 'html')

def rmme(update,context):
	user = update.effective_user
	if user.id not in me.keys():
		update.message.reply_text("<b>You haven't set any bio yet!\nPlease set your bio first using /setme command then try this comman again ;)</b>", parse_mode ='html')
	else:
		del me[user.id]
		update.message.reply_text("<b>Your bio has been successfully removed✅</b>", parse_mode = 'html')
		
def info(update,context):
	text = ""
	chat = update.effective_chat
	try:
		user = update.message.reply_to_message.from_user
	except:
		user = update.message.from_user
	
	try:
		ph = bot.get_user_profile_photos(user.id).photos[0][-1]
		ph1 = bot.get_file(ph["file_id"])
		ph1.download("helper_function/profile_pic/{}.png".format(user.id))
	except:
		pass
	
	if os.path.isfile('Kushida_Bot/modules/helper_function/profile_pic/{}.png'.format(user.id)):
		phto = open('Kushida_Bot/modules/helper_function/profile_pic/{}.png'.format(user.id), 'rb')
		if chat.type == 'private':
			text += "╒═══「 <b>🔻User Info🔻</b> 」\nID: <code>{}</code>\nFirst Name: <b>{}</b>\nLast Name: <b>{}</b>\nUsername: <b>{}</b>\nPermaLink: {}\n\n".format(user.id, user.first_name, user.last_name, user.username, mention_html(user.id, 'link'))
		
			if user.id in me.keys():
				text += "Bio : <i>{}</i>\n\n".format(me[user.id])
			else:
				text += "Bio : <i>Not Seted</i>\n\n"
		
			if user.id in console.gban_list:
				text += "Is GBanned : <b>Yes</b>"
			else:
				text += "Is GBanned : <b>No</b>"
			update.message.reply_document(phto, caption = text, parse_mode = 'html')
		else:
			text += "╒═══「 <b>🔻User Info🔻</b> 」\nID: <code>{}</code>\nFirst Name: <b>{}</b>\nLast Name: <b>{}</b>\nUsername: <b>{}</b>\nPermaLink: {}\n\n".format(user.id, user.first_name, user.last_name, user.username, mention_html(user.id, 'link'))
			
			if user.id in console.m_sudo_user:
				text += "╒═══「<b>Bot Rank:</b> <code>Sudo Admin</code>」\n"
			elif user.id in console.s_admins:
				text += "╒═══「<b>Bot Rank:</b> <code>Admin</code>」\n"
			else:
				text += "╒═══「<b>Bot Rank:</b> <code>User</code>」\n"
			adm = chat.get_member(user.id)
			if adm.status != 'member':
				text += 'Stayed as: <b>{}</b>\nTitle: <b>{}</b>\n'.format(adm.status, adm.custom_title)
			else:
				text += 'Stayed as: <b>{}</b>\nTitle: <b>None</b>\n'.format(adm.status)
			if user.id in afk.afk_dict.keys():
				text += "╘══「<b>Currently Afk:</b> <code>Yes</code>」\n\n"
			else:
				text += "╘══「<b>Currently Afk:</b> <code>No</code>」\n\n"
			
			if user.id in me.keys():
				text += "Bio : <i>{}</i>\n\n".format(me[user.id])
			else:
				text += "Bio : <i>Not Seted</i>\n\n"
			
			if user.id in console.gban_list:
				text += "Is GBanned : <b>Yes</b>"
			else:
				text += "Is GBanned : <b>No</b>"

			update.message.reply_document(phto, caption = text, parse_mode = 'html')
			try:
				os.remove("Kushida_Bot/modules/helper_function/profile_pic/{}.png".format(user.id))
			except:
				return
							
	else:
		if chat.type == 'private':
			text += "╒═══「 <b>🔻User Info🔻</b> 」\nID: <code>{}</code>\nFirst Name: <b>{}</b>\nLast Name: <b>{}</b>\nUsername: <b>{}</b>\nPermaLink: <b>{}</b>\n\n".format(user.id, user.first_name, user.last_name, user.username, mention_html(user.id, 'link'))
		
			if user.id in me.keys():
				text += "Bio : <i>{}</i>\n\n".format(me[user.id])
			else:
				text += "Bio : <i>Not Seted</i>\n\n"
		
			if user.id in console.gban_list:
				text += "Is GBanned : <b>Yes</b>"
			else:
				text += "Is GBanned : <b>No</b>"
			update.message.reply_text(text, parse_mode = 'html')
		else:
			text += "╒═══「 <b>🔻User Info🔻</b> 」\nID: <code>{}</code>\nFirst Name: <b>{}</b>\nLast Name: <b>{}</b>\nUsername: <b>{}</b>\nPermaLink: <b>{}</b>\n\n".format(user.id, user.first_name, user.last_name, user.username, mention_html(user.id, 'link'))
			
			if user.id in console.m_sudo_user:
				text += "╒═══「<b>Bot Rank:</b> <code>Sudo Admin</code>」\n"
			elif user.id in console.s_admins:
				text += "╒═══「<b>Bot Rank:</b> <code>Admin</code>」\n"
			else:
				text += "╒═══「<b>Bot Rank:</b> <code>User</code>」\n"
			adm = chat.get_member(user.id)
			if adm.status != 'member':
				text += 'Stayed as: <b>{}</b>\nTitle: <b>{}</b>\n'.format(adm.status, adm.custom_title)
			else:
				text += 'Stayed as: <b>{}</b>\nTitle: <b>None</b>\n'.format(adm.status)
			if user.id in afk.afk_dict.keys():
				text += "╘══「<b>Currently Afk:</b> <code>Yes</code>」\n\n"
			else:
				text += "╘══「<b>Currently Afk:</b> <code>No</code>」\n\n"
			
			if user.id in me.keys():
				text += "Bio : <i>{}</i>\n\n".format(me[user.id])
			else:
				text += "Bio : <i>Not Seted</i>\n\n"
			
			if user.id in console.gban_list:
				text += "Is GBanned : <b>Yes</b>"
			else:
				text += "Is GBanned : <b>No</b>"

			update.message.reply_text(text, parse_mode = 'html')
			try:
				os.remove("Kushida_Bot/modules/helper_function/profile_pic/{}.png".format(user.id))
			except:
				return
