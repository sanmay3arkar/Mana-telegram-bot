import requests
from telegram import Bot, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

airing_query = '''
    query ($id: Int,$search: String) { 
      Media (id: $id, type: ANIME,search: $search) { 
        id
        episodes
        title {
          romaji
          english
          native
        }
        coverImage {
        extraLarge
      }
      description
        siteUrl
        nextAiringEpisode {
           airingAt
           timeUntilAiring
           episode
        } 
      }
    }
    '''
url = 'https://graphql.anilist.co'


def air(update,context):
	args = update.message.text.split(None, 1)
	find = update.message.reply_text('*Finding for you🔎....*', parse_mode= ParseMode.MARKDOWN )
	if len(args) >= 2:
		try: 
			variables = {'search': args[1]}
			airing = requests.post(
        url, json={'query': airing_query, 'variables': variables}).json()['data']['Media']	
		
			name = airing['title']['english']
			jps = airing['title']['native']
			img = airing['coverImage']['extraLarge']
			eps = airing['episodes']
			eps = str(eps)
			sturl = airing['siteUrl']
			n_air_ep = airing['nextAiringEpisode']['episode']
			n_air_ep = str(n_air_ep)
			des = airing['description']
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
			if len(des) > 200:
				des = des[0:200]
			n_episode1 = airing['nextAiringEpisode']['timeUntilAiring']
			seconds = n_episode1 * 1000

			d =1000 * 60 * 60 * 24
			h =1000 * 60 * 60
			m = 1000 * 60
			sec = 1000


			days = seconds // d
			hours = (seconds - (days * d)) // h
			minutes = (seconds - (days * d) - (hours * h)) // m
			second = (seconds - (days * d) -( hours * h) - (minutes * m)) // sec
		
			days = str(days)
			hours = str(hours)
			minutes = str(minutes)
			second = str(second)
		
			n_episode = (days + ' Days, ' + hours + ' Hours, ' + minutes + ' Minutes, ' + second + ' Seconds ')
			keys = InlineKeyboardMarkup([[
			InlineKeyboardButton('More Info', url = sturl)]])
			
			find.delete()
			if len(des) >= 200:
				update.message.reply_photo(img, '<b>📺 : ' + name + '</b>' + '(' + jps + ')\n\n' + '<b>🗓 : TOTAL EPISODES: </b>' + '<i>' + eps + '</i>\n' + '<b>⏭ : NEXT AIRING EPISODE: </b>' + '<i>' + n_air_ep + '</i>\n' + '<b>📅 : AIRING IN: </b>' + '<code>' + n_episode + '</code>\n\n' + '📄 : DESCRIPTION: ' + '<i>' + des + '...<a href = "{}">Read More</a></i>'.format(sturl), reply_markup = keys, parse_mode = 'html')
			else:
				update.message.reply_photo(img, '<b>📺 : ' + name + '</b>' + '(' + jps + ')\n\n' + '<b>🗓 : TOTAL EPISODES: </b>' + '<i>' + eps + '</i>\n' + '<b>⏭ : NEXT AIRING EPISODE: </b>' + '<i>' + n_air_ep + '</i>\n' + '<b>📅 : AIRING IN: </b>' + '<code>' + n_episode + '</code>\n\n' + '📄 : DESCRIPTION: ' + '<i>' + des + '</i>', reply_markup = keys, parse_mode = 'html')
			
		except:
			find.edit_text("<b>I am really sorry.\n\nI tried my best to find it but i could not find it. It's because currently this anime isn't airing or the entered name isn't correct.\n\nPlease try again with another anime name or correct the sended anime name and send again👍😊</b>", parse_mode = 'html')
	
	else:
		find.edit_text("<b>Please provide with airing anime name Like this👇</b>\n\n🔹/airing <code>(Airing Anime Name)</code>🔹\n\n<b> Please try again😊</b>", parse_mode = 'html')
		