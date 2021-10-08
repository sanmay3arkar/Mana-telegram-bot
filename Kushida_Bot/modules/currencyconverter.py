from currency_converter import CurrencyConverter
from telegram import Bot
from telegram.ext import Updater


bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

converter = CurrencyConverter()

def convert(update,context):
	txt = update.message.text.upper()
	args = txt.split()
	
	
	if len(args) < 4:
		update.message.reply_text('<b>Less value Entered!! Expected 4.\nFor using this Command you have to send it like this👇</b>\n\n🔹/convert (<code>EUR USD 10)</code>🔹\n\n <b>here the first one is the currency that you want to convert, the second one is the converted currency, the third one is the amount. Dont use brakets its for showing.😊</b>', parse_mode = 'html')
		return 
	elif len(args) > 4:
		update.message.reply_text('<b>More then expected value Entered!! Expected 4.\nFor using this Command you have to send it like this👇</b>\n\n🔹/convert (<code>EUR USD 10</code>)🔹\n\n <b>here the first one is the currency that you want to convert, the second one is the converted currency, the third one is the amount. Dont use brakets its for showing.😊</b>', parse_mode = 'html')
		return
	else:
		try:
			value = converter.convert(args[3], args[1], args[2])
			update.message.reply_text('<code>{}</code> <b>{} = </b><code>{}</code> <b>{}</b>'.format(args[3], args[1], value, args[2]), parse_mode = 'html')
		except:
			update.message.reply_text("<b>I Can't Able to Convert it. make sure you entered All value correct. and make sure the currency names are all capital letter.</b>", parse_mode = 'html')	