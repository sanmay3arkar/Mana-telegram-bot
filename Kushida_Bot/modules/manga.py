import anilistpy as a
from telegram import Bot, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

def mangaa(update,context):
	args = update.message.text.split(None, 1)
	find = update.message.reply_text('*Finding for you🔎....*', parse_mode= ParseMode.MARKDOWN )
	if len(args) >= 2:
		try:
		
			searchM = a.mangaSearch(args[1])
			mangaObj = a.Manga(searchM.id(0))
			manga = mangaObj.json()
		
		
		
		
			name = manga['data']['Page']['media'][0]['title']['english']
			jps = manga['data']['Page']['media'][0]['title']['native']
			types = 'MANGA'

		
			stat = manga['data']['Page']['media'][0]['status']

	
			chp = manga['data']['Page']['media'][0].get('chapters', None)
			if chp:
				mchp = manga['data']['Page']['media'][0]['chapters']
				mchp = str(mchp)
			else:
				mchp = "none"
			
		
			ge = manga['data']['Page']['media'][0]['genres']
			gen = ", "
			gen = gen.join(ge)	
		
			img = manga['data']['Page']['media'][0]['coverImage']['extraLarge']
		
			scr = manga['data']['Page']['media'][0]['averageScore']
			scr = str(scr)
		
			sour = manga['data']['Page']['media'][0]['source']
		
			str_date = manga['data']['Page']['media'][0]['startDate']['year']
			str_date = str(str_date)
		
			des = manga['data']['Page']['media'][0]['description']
		
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
		
			hurl = manga['data']['Page']['media'][0]['id']
			hurl = str(hurl)
			url = "https://anilist.co/manga/" + hurl
		
			keys = InlineKeyboardMarkup([[
		InlineKeyboardButton('More Info', url = url)]])
		
			find.delete()
			if len(des) >= 500:
				if mchp == 'none':
					update.message.reply_photo(img, '<b>📕 : ' + name + '</b>' + ' (' + jps + ')\n\n' + '<b>📅 : START DATE: </b>' + '<i>' + str_date + '</i>' + '\n' + '<b>👀 : TYPE: </b>' + '<i>' + types + '</i>' + '\n' + '<b>📡 : STATUS: </b>' + '<i>' + stat + '</i>' + '\n'+ '<b>📝 : SCORE: </b>' + '<i>' + scr + '</i>' + '\n' + '<b>📚 : CHAPTER: </b>' + '<i>NONE</i>\n'  + '<b>💻 : SOURCE: </b>' + '<i>' + sour + '</i>\n' + '<b>🎭 : GENRE: </b>'+ '<code>' + gen +'</code>' + '\n\n' + '<b>📄 : DESCRIPTION: </b>' + '<i>' + des + '...<a href = "{}">Read More</a></i>'.format(url) , reply_markup = keys, parse_mode = 'html')
				else:
					update.message.reply_photo(img, '<b>📕 : ' + name + '</b>' + ' (' + jps + ')\n\n' + '<b>📅 : START DATE: </b>' + '<i>' + str_date + '</i>' + '\n' + '<b>👀 : TYPE: </b>' + '<i>' + types + '</i>' + '\n' + '<b>📡 : STATUS: </b>' + '<i>' + stat + '</i>' + '\n'+ '<b>📝 : SCORE: </b>' + '<i>' + scr + '</i>' + '\n' + '<b>📚 : CHAPTER: </b>' + '<i>' + mchp + '</i>\n' + '<b>💻 : SOURCE: </b>' + '<i>' + sour + '</i>\n' + '<b>🎭 : GENRE: </b>'+ '<code>' + gen +'</code>' + '\n\n' + '<b>📄 : DESCRIPTION: </b>' + '<i>' + des + '.. <a href = "{}">Read More</a></i>'.format(url) , reply_markup = keys, parse_mode = 'html')
			else:
				if mchp == 'none':
					update.message.reply_photo(img, '<b>📕 : ' + name + '</b>' + ' (' + jps + ')\n\n' + '<b>📅 : START DATE: </b>' + '<i>' + str_date + '</i>' + '\n' + '<b>👀 : TYPE: </b>' + '<i>' + types + '</i>' + '\n' + '<b>📡 : STATUS: </b>' + '<i>' + stat + '</i>' + '\n'+ '<b>📝 : SCORE: </b>' + '<i>' + scr + '</i>' + '\n' + '<b>📚 : CHAPTER: </b>' + '<i>NONE</i>\n'  + '<b>💻 : SOURCE: </b>' + '<i>' + sour + '</i>\n' + '<b>🎭 : GENRE: </b>'+ '<code>' + gen +'</code>' + '\n\n' + '<b>📄 : DESCRIPTION: </b>' + '<i>' + des + '</i>' , reply_markup = keys, parse_mode = 'html')
				else:
					update.message.reply_photo(img, '<b>📕 : ' + name + '</b>' + ' (' + jps + ')\n\n' + '<b>📅 : START DATE: </b>' + '<i>' + str_date + '</i>' + '\n' + '<b>👀 : TYPE: </b>' + '<i>' + types + '</i>' + '\n' + '<b>📡 : STATUS: </b>' + '<i>' + stat + '</i>' + '\n'+ '<b>📝 : SCORE: </b>' + '<i>' + scr + '</i>' + '\n' + '<b>📚 : CHAPTER: </b>' + '<i>' + mchp + '</i>\n' + '<b>💻 : SOURCE: </b>' + '<i>' + sour + '</i>\n' + '<b>🎭 : GENRE: </b>'+ '<code>' + gen +'</code>' + '\n\n' + '<b>📄 : DESCRIPTION: </b>' + '<i>' + des + '</i>' , reply_markup = keys, parse_mode = 'html')
		except:
			
			find.edit_text("<b>I am really sorry.\n\nI tried my best to find it but i could not find it. It's because this manga does not exist or the entered name isn't correct.\n\nPlease try again with another manga name or correct the sended manga name and send again👍😊</b>", parse_mode = 'html')
	else:
		find.edit_text("<b>Please provide with Manga name Like this👇</b>\n\n🔹/manga <code>(Manga Name)</code>🔹\n\n<b> Please try again😊</b>", parse_mode = 'html')