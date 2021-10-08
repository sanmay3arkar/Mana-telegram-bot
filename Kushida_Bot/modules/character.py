import anilistpy as a

from telegram import Bot, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater


bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

def chara(update,context):
	args = update.message.text.split(None, 1)
	find = update.message.reply_text('*Finding for you🔎....*', parse_mode= ParseMode.MARKDOWN )
	
	if len(args) >= 2:
		try:
			searchC = a.charSearch(args[1])
			search_char = a.Character(searchC.id(0))
			character = search_char.json()
		
			name = character['data']['Character']['name']['full']
		
			jps = character['data']['Character']['name']['native']
		
			img = character['data']['Character']['image']['large']
			des = character['data']['Character']['description']
		
			if '<br>' in des:
				des = des.replace("<br>", "")
			if '<i>' in des:
				des = des.replace('<i>', '')
				des = des.replace('</i>', '')
			if '<u>' in des:
				des = des.replace('<u>', '')
				des = des.replace('</u>', '')
			if '<b>' in des:
				des = des.replace('<b>', '')
				des = des.replace('</b>', '')
			if '<' in des:
				des = des.replace('<', '')
			if '>' in des:
				des.replace('>', '')
			if len(des) > 300:
				des = des[0:300]
		
			url1 = character['data']['Character']['siteUrl']
		
			keys = InlineKeyboardMarkup([[
		InlineKeyboardButton('More Info', url = url1)]])
			
			fav = character['data']['Character']['favourites']
			fav = str(fav)
		
			find.delete()
		
			if len(des) >= 300:
				update.message.reply_photo(img, '<b>🔷 : ' + name + '</b>' + '(' + jps + ')\n\n' + '<b>😍 : FAVOURITES: </b>' + '<i>' + fav + '</i>\n\n' + '<b>📄 : DESCRIPTION: </b>' + '<i>' + des + '...<a href = "{}">Read More</a></i>'.format(url1), reply_markup = keys, parse_mode = 'html')
			else:
				update.message.reply_photo(img, '<b>🔷 : ' + name + '</b>' + '(' + jps + ')\n\n' + '<b>😍 : FAVOURITES: </b>' + '<i>' + fav + '</i>\n\n' + '<b>📄 : DESCRIPTION: </b>' + '<i>' + des + '</i>', reply_markup = keys, parse_mode = 'html')
		
		except:
			find.edit_text("<b>I am really sorry.\n\nI tried my best to find it but i could not find it. It's because this character does not exist or the entered name isn't correct.\n\nPlease try again with another character name or correct the sended character name and send again👍😊</b>", parse_mode = 'html')
			
	else:
		find.edit_text("<b>Please provide with character name Like this👇</b>\n\n🔹/character <code>(Character Name)</code>🔹\n\n<b> Please try again😊</b>", parse_mode = 'html')

