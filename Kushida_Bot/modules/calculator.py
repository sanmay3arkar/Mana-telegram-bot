from telegram import Bot
from telegram.ext import Updater

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

def solve(update,context):
	mes = update.message.text.split(None, 1)
	if len(mes) < 2:
		update.message.reply_text('<b>For Using This command you have to send it like this👇</b>\n\n🔹/solve (<code>10 + 10</code>)🔹\n\n<b>Do not use brakets its just for showing. Please try again😊</b>', parse_mode = 'html')
		return
	
	try:
		mess = eval(mes[1])
		mess = str(mess)
	except:
		update.message.reply_text("<b>Invalid Value entered‼️\nMake sure you entered Only numbers and ‘+ , - , * , /’. here ‘+’ = PLUS, and ‘-’ = MINUS, ‘*’ = MULTIPLY, ‘/’ = DIVIDE. that should be used on simple equations.\n\nPlease Try again😊</b>", parse_mode = 'html')
		return
	update.message.reply_text("<b>The Answer is 🔹<code>{}</code>🔹</b>".format(mess), parse_mode='html')

