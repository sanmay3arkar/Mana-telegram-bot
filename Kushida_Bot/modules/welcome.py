from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

rules = {}
btns = {}
btn_res = {}
lnks = {}

class Main():
	def __init__(self):
		self.grp = ''
		self.clkr = ''
	def setrules(self,update,context):
		args = update.message.text.split(None,1)
		user = update.effective_user
		chat = update.effective_chat
		admin = chat.get_member(user.id)
		if chat.type == 'private':
			update.message.reply_text('*I am really sorry this command only work on groups. add me on your group to use this command:)*', parse_mode = ParseMode.MARKDOWN)
			return 
		
		if (not(admin.status == 'administrator' or admin.status == 'creator')):
			update.message.reply_text("<b>I am really sorry but you don't have necessary rights to do that. please become an admin first.</b>", parse_mode = 'html')
			return 
		
		if len(args) < 2:
			if chat.id not in rules.keys():
				try:
					mes = update.message.reply_to_message.text
				except:
					update.message.reply_text('<b>For useing this command you have to send it on a reply. otherwise Send it like this👇</b>\n\n🔹/addwelcome (<code>Welcome Message</code>)🔹\n\n<b>Please Try again😊</b>', parse_mode = 'html')
					return
			else:
				mes = rules[chat.id]
		else:
			mes = args[1]
		
		keys = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					text = 'Button ON',
					callback_data = 'ss_btn'
				),
				InlineKeyboardButton(
					text = 'Button OFF',
					callback_data = 'rrm_btn'
				)
			],
			[
				InlineKeyboardButton(
					text = 'Preview',
					callback_data = 'pprev'
				)
			]
		]
	)
	
		rules[chat.id] = mes
		update.message.reply_text("<b>Seted Welcome message on this group:</b>\n\n<i>{}</i>".format(rules[chat.id]), parse_mode = 'html', reply_markup = keys)
		self.clkr = update.effective_user.id

	def stbtn(self,update,context):
		group = update.effective_chat
		query = update.callback_query
		user = update.callback_query.from_user
		member = group.get_member(user.id)
		
		
		if (not(member.status == 'administrator' or member.status == 'creator')):
			query.answer("You don't have any necessary rights to do that. please become an admin first!", show_alert = True)
			return 
		if query.data == 'ss_btn':
			if group.id not in btns.keys():
				query.answer(text = "You Haven't set any button's yet! Please Set button using /setwelbutton Command.", show_alert = True)
				return 
			elif group.id not in btn_res.keys():
				btn_res[group.id] = 'ON'
				query.answer('Buttons successfully Enabled!✅')
			elif btn_res[group.id] == 'ON':
				query.answer(text = "Button's are already enabled!", show_alert = True)
				return 
			else:
				btn_res[group.id] = 'ON'
				query.answer('Buttons successfully Enabled!✅')
		elif query.data == 'rrm_btn':
			if group.id not in btns.keys():
				query.answer(text = "You Haven't set any button's yet! Please Set button using /setwelbutton Command.", show_alert = True)
				return 
			elif group.id not in btn_res.keys():
				query.answer(text = "Button's are already disabled!", show_alert = True)
				return 
				
			elif btn_res[group.id] == 'OFF':
				query.answer(text = "Button's are already Disabled!", show_alert = True)
				return
			else:
				btn_res[group.id] = 'OFF'
				query.answer('Buttons successfully Disabled!✅')
		elif query.data == 'pprev':
			query.answer()
			if group.id not in btn_res.keys():
				query.edit_message_text("<b>{}</b>".format(rules[group.id]),parse_mode = 'html')
			elif btn_res[group.id] == 'OFF':
				query.edit_message_text("<b>{}</b>".format(rules[group.id]),parse_mode = 'html')
			else:
				if 'btn3' in btns[group.id].keys():
					key = InlineKeyboardMarkup(
						[
							[
								InlineKeyboardButton(
									text = btns[group.id]['btn1'],
									url = lnks[group.id]['lnk1']
								),
								InlineKeyboardButton(
									text = btns[group.id]['btn2'],
									url= lnks[group.id]['lnk2']
								)
							],
							[
								InlineKeyboardButton(
									text= btns[group.id]['btn3'],
									url= lnks[group.id]['lnk3']
								)
							]
						]
					)
				elif 'btn2' in btns[group.id].keys():
					if 'btn3' not in btns[group.id].keys():
						key = InlineKeyboardMarkup(
							[
								[
									InlineKeyboardButton(
										text= btns[group.id]['btn1'],
										url= lnks[group.id]['lnk1']
									),
									InlineKeyboardButton(
										text= btns[group.id]['btn2'],
										url= lnks[group.id]['lnk2']
									)
								]
							]
						)
					
				elif 'btn1' in btns[group.id].keys():
					if 'btn2' not in btns[group.id].keys():
						key = InlineKeyboardMarkup(
							[
								[
									InlineKeyboardButton(
										text= btns[group.id]['btn1'],
										url= lnks[group.id]['lnk1']
									)
								]
							]
						)
				query.edit_message_text("<b>{}</b>".format(rules[group.id]),parse_mode = 'html', reply_markup = key)

def setbutton(update,context):
	chat = update.effective_chat
	user = update.effective_user
	member = chat.get_member(user.id)
	
	if chat.type == 'private':
		update.message.reply_text('<b>I am really sorry. but this command only work on groups. add me on your group to try it😊</b>', parse_mode = 'html')
		return 
	
	if (not(member.status == 'administrator' or member.status == 'creator')):
		update.message.reply_text("<b>I am really sorry but you don't have necessary rights to do that. please become an admin first</b>", parse_mode = 'html')
		return 
	args = update.message.text.split(None,1)
	if len(args) < 2:
		update.message.reply_text("<b>For set button's you have to send it like this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
		return
	else:
		try:
			args1 = args[1].split('#')
		except:
			update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
			return 
		
		if len(args1) > 3:
			update.message.reply_text("<b>More then expected Value's!\nMake sure you won't try to add more then 3 button's because only 3 button's are allowed to add. Please Try Again😊</b>", parse_mode = 'html')
			return 
		
		if len(args1) == 3:
			btn1 = args1[0].split('-')
			if len(btn1) > 2:
				update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
				return 
			
			elif len(btn1) < 2:
				update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
				return
			elif 'https://' not in btn1[1]:
				if 'http://' not in btn1[1]:
					update.message.reply_text('<b>Invalid URL entered!\nMake Sure you use https:// or http:// on the link.please Try again😊</b>', parse_mode = 'html')
					return 
			elif ' ' in btn1[1]:
				update.message.reply_text('<b>Spaces found on URL!\nMake sure you dont use spaces on the link. please try again😊</b>', parse_mode = 'html')
				return 
			btn2 = args1[1].split('-')
			if len(btn2) > 2:
				update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
				return 
			elif len(btn2) < 2:
				update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
				return 
			elif 'https://' not in btn2[1]:
				if 'http://' not in btn2[1]:
					update.message.reply_text('<b>Invalid URL entered!\nMake Sure you use https:// or http:// on the link.please Try again😊</b>', parse_mode = 'html')
					return 
			elif ' ' in btn2[1]:
				update.message.reply_text('<b>Spaces found on URL!\nMake sure you dont use spaces on the link. please try again😊</b>', parse_mode = 'html')
				return 
			btn3 = args1[2].split('-')
			if len(btn3) > 2:
				update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
				return 
			elif len(btn3) < 2:
				update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
				return 
			elif 'https://' not in btn3[1]:
				if 'http://' not in btn3[1]:
					update.message.reply_text('<b>Invalid URL entered!\nMake Sure you use https:// or http:// on the link.please Try again😊</b>', parse_mode = 'html')
					return 
			elif ' ' in btn3[1]:
				update.message.reply_text('<b>Spaces found on URL!\nMake sure you dont use spaces on the link. please try again😊</b>', parse_mode = 'html')
				return 
			if chat.id not in btns.keys():
				btns[chat.id] = {}
				btns[chat.id]['btn1'] = btn1[0]
				btns[chat.id]['btn2'] = btn2[0]
				btns[chat.id]['btn3'] = btn3[0]
			else:
				btns[chat.id]['btn1'] = btn1[0]
				btns[chat.id]['btn2'] = btn2[0]
				btns[chat.id]['btn3'] = btn3[0]
			if chat.id not in lnks.keys():
				lnks[chat.id] = {}
				lnks[chat.id]['lnk1'] = btn1[1]
				lnks[chat.id]['lnk2'] = btn2[1]
				lnks[chat.id]['lnk3'] = btn3[1]
			else:
				lnks[chat.id]['lnk1'] = btn1[1]
				lnks[chat.id]['lnk2'] = btn2[1]
				lnks[chat.id]['lnk3'] = btn3[1]
				
			update.message.reply_text("<b>Button's Successfully Set for Welcome Message✅</b>", parse_mode = 'html')
				
		elif len(args1) == 2:
			btn1 = args1[0].split('-')
			if len(btn1) > 2:
				update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
				return 
			elif len(btn1) < 2:
				update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
				return 
			elif 'https://' not in btn1[1]:
				if 'http://' not in btn1[1]:
					update.message.reply_text('<b>Invalid URL entered!\nMake Sure you use https:// or http:// on the link.please Try again😊</b>', parse_mode = 'html')
					return 
			elif ' ' in btn1[1]:
				update.message.reply_text('<b>Spaces found on URL!\nMake sure you dont use spaces on the link. please try again😊</b>', parse_mode = 'html')
				return 
			btn2 = args1[1].split('-')
			if len(btn2) > 2:
				update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
				return 
			elif len(btn2) < 2:
				update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
				return 
			elif 'https://' not in btn2[1]:
				if 'http://' not in btn2[1]:
					update.message.reply_text('<b>Invalid URL entered!\nMake Sure you use https:// or http:// on the link.please Try again😊</b>', parse_mode = 'html')
					return 
			elif ' ' in btn2[1]:
				update.message.reply_text('<b>Spaces found on URL!\nMake sure you dont use spaces on the link. please try again😊</b>', parse_mode = 'html')
				return 
			if chat.id not in btns.keys():
				btns[chat.id] = {}
				btns[chat.id]['btn1'] = btn1[0]
				btns[chat.id]['btn2'] = btn2[0]
			else:
				btns[chat.id]['btn1'] = btn1[0]
				btns[chat.id]['btn2'] = btn2[0]
			if chat.id not in lnks.keys():
				lnks[chat.id] = {}
				lnks[chat.id]['lnk1'] = btn1[1]
				lnks[chat.id]['lnk2'] = btn2[1]
			else:
				lnks[chat.id]['lnk1'] = btn1[1]
				lnks[chat.id]['lnk2'] = btn2[1]
			if 'btn3' in btns[chat.id].keys():
				del btns[chat.id]['btn3']
			if 'lnk3' in lnks[chat.id].keys():
				del lnks[chat.id]['lnk3']
			
			update.message.reply_text("<b>Button's Successfully Set for welcome message✅</b>", parse_mode = 'html')
				
		elif len(args1) == 1:
			btn1 = args1[0].split('-')
			if len(btn1) > 2:
				update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
				return 
			elif len(btn1) < 2:
				update.message.reply_text("<b>Incorrect pettern!\n Make sure you follow this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
				return 
			elif 'https://' not in btn1[1]:
				if 'http://' not in btn1[1]:
					update.message.reply_text('<b>Invalid URL entered!\nMake Sure you use https:// or http:// on the link.please Try again😊</b>', parse_mode = 'html')
					return
			elif ' ' in btn1[1]:
				update.message.reply_text('<b>Spaces found on URL!\nMake sure you dont use spaces on the link. please try again😊</b>', parse_mode = 'html')
				return  
			if chat.id not in btns.keys():
				btns[chat.id] = {}
				btns[chat.id]['btn1'] = btn1[0]
			else:
				btns[chat.id]['btn1'] = btn1[0]
			if chat.id not in lnks.keys():
				lnks[chat.id] = {}
				lnks[chat.id]['lnk1'] = btn1[1]
			else:
				lnks[chat.id]['lnk1'] = btn1[1]
			if 'btn3' in btns[chat.id].keys():
				del btns[chat.id]['btn3']
			if 'lnk3' in lnks[chat.id].keys():
				del lnks[chat.id]['lnk3']
			if 'btn2' in btns[chat.id].keys():
				del btns[chat.id]['btn2']
			if 'lnk2' in lnks[chat.id].keys():
				del lnks[chat.id]['lnk2']
			
			update.message.reply_text("<b>Button's Successfully Set for welcome message✅</b>", parse_mode = 'html')
				
		else:
			update.message.reply_text("<b>For set button's you have to send it like this pattern👇</b>\n\n /setwelbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link</code>\n\n<b>Meximum 3 buttons you are able to set. and make sure you use ‘ - ’ and ‘#’ Symbol its very important. do not use any spaces between bttton name and button link. and make sure you use ‘https://’ to the links. and do not use - and # to the button name. Please Try again😊</b>", parse_mode = 'html')
			return 

def rule(update,context):
	chat = update.effective_chat
	if chat.type == 'private':
		update.message.reply_text('<b>This Command only work on groups. so add me on your group to try this ;)</b>', parse_mode = 'html')
		return
	if chat.id not in rules.keys():
		update.message.reply_text('<b>Welcome Message Not seted on this group. Ask admins for further infomation;)</b>', parse_mode = 'html')
		return 
	if chat.id not in btn_res.keys():
		update.message.reply_text('<b>{}</b>'.format(rules[chat.id]), parse_mode = 'html')
		
	elif btn_res[chat.id] == 'OFF':
		update.message.reply_text('<b>{}</b>'.format(rules[chat.id]), parse_mode = 'html')
		
	elif chat.id not in btns.keys():
		update.message.reply_text('<b>{}</b>'.format(rules[chat.id]), parse_mode = 'html')
	else:
		if 'btn3' in btns[chat.id].keys():
			key = InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton(
							text= btns[chat.id]['btn1'],
							url= lnks[chat.id]['lnk1']
						),
						InlineKeyboardButton(
							text= btns[chat.id]['btn2'],
							url= lnks[chat.id]['lnk2']
						)
					],
					[
						InlineKeyboardButton(
							text= btns[chat.id]['btn3'],
							url= lnks[chat.id]['lnk3']
						)
					]
				]
			)
			
		elif 'btn2' in btns[chat.id].keys():
			if 'btn3' not in btns[chat.id].keys():
				key = InlineKeyboardMarkup(
					[
						[
							InlineKeyboardButton(
								text=btns[chat.id]['btn1'],
								url= lnks[chat.id]['lnk1']
							),
							InlineKeyboardButton(
								text=btns[chat.id]['btn2'],
								url=lnks[chat.id]['lnk2']
							)
						]
					]
				)
		elif 'btn1' in btns[chat.id].keys():
			if 'btn2' not in btns[chat.id].keys():
				key = InlineKeyboardMarkup(
					[
						[
							InlineKeyboardButton(
								text=btns[chat.id]['btn1'],
								url=lnks[chat.id]['lnk1']
							)
						]
					]
				)
		
		update.message.reply_text('<b>{}</b>'.format(rules[chat.id]), parse_mode = 'html', reply_markup = key)

def rmrul(update,context):
	chat = update.effective_chat
	user = update.effective_user
	member = chat.get_member(user.id)
	
	if (not(member.status == 'administrator' or member.status == 'creator')):
		update.message.reply_text("<b>I am really sorry but you don't have necessary rights to do that!</b>", parse_mode = 'html')
		return 
	if chat.type == 'private':
		update.message.reply_text("<b>I am really sorry but this command only work on groups. add me on your group to try it ;)</b>", parse_mode = 'html')
		return 
	
	if chat.id not in rules.keys():
		update.message.reply_text("<b>You haven't Set any welcome message to delete! First Add welcome message then try this again.</b>", parse_mode = 'html')
		return 
	else:
		del rules[chat.id]
	
	if chat.id in btns.keys():
		del btns[chat.id]
		del lnks[chat.id]
	update.message.reply_text("<b>Welcome message has been successfully deleted✅</b>", parse_mode = 'html')