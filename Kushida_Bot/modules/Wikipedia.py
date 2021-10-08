from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater
import wikipedia as wiki


bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

def wik(update,context):
	args = update.message.text.split(None, 1)
	if len(args) < 2:
		try:
			r_text = update.message.reply_to_message.text
			try:
				src = update.message.reply_text('<b>Fatching Details from wikipedia🔎...</b>', parse_mode = 'html')
				search = wiki.page(r_text)
				text = wiki.summary(r_text)
				link = search.url
				key = (
					InlineKeyboardMarkup(
						[
							[
								InlineKeyboardButton(
									text = (
										'More Info'
									),
									url = (
										link
									)
								)
							]
						]
					)
				)
				if len(text) > 800:
					text = text[0:800]
					src.edit_text('<b>Result: </b><i>{}...</i>'.format(text), parse_mode = 'html', reply_markup = key)
				else:
					src.edit_text('<b>Result: </b><i>{}</i>'.format(text), parse_mode = 'html')
			except:
				src.edit_text("<b>Could not find it!\nit's because its possible that the page you want to search isn't availeable on wikipedia please search with more specific keyword☑️</b>", parse_mode = 'html')
		except:
			update.message.reply_text('<b>For using this command you have to send it on a reply. Otherwise you have send it like this👇</b>\n\n🔹/wiki (<code>Your Keyword</code>)🔹\n\n<b>Dont use brakets its just for showing Please Try Again😊</b>', parse_mode = 'html')
			return 
	else:
		src = update.message.reply_text('<b>Fatching Details from wikipedia🔎...</b>', parse_mode = 'html')
		try:
			search = wiki.page(args[1])
			text = wiki.summary(args[1])
			link = search.url
			key = (
				InlineKeyboardMarkup(
					[
						[
							InlineKeyboardButton(
								text = (
									'More Info'
								),
								url = (
									link
								)
							)
						]
					]
				)
			)
			if len(text) > 800:
				text = text[0:800]
				src.edit_text('<b>Result: </b><i>{}...</i>'.format(text), parse_mode = 'html', reply_markup = key)
			else:
				src.edit_text('<b>Result: </b><i>{}</i>'.format(text), parse_mode = 'html')
		except:
			src.edit_text("<b>Could not find it!\nit's because its possible that the page you want to search isn't availeable on wikipedia please search with more specific keyword☑️</b>", parse_mode = 'html')