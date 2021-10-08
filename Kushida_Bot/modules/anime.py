import anilistpy as a
from telegram import Bot, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater


bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

def xxx(update,context):
	args = update.message.text.split(None, 1)
	find = update.message.reply_text('*Finding for you🔎....*', parse_mode= ParseMode.MARKDOWN )
	if len(args) >= 2:
		try:
			searchA = a.animeSearch(args[1])
			anim_object = a.Anime(searchA.id(0))
			anime = anim_object.json()
		
			name = anime['data']['Page']['media'][0]['title']['english']
			jps = anime['data']['Page']['media'][0]['title']['native']
			types = anime['data']['Page']['media'][0]['format']

		
			stat = anime['data']['Page']['media'][0]['status']

	
			dur = anime['data']['Page']['media'][0]['duration']
			dur = str(dur)
		
			ge = anime['data']['Page']['media'][0]['genres']
			gen = ", "
			gen = gen.join(ge)	
		
			img = anime['data']['Page']['media'][0]['coverImage']['extraLarge']
		
			scr = anime['data']['Page']['media'][0]['averageScore']
			scr = str(scr)
		
			sour = anime['data']['Page']['media'][0]['source']
		
			des = anime['data']['Page']['media'][0]['description']
		
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
			if len(des) > 500:
				des = des[0:500]
			
		
			epi = anime['data']['Page']['media'][0]['episodes']
			epi = str(epi)
			
		
			std = ""
			for st in anime['data']['Page']['media'][0]['studios']['nodes']:
				std = (std) + st['name'] + ", "
	
			find.delete()
		
			hurl = anime['data']['Page']['media'][0]['id']
			hurl = str(hurl)
			url1 = "https://anilist.co/anime/" + hurl
		
			url2 = anime['data']['Page']['media'][0].get('trailer', None)
			if url2:
				url3 = "https://youtu.be/" + anime['data']['Page']['media'][0]['trailer']['id']
			else:
				url3 = 'None'
			
			if url3 == 'None':
				keys = InlineKeyboardMarkup([[InlineKeyboardButton("More Info", url = url1 )]])
			else:
				keys = InlineKeyboardMarkup([[InlineKeyboardButton("More Info", url = url1 ), InlineKeyboardButton('Trailer🎬', url = url3)]])
			
			if len(des) >= 500:
				update.message.reply_photo(img, '<b>📺 : ' + name +'</b>'+ ' (' + jps + ')\n\n' + '<b>👀 : TYPE: </b>' + '<i>' + types + '</i>' + '\n' + '<b>📡 : STATUS: </b>' + '<i>' + stat + '</i>\n' + '<b>🗓 : EPISODE: </b>' + '<i>' + epi + '</i>' + '\n' + '<b>⏱ : DURATION: </b>' + '<i>' + dur + ' m per episode' + '</i>' + '\n' +'<b>📝 : SCORE: </b>' + '<i>' + scr + '</i>' + '\n' + '<b>💻 : SOURCE: </b>' + '<i>' + sour + '</i>' + '\n' + '<b>🎭 : GENRE: </b>' + '<code>' + gen + '</code>' + '\n' + '<b>🎬 : STUDIOS: </b>' + '<i>' + std + '</i>\n\n<b>📄 : DESCRIPTION: </b>' + '<i>' + des + '...<a href ="{}">Read More</a></i>'.format(url1),reply_markup = keys, parse_mode = 'html')
			else:
				update.message.reply_photo(img, '<b>📺 : ' + name +'</b>'+ ' (' + jps + ')\n\n' + '<b>👀 : TYPE: </b>' + '<i>' + types + '</i>' + '\n' + '<b>📡 : STATUS: </b>' + '<i>' + stat + '</i>\n' + '<b>🗓 : EPISODE: </b>' + '<i>' + epi + '</i>' + '\n' + '<b>⏱ : DURATION: </b>' + '<i>' + dur + ' m per episode' + '</i>' + '\n' +'<b>📝 : SCORE: </b>' + '<i>' + scr + '</i>' + '\n' + '<b>💻 : SOURCE: </b>' + '<i>' + sour + '</i>' + '\n' + '<b>🎭 : GENRE: </b>' + '<code>' + gen + '</code>' + '\n' + '<b>🎬 : STUDIOS: </b>' + '<i>' + std + '</i>\n\n<b>📄 : DESCRIPTION: </b>' + '<i>' + des + '</i>',reply_markup = keys, parse_mode = 'html')
		except:
			find.edit_text("<b>I am really sorry.\n\nI tried my best to find it but i could not find it. It's because this anime does not exist or the entered name isn't correct.\n\nPlease try again with another anime name or correct the sended anime name and send again👍😊</b>", parse_mode = 'html')
	else:
		find.edit_text("<b>Please provide with anime name Like this👇</b>\n\n🔹/anime <code>(Anime Name)</code>🔹\n\n<b> Please try again😊</b>", parse_mode = 'html')