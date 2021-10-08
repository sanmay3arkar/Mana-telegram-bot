from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater
from youtubesearchpython import VideosSearch as video
import youtube_dl
import os


bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

def song(update,context):
	args = update.message.text.split(None, 1)
	find = update.message.reply_text('<b>Searching the Song🔎....</b>', parse_mode = 'html')
	if len(args) >= 2:
		try:
			vid = video(args[1], limit=1)
			name1 = "Kushida_Bot/modules/helper_function/YouTube/{}".format(vid.result()['result'][0]['title'])
			name = name1 + '.mp3'
			link = vid.result()['result'][0]['link']
			
			ydl_opt = {'outtmpl': name, 'format': 'bestaudio'}
			find.edit_text('<b>Downloading the Song⬇....</b>', parse_mode = 'html')
			with youtube_dl.YoutubeDL(ydl_opt) as ydl:
				ydl.extract_info(link)
			media = open(name, 'rb')
			find.edit_text('*Uploading the Song for you📲....*', parse_mode = ParseMode.MARKDOWN)
			update.message.reply_audio(media)
			find.delete()
			os.remove(name)
		except:
			find.edit_text("<b>I am really sorry.\n\nI tried my best to find it but i could not find it. It's because this song isn't availeable on YouTube or the entered name isn't correct.\n\nPlease try again with another song name or correct the sended song name and send it again👍😊</b>", parse_mode = 'html')
	else:
		find.edit_text("<b>Please provide with song name Like this👇</b>\n\n🔹/song <code>(Song Name)</code>🔹\n\n<b> Please try again😊</b>", parse_mode = 'html')


def videos(update,context):
	args1 = update.message.text.split(None, 1)
	find1 = update.message.reply_text('<b>Searching the Video🔎....</b>', parse_mode = 'html')
	if len(args1) >= 2:
		try:
			vid1 = video(args1[1], limit=1)
			name2 = "Kushida_Bot/modules/helper_function/YouTube/{}".format(vid1.result()['result'][0]['title'])
			name1 = name2 + '.mp4'
			link1 = vid1.result()['result'][0]['link']
			
			ydl_opt1 = {'outtmpl': name1}
			find1.edit_text('<b>Downloading the Video⬇....</b>', parse_mode = 'html')
			with youtube_dl.YoutubeDL(ydl_opt1) as ydl1:
				ydl1.extract_info(link1)
			media1 = open(name1, 'rb')
			find1.edit_text('*Uploading the Video for you📲....*', parse_mode = ParseMode.MARKDOWN)
			keys = InlineKeyboardMarkup([[
			InlineKeyboardButton('More Info', link1)]])
			update.message.reply_video(media1, reply_markup = keys, parse_mode = 'html')
			find1.delete()
			os.remove(name1)
		except:
			find1.edit_text("<b>I am really sorry.\n\nI tried my best to find it but i could not find it. It's because this video isn't availeable on YouTube or the entered name isn't correct.\n\nPlease try again with another video name or correct the sended video name and send it again👍😊</b>", parse_mode = 'html')
	else:
		find1.edit_text("<b>Please provide with video name Like this👇</b>\n\n🔹/video <code>(Video Name)</code>🔹\n\n<b> Please try again😊</b>", parse_mode = 'html')