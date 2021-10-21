from telegram import Bot, ParseMode
from telegram.ext import Updater
from Kushida_Bot.modules import welcome, blacklist, chatbot, Info, rules, afk
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import random as r
from Kushida_Bot.modules.helper_function import list_dict as l_file
import html
from telegram.utils.helpers import mention_html

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

cred = credentials.Certificate('Kushida_Bot/modules/sql/nagase-mana-firebase.json')
firebase_admin.initialize_app(cred, {
	'databaseURL' : 'https://nagase-mana-default-rtdb.firebaseio.com/'
})

rref = db.reference('Rules')
rle = rref.get()
wref = db.reference('WELMes')
wmes = wref.get()
bref = db.reference('BlackList')
blist = bref.get()
cref = db.reference('Chatbot_list')
cht = cref.get()
wblref = db.reference('WELBLnks')
wbln = wblref.get()
wblsref = db.reference('WELBStat')
wbls = wblsref.get()
wbtnref = db.reference('WELBtns')
wbtn = wbtnref.get()
ntref = db.reference("Notes")
nts = ntref.get()

ref = db.reference('User')
user_dict = ref.get()
gbanref = db.reference('GBan')
gban_list = gbanref.get()
s_adref = db.reference('SAdmin')
s_admins = s_adref.get()
sudoref = db.reference('SudoUser')
m_sudo_user = sudoref.get()
rf = db.reference('Groups')
grp = rf.get()
afk_dict = {}

def afk(update,context):
	args = update.message.text.split(None, 1)
	user = update.message.from_user
	
	if len(args) >= 2:
		afk_dict[user.id] = args[1]
		update.message.reply_text(r.choice(l_file.AWAY).format(user['first_name']))
	else:
		afk_dict[user.id] = " "
		update.message.reply_text(r.choice(l_file.AWAY).format(user['first_name']))

def tuser(update,context):
	chat = update.effective_chat
	user = update.effective_user
	if user.id in afk_dict.keys():
		update.message.reply_text(r.choice(l_file.BACK_AFK).format(user['first_name']))
		afk_dict.pop(user.id)
	else:
		try:
			reply = update.message.reply_to_message.from_user
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
		except:
			pass
	try:
		txt = update.message.text
		if txt in blacklist.lst[chat.id]:
			bot.delete_message(chat.id, update.message.message_id)
			bot.send_message(chat.id, "<b> {} Do not use this word on this group ever again‼️\n\nBecause this word has been banned by group admins</b>".format(user.first_name), parse_mode = 'html')
	except:
		pass
	chat = update.effective_chat
	if chat.id not in grp:
		try:
			if chat.type != "private":
				grp.append(chat.id)
				rrf = db.reference('Groups')
				rrf.set(grp)
		except:
			pass
	if user.id in m_sudo_user:
		m = chat.get_member(user.id)
		if m.status != 'administrator':
			if m.status != 'creator':
				try:
					bot_member = chat.get_member(bot.id)
					bot.promoteChatMember(
            chat.id,
            user.id,
            can_change_info=bot_member.can_change_info,
            can_post_messages=bot_member.can_post_messages,
            can_edit_messages=bot_member.can_edit_messages,
            can_delete_messages=bot_member.can_delete_messages,
            can_invite_users=bot_member.can_invite_users,
            can_restrict_members=bot_member.can_restrict_members,
            can_pin_messages=bot_member.can_pin_messages,
        )
					update.message.reply_text("<b>{} has been promoted to admin because he is a bot sudo admin</b>".format(mention_html(user.id, user.first_name)), parse_mode = 'html')
				except:
					pass
	if user.id in s_admins:
		m = chat.get_member(user.id)
		if m.status != 'administrator':
			if m.status != 'creator':
				try:
					bot_member = chat.get_member(bot.id)
					bot.promoteChatMember(
            chat.id,
            user.id,
            can_change_info=bot_member.can_change_info,
            can_post_messages=bot_member.can_post_messages,
            can_edit_messages=bot_member.can_edit_messages,
            can_delete_messages=bot_member.can_delete_messages,
            can_invite_users=bot_member.can_invite_users,
            can_restrict_members=bot_member.can_restrict_members,
            can_pin_messages=bot_member.can_pin_messages,
        )
					update.message.reply_text("<b>{} has been promoted to admin because he is a bot special admin</b>".format(mention_html(user.id, user.first_name)), parse_mode = 'html')
				except Exception as e:
					print(e)
					pass
	try:
		global gban_list
		global user_dict
		ref = db.reference('User')
		ref1 = db.reference('GBan')
		gban_list = ref1.get()
		user_dict = ref.get()
	except:
		return 
	
	if user.id not in user_dict.keys():
		try:
			cld = ref.child(str(user.id))
			cld.set({
				'first_name':user.first_name,
				'last_name':user.last_name,
				'username':user.username,
				'user_id':user.id
			})
		except:
			return 
	else:
		if user.first_name != user_dict[user.id]['first_name']:
			try:
				cld = ref.child(str(user.id))
				cld.set({
					'first_name':user.first_name,
					'last_name':user.last_name,
					'username':user.username,
					'user_id':user.id
				})
			except:
				return 
		if user.last_name != user_dict[user.id]['last_name']:
			try:
				cld = ref.child(str(user.id))
				cld.set({
					'first_name':user.first_name,
					'last_name':user.last_name,
					'username':user.username,
					'user_id':user.id
				})
			except:
				return 
		if user.username != user_dict[user.id]['username']:
			try:
				cld = ref.child(str(user.id))
				cld.set({
					'first_name':user.first_name,
					'last_name':user.last_name,
					'username':user.username,
					'user_id':user.id
				})
			except:
				return 
	if user.id in gban_list:
		try:
			chat.ban_member(user.id)
		except:
			return 
		update.message.reply_text('*{} has been Kicked from this group. because he is gbaned by admins.*'.format(user.first_name), parse_mode = ParseMode.MARKDOWN)

def n_member(update,context):
	chat = update.effective_chat
	for member in update.message.new_chat_members:
		if chat.id not in grp:
			try:
				if chat.type != "private":
					grp.append(chat.id)
					rrf = db.reference('Groups')
					rrf.set(grp)
			except:
				pass
		if member.id in gban_list:
			try:
				chat.ban_member(member.id)
			except:
				return
			update.message.reply_text('*{} has been Kicked from this group. because he is gbaned by admins.*'.format(member.first_name), parse_mode = ParseMode.MARKDOWN)
			return
		if chat.id not in welcome.rules.keys():
			update.message.reply_text('<b>Welcome {} to {}\n\n• Try to be friendly with everyone\n\n• Enjoy your Stay.😊\n\n• Dont forgot to read the rules /rules</b>'.format(member.first_name, chat.title), parse_mode = 'html')
		else:
			try:
				welcome.rule(update, context)
			except:
				update.message.reply_text('<b>Welcome {} to {}\n\n• Try to be friendly with everyone\n\n• Enjoy your Stay.😊\n\n• Dont forgot to read the rules /rules</b>'.format(member.first_name, chat.title), parse_mode = 'html')
				
def gban(update,context):
	user = update.effective_user
	args = update.message.text.split(None, 1)
	chat = update.effective_chat
	global gban_list
	global s_admins
	global m_sudo_user
	gbanref = db.reference('GBan')
	gban_list = gbanref.get()
	s_adref = db.reference('SAdmin')
	s_admins = s_adref.get()
	sudoref = db.reference('SudoUser')
	m_sudo_user = sudoref.get()
	if user.id not in s_admins:
		if user.id not in m_sudo_user:
			update.message.reply_text("<b>Sorry! But you are not permitted to use this command. Please be an special admin first.</b>", parse_mode = 'html')
			return 
	if len(args) < 2:
		try:
			b_user = update.message.reply_to_message.from_user.id
		except:
			update.message.reply_text('<b>For using this command you have to send it on a reply of someones previous message. please try again😊</b>', parse_mode = 'html')
			return 
	else:
		try:
			b_user = int(args[1])
		except:
			update.message.reply_text('<b>You need to send user id. please use /info to get user id. please try again</b>', parse_mode = 'html')
			return
	if b_user == 632250618:
	 	update.message.reply_text("<b>You trying to GBan my creator. how funny it can be😹</b>", parse_mode = 'html')
	 	return
	if b_user in s_admins:
		update.message.reply_text("*You cant gban other special admins.*", parse_mode = ParseMode.MARKDOWN)
		return
	if b_user in m_sudo_user:
		update.message.reply_text("<b>Whats wrong with you. try to gban a sudo user.</b>", parse_mode ="html")
		return
	if b_user in gban_list:
		update.message.reply_text('*{} is already GBanned.*'.format(b_user), parse_mode = ParseMode.MARKDOWN)
		return 
	try:
		gban_list.append(b_user)
		ref = db.reference('GBan')
		ref.set(gban_list)
		update.message.reply_text('*User {} Has been successfully GBanned.✅*'.format(b_user), parse_mode = ParseMode.MARKDOWN)
	except:
		update.message.reply_text('*Server is currently busy please try after some time*', parse_mode = ParseMode.MARKDOWN)
		try:
			gban_list.remove(b_user)
		except:
			return 
	
def sadmin(update,context):
	user = update.effective_user
	args = update.message.text.split(None,1)
	chat = update.effective_chat
	global gban_list
	global s_admins
	global m_sudo_user
	gbanref = db.reference('GBan')
	gban_list = gbanref.get()
	s_adref = db.reference('SAdmin')
	s_admins = s_adref.get()
	sudoref = db.reference('SudoUser')
	m_sudo_user = sudoref.get()
	if user.id not in m_sudo_user:
		update.message.reply_text('*You havent permitted to give special user permission. Please become a sudo user.*', parse_mode = ParseMode.MARKDOWN)
		return 
	if len(args) < 2:
		try:
			b_user = update.message.reply_to_message.from_user.id
		except:
			update.message.reply_text('<b>For using this command you have to send it on a reply of someones previous message. please try again😊</b>', parse_mode = 'html')
			return 
	else:
		try:
			b_user = int(args[1])
		except:
			update.message.reply_text('<b>You need to send user id. please use /info to get user id. please try again</b>', parse_mode = 'html')
			return 
	if b_user == 632250618:
	 	update.message.reply_text("<b>You trying to give permission to my creator. how funny it can be😹</b>", parse_mode = 'html')
	 	return
	if b_user in s_admins:
		update.message.reply_text('*You Must know that {} already is a  special admin*'.format(b_user), parse_mode = ParseMode.MARKDOWN)
		return 
	try:
		s_admins.append(b_user)
		ref = db.reference('SAdmin')
		ref.set(s_admins)
		update.message.reply_text('*User {} Has been successfully promoted to Special Admin✅*'.format(b_user), parse_mode = ParseMode.MARKDOWN)
	except:
		update.message.reply_text('*Server is currently busy please try after some time*', parse_mode = ParseMode.MARKDOWN)
		try:
			s_admins.remove(b_user)
		except:
			return 

def sudouser(update,context):
	user = update.effective_user
	args = update.message.text.split(None,1)
	chat = update.effective_chat
	global gban_list
	global s_admins
	global m_sudo_user
	gbanref = db.reference('GBan')
	gban_list = gbanref.get()
	s_adref = db.reference('SAdmin')
	s_admins = s_adref.get()
	sudoref = db.reference('SudoUser')
	m_sudo_user = sudoref.get()
	if user.id not in m_sudo_user:
		update.message.reply_text('*You havent permitted to give Sudo User permission. Please become a sudo user.*', parse_mode = ParseMode.MARKDOWN)
		return 
	if len(args) < 2:
		try:
			b_user = update.message.reply_to_message.from_user.id
		except:
			update.message.reply_text('<b>For using this command you have to send it on a reply of someones previous message. please try again😊</b>', parse_mode = 'html')
			return 
	else:
		try:
			b_user = int(args[1])
		except:
			update.message.reply_text('<b>You need to send user id. please use /info to get user id. please try again</b>', parse_mode = 'html')
			return 
	
	if b_user == 632250618:
	 	update.message.reply_text("<b>You trying to give permission to my creator. how funny it can be😹</b>", parse_mode = 'html')
	 	return
	if b_user in m_sudo_user:
		update.message.reply_text('*You Must know that {} already is a sudo user.*'.format(b_user), parse_mode = ParseMode.MARKDOWN)
		return 
	try:
		m_sudo_user.append(b_user)
		ref = db.reference('SudoUser')
		ref.set(m_sudo_user)
		update.message.reply_text('*User {} Has been successfully promoted to SudoUser✅*'.format(b_user), parse_mode = ParseMode.MARKDOWN)
	except:
		update.message.reply_text('*Server is currently busy please try after some time*', parse_mode = ParseMode.MARKDOWN)
		try:
			m_sudo_user.remove(b_user)
		except:
			return 

def rmgban(update,context):
	user = update.effective_user
	args = update.message.text.split(None, 1)
	chat = update.effective_chat
	global gban_list
	global s_admins
	global m_sudo_user
	gbanref = db.reference('GBan')
	gban_list = gbanref.get()
	s_adref = db.reference('SAdmin')
	s_admins = s_adref.get()
	sudoref = db.reference('SudoUser')
	m_sudo_user = sudoref.get()
	gban_list = gbanref.get()
	if user.id not in s_admins:
		if user.id not in m_sudo_user:
			update.message.reply_text("<b>Sorry! But you are not permitted to use this command. Please be an special admin first.</b>", parse_mode = 'html')
			return 
	if len(args) < 2:
		try:
			b_user = update.message.reply_to_message.from_user.id
		except:
			update.message.reply_text('<b>For using this command you have to send it on a reply of someones previous message. please try again😊</b>', parse_mode = 'html')
			return 
	else:
		try:
			b_user = int(args[1])
		except:
			update.message.reply_text('<b>You need to send user id. please use /info to get user id. please try again</b>', parse_mode = 'html')
			return 
	if b_user == 632250618:
	 	update.message.reply_text("<b>Commands like this isnt work to my creator</b>", parse_mode = 'html')
	 	return
	if b_user not in gban_list:
		update.message.reply_text('*{} is already Unbanned*'.format(b_user), parse_mode = ParseMode.MARKDOWN)
		return 
	try:
		gban_list.remove(b_user)
		ref = db.reference('GBan')
		ref.set(gban_list)
		update.message.reply_text('*User {} Has been successfully UnBanned✅*'.format(b_user), parse_mode = ParseMode.MARKDOWN)
	except:
		update.message.reply_text('*Server is currently busy please try after some time*', parse_mode = ParseMode.MARKDOWN)
		try:
			gban_list.append(b_user)
		except:
			return 

def rmsadmin(update,context):
	user = update.effective_user
	args = update.message.text.split(None,1)
	chat = update.effective_chat
	global gban_list
	global s_admins
	global m_sudo_user
	gbanref = db.reference('GBan')
	gban_list = gbanref.get()
	s_adref = db.reference('SAdmin')
	s_admins = s_adref.get()
	sudoref = db.reference('SudoUser')
	m_sudo_user = sudoref.get()
	if user.id not in m_sudo_user:
		update.message.reply_text('*You havent permitted to use this command. Please become a sudo user.*', parse_mode = ParseMode.MARKDOWN)
		return 
	if len(args) < 2:
		try:
			b_user = update.message.reply_to_message.from_user.id
		except:
			update.message.reply_text('<b>For using this command you have to send it on a reply of someones previous message. please try again😊</b>', parse_mode = 'html')
			return 
	else:
		try:
			b_user = int(args[1])
		except:
			update.message.reply_text('<b>You need to send user id. please use /info to get user id. please try again</b>', parse_mode = 'html')
			return 
	if b_user == 632250618:
	 	update.message.reply_text("<b>Commands like this isnt work to my creator</b>", parse_mode = 'html')
	 	return
	if b_user not in s_admins:
		update.message.reply_text('*user {} not a special admin.*'.format(b_user), parse_mode = ParseMode.MARKDOWN)
		return 
	try:
		s_admins.remove(b_user)
		ref = db.reference('SAdmin')
		ref.set(s_admins)
		update.message.reply_text('*User {} Has been successfully removed from Special Admin✅*'.format(b_user), parse_mode = ParseMode.MARKDOWN)
	except:
		update.message.reply_text('*Server is currently busy please try after some time*', parse_mode = ParseMode.MARKDOWN)
		try:
			s_admins.append(b_user)
		except:
			return 

def rmsudouser(update,context):
	user = update.effective_user
	args = update.message.text.split(None,1)
	chat = update.effective_chat
	global gban_list
	global s_admins
	global m_sudo_user
	gbanref = db.reference('GBan')
	gban_list = gbanref.get()
	s_adref = db.reference('SAdmin')
	s_admins = s_adref.get()
	sudoref = db.reference('SudoUser')
	m_sudo_user = sudoref.get()
	if user.id not in m_sudo_user:
		update.message.reply_text('*You havent permitted to use this command. Please become a sudo user.*', parse_mode = ParseMode.MARKDOWN)
		return 
	if len(args) < 2:
		try:
			b_user = update.message.reply_to_message.from_user.id
		except:
			update.message.reply_text('<b>For using this command you have to send it on a reply of someones previous message. please try again😊</b>', parse_mode = 'html')
			return 
	else:
		try:
			b_user = int(args[1])
		except:
			update.message.reply_text('<b>You need to send user id. please use /info to get user id. please try again</b>', parse_mode = 'html')
			return
	
	if b_user == 632250618:
	 	update.message.reply_text("<b>Commands like this isnt work to my creator</b>", parse_mode = 'html')
	 	return
	if b_user not in m_sudo_user:
		update.message.reply_text('*You Must know that user {} not a sudo user.*'.format(b_user), parse_mode = ParseMode.MARKDOWN)
		return 
	try:
		m_sudo_user.remove(b_user)
		ref = db.reference('SudoUser')
		ref.set(m_sudo_user)
		update.message.reply_text('*User {} Has been successfully removed from SudoUser✅*'.format(b_user), parse_mode = ParseMode.MARKDOWN)
	except:
		update.message.reply_text('*Server is currently busy please try after some time*', parse_mode = ParseMode.MARKDOWN)
		try:
			m_sudo_user.append(b_user)
		except:
			return 

def s_blklist(update,context):
	user = update.effective_user
	if user.id != 632250618:
		return
	ref = db.reference("BlackList")
	ref.set(blacklist.lst)
	update.message.reply_text("<b>Notes Successfully Uploded</b>", parse_mode = 'html')

def chbt(update,context):
	user = update.effective_user
	if user.id != 632250618:
		return
	ref = db.reference("Chatbot_list")
	ref.set(chatbot.m_chat)
	update.message.reply_text("<b>Notes Successfully Uploded</b>", parse_mode = 'html')

def Bio(update,context):
	user = update.effective_user
	if user.id != 632250618:
		return
	ref = db.reference("Bio")
	ref.set(Info.me)
	update.message.reply_text("<b>Notes Successfully Uploded</b>", parse_mode = 'html')

'''def s_note(update,context):
	user = update.effective_user
	if user.id != 632250618:
		return
	ref = db.reference("Notes")
	ref.set(notes.notes)
	update.message.reply_text("<b>Notes Successfully Uploded</b>", parse_mode = 'html')'''

def uprule(update,context):
	user = update.effective_user
	if user.id != 632250618:
		return
	try: 
		ref = db.reference('Rules')
		ref.set(rules.rules)
		ref1 = db.reference('RBtns')
		ref1.set(rules.btns)
		ref2 = db.reference('RBTNLnks')
		ref2.set(rules.lnks)
		ref3 = db.reference('RBTNStat')
		ref3.set(rules.btn_res)
		update.message.reply_text('<b>Data Successfully uploded to server master✅. You may proceed next.</b>', parse_mode = 'html')
	except:
		update.message.reply_text('*I am really sorry Master!. But Server is currently busy*', parse_mode = ParseMode.MARKDOWN)

def upwel(update,context):
	user = update.effective_user
	if user.id != 632250618:
		return
	try: 
		ref = db.reference('WELMes')
		ref.set(welcome.rules)
		ref1 = db.reference('WELBtns')
		ref1.set(welcome.btns)
		ref2 = db.reference('WELBLnks')
		ref2.set(welcome.lnks)
		ref3 = db.reference('WELBStat')
		ref3.set(welcome.btn_res)
		update.message.reply_text('<b>Data Successfully uploded to server master✅. You may proceed next.</b>', parse_mode = 'html')
	except:
		update.message.reply_text('*I am really sorry Master!. But Server is currently busy*', parse_mode = ParseMode.MARKDOWN)

def special(update,context):
	user = update.effective_user
	if user.id not in s_admins:
		if user.id not in m_sudo_user:
			return
	
	update.message.reply_text("*Command list for Special users\n\nSAdmin Commands:*\n`~/gban <user id / reply>` :*For globally ban a user. on this bot. so if bot found him in any group bot will kick him from group*\n\n`~/rmgban <user id / reply>` *: For unban a member from gban list*\n\n`~/specialuser` *: To view current SAdmin and Sudo Admins list*\n\n*Special Access : get admin access on any group where this bot belongs.\n\nSudoUser Commands*\n`~/gban <user id / reply>` :*For globally ban a user. on this bot. so if bot found him in any group bot will kick him from group*\n\n`~/rmgban <user id / reply>` *: For unban a member from gban list*\n\n`~/sadmin <user id / reply>`* : To promote a user to Special admin*\n\n`~/rmsadmin <user id / reply>`* : to remove a user from special admin*\n\n`~/sudouser <user id / reply>` *: To promote someone to Sudo User*\n\n`~/rmsudo <user id / reply>` *: To remove someone from sudo user*\n\n`~/specialuser` *: To view current SAdmin and Sudo Admins list\n\nSpecial Access : to get Admin access on any group where your bot belongs.*", parse_mode = ParseMode.MARKDOWN)

def admlist(update,context):
	user = update.effective_user
	if user.id not in s_admins:
		if user.id not in m_sudo_user:
			update.message.reply_text("<b>This command isnt accessable</b>", parse_mode = 'html')
			return
	txt = '♦️SAdmins:\n\n'
	for id in s_admins:
		if str(id) in user_dict.keys():
			try:
				txt += "🔹{}\n\n".format(mention_html(id, user_dict[str(id)]['first_name']))
			except:
				pass
	txt += "Sudo Admins:\n\n" 
	for id in m_sudo_user:
		if str(id) in user_dict.keys():
			try:
				txt += "🔹{}\n\n".format(mention_html(id, user_dict[str(id)]['first_name']))
			except:
				pass
	
	update.message.reply_text("<b>{}</b>".format(txt), parse_mode = 'html')

def statt(update,context):
	user = update.effective_user
	if (not(user.id == 632250618 or user.id == 675277916 or user.id == 1698224515 or user.id == 1762442011 or user.id == 1092080078 or user.id == 1142185639)):
		return
	update.message.reply_text("<b>Total Bot users: {}\n\nTotal Groups Count: {}</b>".format(len(user_dict.keys()), len(grp)),parse_mode = 'html')

def console(update,context):
	user = update.effective_user
	if user.id != 632250618:
		return
	update.message.reply_text("*Console Command for creator*\n\n`~/upblk`* : To upload blacklist To Server*\n\n`~/upchbot` *: To upload chatbot list to server*\n\n`~/upbio` *: to upload bio to the server*\n\n`~/upsnote` *: To upload notes to the server*\n\n`~/uprules` *: To upload Rules detail to the server*\n\n`~/upwel`* : To upload welcome detail to the server*\n\n`~/stats `*: to view bot stats*", parse_mode = ParseMode.MARKDOWN)
		
def gbans(update,context):
	user = update.effective_user
	args = update.message.text.split(None, 1)
	if user.id not in s_admins:
		if user.id not in m_sudo_user:
			update.message.reply_text("<b>You are not authorised to view it.</b>", parse_mode = 'html')
			return
	
	try:
		for i in gban_list:
			txt = '♦️GBan List\n\n'
			if str(i) in user_dict.keys():
				txt += "🔹{}\n\n".format(mention_html(i, user_dict[str(i)]["first_name"]))
		update.message.reply_text("<b>{}</b>".format(txt), parse_mode = 'html')
	except:
		update.message.reply_text("<b>I am really sorry server is currently busy please try again later</b>", parse_mode = 'html')
