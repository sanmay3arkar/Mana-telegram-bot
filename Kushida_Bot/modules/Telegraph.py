import telegraph
from telegraph import upload
from telegram import Bot
from telegram.ext import Updater
from Kushida_Bot.modules.helper_function.list_dict import TELE
import random as r
import shutil

tele = telegraph.Telegraph()
bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

tele.create_account(short_name= r.choice(TELE))

def tgn(update,context):
	args = update.message.text.split(None,1)
	try:
		args1 = args[1].split(':', 1)
	except:
		update.message.reply_text('<b>Not Enough Value Entered!!\nFor using this command You have to send it like this on a previous message reply👇</b>\n\n🔹/tgn (<code>Note Title</code>)🔹.\n\n<b>Otherwise Send it like this👇</b>\n\n🔹/tgn (<code>Note Title : Your Note</code>)🔹\n\n<b>Make Sure you used the : symbol after note title its important😊</b>', parse_mode = 'html')
		return 
	
	if len(args1) < 2:
		if len(args1) <1:
			update.message.reply_text('<b>Not Enough Value Entered!!\nFor using this command You have to send it like this on a previous message reply👇</b>\n\n🔹/tgn (<code>Note Title</code>)🔹.\n\n<b>Otherwise Send it like this👇</b>\n\n🔹/tgn (<code>Note Title : Your Note</code>)🔹\n\n<b>Make Sure you used the : symbol after note title its important😊</b>', parse_mode = 'html')
			return 
		else:
			try:
				text = update.message.reply_to_message.text
			except:
				update.message.reply_text('<b>Not able to upload it!\nFor using this command You have to send it like this on a previous message reply👇</b>\n\n🔹/upnote (<code>Note Title</code>)🔹.\n\n<b>Otherwise Send it like this👇</b>\n\n🔹/upnote (<code>Note Title : Your Note</code>)🔹\n\n<b>Make Sure you used the : symbol after note title its important😊</b>', parse_mode = 'html')
				return 
			wait = update.message.reply_text('<b>Creating telegraph page📄...</b>', parse_mode = 'html')
			page = tele.create_page(args1[0], html_content=text)
			link = 'https://telegra.ph/{}'.format(page['path'])
			wait.edit_text('<b>🔻Here is your page link🔻</b>\n\n<b>♦️{}</b>'.format(link), parse_mode = 'html', disable_web_page_preview= True)
			
	else:
		wait = update.message.reply_text('<b>Creating telegraph page📄...</b>', parse_mode = 'html')
		page = tele.create_page(args1[0], html_content=args1[1])
		link = 'https://telegra.ph/{}'.format(page['path'])
		wait.edit_text('<b>🔻Here is your page link🔻</b>\n\n<b>♦️{}</b>'.format(link), parse_mode = 'html', disable_web_page_preview = True)


def tgp(update,context):
	user = update.effective_user
	try:
		mes = update.message.reply_text('<b>Uploading the photo🏞...</b>', parse_mode = 'html')
		file1 = shutil.os.listdir('Kushida_Bot/modules/helper_function/telegraph/')
		
		if '{}.jpg'.format(user.id) not in file1:
			update.message.reply_to_message.photo[-1].get_file().download('Kushida_Bot/modules/helper_function/telegraph/{}.jpg'.format(user.id)) 
		else:
			shutil.os.remove('Kushida_Bot/modules/helper_function/telegraph/{}.jpg'.format(user.id))
			update.message.reply_to_message.photo[-1].get_file().download('Kushida_Bot/modules/helper_function/telegraph/{}.jpg'.format(user.id))
		
		file1 = shutil.os.listdir('Kushida_Bot/modules/helper_function/telegraph/')
		if '{}.jpg'.format(user.id) in file1:
			file2 = open('Kushida_Bot/modules/helper_function/telegraph/{}.jpg'.format(user.id), 'rb')
			file = telegraph.upload.upload_file(file2)
			mes.edit_text("<b>🔻Here is your File link🔻\n\n♦️{}</b>".format('https://telegra.ph{}'.format(file[0])), parse_mode = 'html', disable_web_page_preview = True)
			shutil.os.remove('Kushida_Bot/modules/helper_function/telegraph/{}.jpg'.format(user.id))
	except:
		mes.edit_text("<b>Can't able to upload it!😔\nMake sure you send this command on a reply of previously sended photo. and make sure its not a video file.</b>", parse_mode = 'html')
		return 

def tgv(update,context):
	user = update.effective_user
	try:
		mes = update.message.reply_text('<b>Uploading the video📹...</b>', parse_mode = 'html')
		file1 = shutil.os.listdir('Kushida_Bot/modules/helper_function/telegraph/')
		
		if '{}.mp4'.format(user.id) not in file1:
			update.message.reply_to_message.video.get_file().download('Kushida_Bot/modules/helper_function/telegraph/{}.mp4'.format(user.id)) 
		else:
			shutil.os.remove('Kushida_Bot/modules/helper_function/telegraph/{}.mp4'.format(user.id))
			update.message.reply_to_message.video.get_file().download('Kushida_Bot/modules/helper_function/telegraph/{}.mp4'.format(user.id))
		
		file1 = shutil.os.listdir('Kushida_Bot/modules/helper_function/telegraph/')
		if '{}.mp4'.format(user.id) in file1:
			file2 = open('Kushida_Bot/modules/helper_function/telegraph/{}.mp4'.format(user.id), 'rb')
			mes.edit_text('<b>About to complete📹...</b>', parse_mode = 'html')
			file = telegraph.upload.upload_file(file2)
			mes.edit_text("<b>🔻Here is your File link🔻\n\n♦️{}</b>".format('https://telegra.ph{}'.format(file[0])), parse_mode = 'html', disable_web_page_preview = True)
			shutil.os.remove('Kushida_Bot/modules/helper_function/telegraph/{}.mp4'.format(user.id))
	except:
		mes.edit_text("<b>Can't able to upload it!😔\nMake sure you send this command on a reply of previously sended video. and make sure the file is a video file.</b>", parse_mode = 'html')
		return
		
	
	