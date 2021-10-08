from telegram import Bot, ParseMode
from telegram.ext import Updater, dispatcher, CommandHandler
from telegram.utils.helpers import mention_html
from telegram.error import BadRequest

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

def admn(update,context):
	user = update.effective_user
	chat_id = update.effective_chat.id
	chat = update.effective_chat
	if chat.type == 'private':
		update.message.reply_text("<b>Sorry but this command only work's on group's. Add me on your group to try this😊</b>", parse_mode = 'html')
		return 
	
	fst = update.message.reply_text('<b>Fetching group administrator...</b>', parse_mode = 'html')
	adm = bot.getChatAdministrators(chat_id)
	text = '<b>ADMINISTRATOR OF\n▪️{}</b>'.format(update.effective_chat.title)
	
	bot_list = []
	admin_list = []
	
	for admin in adm:
		user = admin.user
		status = admin.status
		title = admin.custom_title
		
		if user.first_name == '':
			name = '☠ Deleted Account'
		else:
			name = '{}'.format(user.first_name + ' ' + (user.last_name or ' '))
		
		if user.is_bot:
			bot_list.append(name)
			adm.remove(admin)
			continue
		
		if status == 'creator':
		    
		    text += '\n\n<b>👑 CREATOR:</b>'
		    n_lnk = mention_html(user.id, name)
		    
		    text += '\n<b> ♦️{}</b>\n'.format(n_lnk)
		    if title:
		    	text += "<code>      ┗━━🔹{}🔹</code>\n".format(title)
		    else:
		    	text += "<code>      ┗━━🔹Owner🔹</code>\n"
		    
	text += '\n<b>♻ ADMINS:</b>\n'
	
	for admin in adm:
		user = admin.user
		status = admin.status
		title = admin.custom_title
		
		if user.first_name == '':
			name = '☠ Deleted Account'
		else:
			name = '{}'.format(user.first_name + ' ' + (user.last_name or ' '))
			
		a_lnk = mention_html(user.id, name)
		    
		if status == 'administrator':
		    text += '<b> ♦️{}</b>\n'.format(a_lnk)
		    if title:
		    	text += "<code>      ┗━━🔹{}🔹</code>\n".format(title)
		    else:
		    	text += "<code>      ┗━━🔹Admin🔹</code>\n"
	
	text += "\n<b>🤖 BOT'S:</b>\n"
	
	adm = bot.getChatAdministrators(chat_id)
	for admin in adm:
		user = admin.user
		status = admin.status
		title = admin.custom_title
		if user.is_bot:
			bot_link = 'https://t.me/' + user.username
			name = '{}'.format(user.first_name + ' ' + (user.last_name or ''))
			if title:
				text += '<a href = "{}"> ♦️{}</a>\n<code>      ┗━━🔹{}🔹</code>\n'.format(bot_link, name, title)
			else:
			   text += '<b><a href = "{}"> ♦️{}</a></b>\n<code>      ┗━━🔹Helper🔹</code>\n'.format(bot_link, name)
		    
	fst.edit_text(text, parse_mode = 'html', disable_web_page_preview= True)
	
def pin(update,context):
	args = update.message.text.split(None, 1)
	user = update.effective_user
	chat = update.effective_chat
	if chat.type == 'private':
		update.message.reply_text("<b>Sorry but this command only work's on group's. Add me on your group to try this😊</b>", parse_mode = 'html')
		return
	promoter = chat.get_member(user.id)

	if (
        not (promoter.status == 'administrator' or promoter.status == "creator")
    ):
		update.message.reply_text("<b>I am really sorry but you don't have the necessary rights to do that. please become an admin first!</b>", parse_mode = 'html')
		return
	
	try:
		if len(args) >=2:
			bot.pinChatMessage(chat.id, update.message.message_id, args)
			update.message.reply_text('<b>Message Pinned successfully✅</b>', parse_mode= 'html')
		else:
			msg = update.effective_message.reply_to_message
			bot.pinChatMessage(chat.id,msg.message_id)
			update.message.reply_text('<b>Message Pinned successfully✅</b>', parse_mode = 'html')
	except:
		update.message.reply_text('<b>Please use this command with a reply to so i will pin the reply message on this group.\n\nOtherwise type something with this commannd like this👇</b>\n\n🔹/pin (<code>Your Message</code>)🔹\n\n<b>So i will pin the message for you✅😊</b>', parse_mode = 'html')

def unpin(update,context):
	user = update.effective_user
	chat = update.effective_chat
	args = update.message.text.split(None, 1)
	if chat.type == 'private':
		update.message.reply_text("<b>Sorry but this command only work's on group's. Add me on your group to try this😊</b>", parse_mode = 'html')
		return 
	promoter = chat.get_member(user.id)

	if (
		not (promoter.status == 'administrator' or promoter.status == "creator")
    ):
		update.message.reply_text("<b>I am really sorry but you don't have the necessary rights to do that. please become an admin first!</b>", parse_mode = 'html')
		return
	if len(args) >= 2:
		if args[1] == 'all':
			bot.unpin_all_chat_messages(chat.id)
			update.message.reply_text('*All messages are now unpinned✅*',parse_mode = ParseMode.MARKDOWN)
		else:
			update.message.reply_text('<b>️️‼️Unknown value for command /unpin.\n\nHow to use this command👇\n\n 🔹/unpin🔹: For unpin last message\n🔹/unpin all🔹: For unpin all messages\n\nHope you are now understand😊</b>', parse_mode = 'html')
	else:
		bot.unpin_chat_message(chat.id)
		update.message.reply_text('*last message now has been unpinned✅*', parse_mode = ParseMode.MARKDOWN)

def promote(update, context):

    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    
    if chat.type == 'private':
    	message.reply_text("<b>I am really sorry this command only work's on group's. Add me on your group to try this😊</b>", parse_mode = 'html')
    	return

    promoter = chat.get_member(user.id)

    if (
        not (promoter.can_promote_members or promoter.status == "creator")
    ):
        message.reply_text("<b>I am really sorry but you don't have the necessary rights to do that. please become an admin first!</b>", parse_mode = 'html')
        return
    
    try:
    	user_id = update.message.reply_to_message.from_user.id
    except:
    	message.reply_text("<b>For using this command you have to send it on a reply someone's previous message. Otherwise it won't work</b>\n\n<b>Please Try again😊</b>", parse_mode = 'html')
    	return

    if not user_id:
        message.reply_text(
            "*You don't seem to be referring to a user or the ID specified is incorrect check it and then try..*", parse_mode= ParseMode.MARKDOWN
        )
        return

    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if user_member.status == "administrator" or user_member.status == "creator":
        message.reply_text("I don't need to make him admin it's because he already is an admin! ;)", parse_mode= ParseMode.MARKDOWN)
        return

    if user_id == bot.id:
        message.reply_text("*I am not able to promote myself Please get an admin to do it for me :)*", parse_mode= ParseMode.MARKDOWN)
        return

    bot_member = chat.get_member(bot.id)

    try:
        bot.promoteChatMember(
            chat.id,
            user_id,
            can_change_info=bot_member.can_change_info,
            can_post_messages=bot_member.can_post_messages,
            can_edit_messages=bot_member.can_edit_messages,
            can_delete_messages=bot_member.can_delete_messages,
            can_invite_users=bot_member.can_invite_users,
            can_restrict_members=bot_member.can_restrict_members,
            can_pin_messages=bot_member.can_pin_messages,
        )
    except BadRequest as err:
        if err.message == "User_not_mutual_contact":
            message.reply_text(" *I am really sorry but i can't promote someone who isn't in the group.*", parse_mode = ParseMode.MARKDOWN)
        else:
            message.reply_text("<b>Sorry i am not able to promote someone in here. it's because it's possible that i am not admin in here or not have permission to appoint new admins :(</b>", parse_mode = 'html')
        return

    bot.sendMessage(
        chat.id,
        f"<b>Sucessfully promoted✅ {user_member.user.first_name or user_id}!</b>",
        parse_mode='html'
    )

def demote(update, context):

    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user
    
    if chat.type == 'private':
    	message.reply_text("<b>I am really sorry this command only work's on group's. Add me on your group to try this😊</b>", parse_mode = 'html')
    	return
    
    promoter = chat.get_member(user.id)
    
    if (
        not (promoter.can_promote_members or promoter.status == "creator")
    ):
        message.reply_text("<b>I am really sorry but you don't have the necessary rights to do that. please become an admin first!</b>", parse_mode = 'html')
        return
    try:
    	user_id = update.message.reply_to_message.from_user.id
    except:
    	message.reply_text("<b>For using this command you have to send it on a reply someone's previous message. who is already an admin Otherwise it won't work\n\nPlease Try again😊</b>", parse_mode = 'html')
    	return
    	
    if not user_id:
        message.reply_text(
            "<b>You don't seem to be referring to a user or the ID specified is incorrect..</b>", parse_mode = 'html'
        )
        return

    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if user_member.status == "creator":
        message.reply_text("<b>I am really sorry but i am not able to de promote the chat creator :)</b>", parse_mode= 'html')
        return

    if not user_member.status == "administrator":
        message.reply_text("<b>There's no way i can demote someone who isn't admin on this group! : )</b>", parse_mode='html')
        return

    if user_id == bot.id:
        message.reply_text("<b>I can't de promote myself! please get a admin for do it for me : | </b>", parse_mode='html')
        return

    try:
        bot.promoteChatMember(
            chat.id,
            user_id,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
        )

        bot.sendMessage(
            chat.id,
            f"<b>Sucessfully demoted {user_member.user.first_name or user_id}</b>!",
            parse_mode=ParseMode.HTML,
        )

    except BadRequest:
        message.reply_text(
            "<b>Couldn't de promoted! it's possible that it's because i am not admin in here. otherwise the member you wan't to de promote isn't promoted by me. i am really sorry.</b>", parse_mode='html')
        return

def set_title(update, context):
    
    chat = update.effective_chat
    message = update.effective_message
    
    if chat.type == 'private':
    	message.reply_text("<b>This command only work's on a Group. add me on your group to try this command😊</b>", parse_mode = 'html' )
    	return
    
    
    title = update.message.text.split(None, 1)
    user = update.effective_user
    
    
    
    check = chat.get_member(user.id)
    
    if (not(check.status == 'administrator' or check.status == 'creator')):
    	message.reply_text("<b>I am really sorry but you don't have permission to do that. please become an admin first then try again!</b>", parse_mode='html' )
    	return
    	
    
    if not len(title) >= 2:
    	message.reply_text("<b>For using this command you have to send it on a reply someone's previous message with a title like this👇\n\n🔹/title (<code>custom title</code>)🔹\n\nPlease try again😊</b>",parse_mode = 'html')
    	return
    try:
        user_id1 = update.message.reply_to_message.from_user
        user_id = update.message.reply_to_message.from_user.id
        user_member = chat.get_member(user_id)
    except:
        message.reply_text("<b>For using this command you have to send it on a reply someone's previous message with a title like this👇\n\n🔹/title (<code>custom title</code>)🔹\n\nPlease try again😊</b>",parse_mode = 'html')
        return

    if not user_id:
        message.reply_text(
            "*You don't seem to be referring to a user or the ID specified is incorrect..*", parse_mode= ParseMode.MARKDOWN
        )
        return

    if user_member.status == "creator":
        message.reply_text("<b>I am really sorry i can't able to change the title of the chat creator :)</b>", parse_mode='html')
        return

    if not user_member.status == "administrator":
        message.reply_text("<b>I am really sorry i can't able to set custom title to non admin's\n\nMake him admin first then try again😊</b>", parse_mode = 'html' )
        return

    if user_id == bot.id:
        message.reply_text(
            "<b>I can't set my own title myself. Please get an admin to do it for me! :)</b>" , parse_mode='html'
        )
        return

    if len(title[1]) > 16:
        message.reply_text(
           "<b>I am really sorry but you can't set a title that longer then 16 character. \n\n please try it again with a less then 16 character title ;)</b>", parse_mode='html'
        )
        return

    try:
        bot.setChatAdministratorCustomTitle(chat.id, user_id, title[1])
    except BadRequest:
        message.reply_text(
            "<b>I am really sorry! But i can't set title someone who isn't promoted by me. please get and admin to do it :(</b>", parse_mode='html'
        )
        return

    message.reply_text('<b>Successfully set title for {}</b>\n\n<b>The title is</b> 🔹<code>{}</code>🔹'.format(user_id1.first_name, title[1]), parse_mode = 'html')

def rm_title(update, context):
    
    chat = update.effective_chat
    message = update.effective_message
    
    if chat.type == 'private':
    	message.reply_text("<b>This command only work's on a Group. add me on your group to try this command😊</b>", parse_mode = 'html' )
    	return
 
    user = update.effective_user
    
    
    
    check = chat.get_member(user.id)
    
    if (not(check.status == 'administrator' or check.status == 'creator')):
    	message.reply_text("<b>I am really sorry but you don't have permission to do that. please become an admin first then try again!</b>", parse_mode='html' )
    	return
    	
    try:
        user_id1 = update.message.reply_to_message.from_user
        user_id = update.message.reply_to_message.from_user.id
        user_member = chat.get_member(user_id)
    except:
        message.reply_text("<b>For using this command you have to send it on a reply someone's previous message \n\nHope you are now understand Please try again😊</b>",parse_mode = 'html')
        return

    if not user_id:
        message.reply_text(
            "*You don't seem to be referring to a user or the ID specified is incorrect..*", parse_mode= ParseMode.MARKDOWN
        )
        return

    if user_member.status == "creator":
        message.reply_text("<b>I am really sorry i can't able to remove the title of the chat creator :)</b>", parse_mode='html')
        return

    if not user_member.status == "administrator":
        message.reply_text("<b>I am really sorry i can't able to remove title to non admin's\n\nMake him admin first then try again😊</b>", parse_mode = 'html' )
        return

    if user_id == bot.id:
        message.reply_text(
            "<b>I can't remove my own title myself. Please get an admin to do it for me! :)</b>" , parse_mode='html'
        )
        return

    try:
        bot.setChatAdministratorCustomTitle(chat.id, user_id, '')
    except BadRequest:
        message.reply_text(
            "<b>I am really sorry! But i can't change someone's who isn't promoted by me. please get and admin to do it :(</b>", parse_mode='html'
        )
        return

    message.reply_text('<b>Successfully removed title of {}</b>'.format(user_id1.first_name), parse_mode = 'html')