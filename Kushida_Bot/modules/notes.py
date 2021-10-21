from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater
import time
import os
from Kushida_Bot.modules import console

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

notes = console.nts

def upnote(update,context):
	args = update.message.text.split(None, 1)
	user = update.effective_user
	try:
		args1 = args[1].split(':',1)
		arggs = args1[0]
		if ' ' == arggs[-1]:
			arggs = arggs.replace(arggs[-1], '')
	except:
		update.message.reply_text('<b>Not Enough Value Entered!!\nFor using this command You have to send it like this on a previous message reply👇</b>\n\n🔹/upnote (<code>Note Title</code>)🔹.\n\n<b>Otherwise Send it like this👇</b>\n\n🔹/upnote (<code>Note Title : Your Note</code>)🔹\n\n<b>Make Sure you used the : symbol after note title its important😊</b>', parse_mode = 'html')
		return 
	if len(args1) < 2:
		if len(args1) < 1:
			update.message.reply_text('<b>Not Enough Value Entered!!\nFor using this command You have to send it like this on a previous message reply👇</b>\n\n🔹/upnote (<code>Note Title</code>)🔹.\n\n<b>Otherwise Send it like this👇</b>\n\n🔹/upnote (<code>Note Title : Your Note</code>)🔹\n\n<b>Make Sure you used the : symbol after note title its important😊</b>', parse_mode = 'html')
		else:
			try:
				txt = update.message.reply_to_message.text
			except:
				update.message.reply_text('<b>Not able to save it!!\nFor using this command You have to send it like this on a previous message reply👇</b>\n\n🔹/upnote (<code>Note Title</code>)🔹.\n\n<b>Otherwise Send it like this👇</b>\n\n🔹/upnote (<code>Note Title : Your Note</code>)🔹\n\n<b>Make Sure you used the : symbol after note title its important😊</b>', parse_mode = 'html')
				return
			if user.id in notes.keys():
				if arggs in notes[user.id]:
					update.message.reply_text('<b>I am really Sorry. This note title is already availeable please try with another title ;)</b>', parse_mode = 'html')
					return
				else:
					notes[user.id][arggs] = txt
					update.message.reply_text('<b>Note Successfully Saved.✅</b>', parse_mode = 'html')
			else:
				notes[user.id] = {}
				notes[user.id][arggs] = txt
				update.message.reply_text('<b>Note Successfully Saved.✅</b>', parse_mode = 'html')
			
	else:
		if user.id in notes.keys():
			if arggs in notes[user.id]:
				update.message.reply_text('<b>I am really Sorry. This note title is already availeable please try with another title ;)</b>', parse_mode = 'html')
				return
			else:
				notes[user.id][arggs] = args1[1]
				update.message.reply_text('<b>Note Successfully Saved.✅</b>', parse_mode = 'html')
		else:
			notes[user.id] = {}
			notes[user.id][arggs] = args1[1]
			update.message.reply_text('<b>Note Successfully Saved.✅</b>', parse_mode = 'html')

def note(update,context):
	user = update.effective_user
	if user.id not in notes.keys():
		update.message.reply_text('<b>I am really Sorry But you wont Have any notes to view😅. Please Save a note First!!</b>',parse_mode = 'html')
		return 
	else:
		v_note = ''
		for my_note in notes[user.id].keys():
			v_note = v_note + '🔹' + ' ' + my_note + '\n\n'
		
		update.message.reply_text('<b>Here is your Note List🔻</b>\n\n<code>{}</code>'.format(v_note),parse_mode = 'html')

def delnote(update,context):
	user = update.effective_user
	args = update.message.text.split(None,1)
	if len(args) < 2:
		update.message.reply_text('<b>For using this command you have to send it like this👇</b>\n\n🔹/delnote (<code>Note Title</code>)🔹\n\n<b>then i will delete your note. dont use brakets its just for showing.😊</b>', parse_mode = 'html')
		return 
	else:
		if user.id not in notes.keys():
			update.message.reply_text('<b>I am really Sorry but you dont have any notes to delete😅. please save a note first then try it again</b>', parse_mode = 'html')
			return 
		elif args[1] not in notes[user.id].keys():
			update.message.reply_text('<b>I am really Sorry. but this Note Title is not availeable on your note list. please check your all note list with /mynotes command then try it againg ;)</b>', parse_mode = 'html')
			return 
		else:
			try:
				del notes[user.id][args[1]]
				update.message.reply_text('<b>This Note has been Successfully Deleted✅</b>', parse_mode = 'html')
			except:
				update.message.reply_text("<b>Can't able to delete right now. please try again after some time :(</b>", parse_mode = 'html')

def dlnote(update,context):
	args = update.message.text.split(None,1)
	user = update.effective_user
	if len(args) < 2:
		update.message.reply_text("<b>For using this command you have to send it like this👇</b>\n\n🔹/dlnote (<code>Note Title</code>)🔹\n\n<b>Don't use brakets it's just for showing. please try again😊</b>", parse_mode = 'html')
		return 
	else:
		if user.id not in notes.keys():
			update.message.reply_text('<b>I am really Sorry but you dont have any notes to download or view😅. please save a note first then try it again</b>', parse_mode = 'html')
			return 
		elif args[1] not in notes[user.id].keys():
			update.message.reply_text('<b>I am really Sorry. but this Note Title is not availeable on your note list. please check your all note list with /mynotes command then try it againg ;)</b>', parse_mode = 'html')
			return 
		else:
			
			keys = InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton(
							text = 'View Here📂',
							callback_data = '{}+{}ads'.format(args[1],user.id)
						),
						InlineKeyboardButton(
							text = 'Download⏬',
							callback_data ='{}+{}'.format(args[1],user.id)
						)
					]
				]
			)
			
			update.message.reply_text('<b>Your Note</b> : <code>{}</code>'.format(args[1]), reply_markup = keys, parse_mode = 'html')
			cr_doc = open('Kushida_Bot/modules/helper_function/txt_file/{}.txt'.format(args[1]), 'w+')
			cr_doc.write(notes[user.id][args[1]])

def que(update,context):
	user = update.callback_query.from_user
	querry = update.callback_query
	qdta = querry.data.split('+')
	if qdta[1] != str(user.id):
		if qdta[1] != str(user.id) + 'ads':
			querry.answer(text = 'I am really sorry. But you are not authorized to do that!.', show_alert = True)
			return 
	querry.answer()
	if 'ads' in qdta[1]:
		os.remove('Kushida_Bot/modules/helper_function/txt_file/{}.txt'.format(qdta[0]))
		ild = qdta[1]
		idd = ild.replace('ads', '')
		idd = int(idd)
		try:
			querry.edit_message_text('<b>Your Note: </b><i>{}</i>'.format(notes[idd][qdta[0]]), parse_mode = 'html')
		except:
			querry.edit_message_text("<b>This Note isnt viewable. Please Try to Download it</b>", parse_mode = 'html')
			return
	elif 'ads' not in qdta[1]:
		iddd = int(qdta[1])
		one = querry.edit_message_text('<b>Sending📲...</b>', parse_mode = 'html')
		doc = open('Kushida_Bot/modules/helper_function/txt_file/{}.txt'.format(qdta[0]), 'rb')
		try:
			update.callback_query.message.reply_document(doc)
			one.delete()
			os.remove('Kushida_Bot/modules/helper_function/txt_file/{}.txt'.format(qdta[0]))
		except Exception as e:
			print(e)
			querry.edit_message_text("<b>I am really sorry i can't able to send it. it's because of meny user's are used the same command at the same time. please try again😊</b>", parse_mode = 'html')
			os.remove('Kushida_Bot/modules/helper_function/txt_file/{}.txt'.format(qdta[0]))
