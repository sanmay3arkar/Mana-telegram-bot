from telegram import Bot, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
from deep_translator import GoogleTranslator as gltr



bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

key = InlineKeyboardMarkup(
	[
		[
			InlineKeyboardButton(
				text = "Supported languages",
				url= "https://telegra.ph/Short-Form-of-Languages-06-30"
			)
		]
	]
)


def tr(update,context):
	args = update.message.text.split(None, 1)
	m = update.message.reply_text('*Translating...*', parse_mode = ParseMode.MARKDOWN)
	if len(args) < 2:
		try:
			tr_t = update.message.reply_to_message.text
		except:
			m.edit_text("<b>For using this command you have to send it on a reply of someones previous sended message. otherwise send it like this👇</b>\n\n🔹/tr (<code>Your Text</code>)🔹\n\n<b>So i will translate it on english. dont use brakets its just for showing please try again😊</b>", parse_mode = 'html')
			return 
	else:
		tr_t = args[1]
	
	try:
		m_tr = gltr(source='auto', target='en').translate(tr_t)
	except:
		m.edit_text("<b>Cant able to translate it! Please Check you word or please try to translate anything else. please try again😊</b>", parse_mode = 'html')
		return 
	
	if m_tr == tr_t:
		m.edit_text('<b>i am really sorry! but language not recognised. Make sure you use the language word instead of English. i mean like in japanese your text must be like this this (おはよう) not like this (Ohayo). please try again😊</b>', parse_mode = 'html')
		return 
	m.edit_text("<b>In English it Means</b> 🔹<code>{}</code>🔹".format(m_tr), parse_mode = 'html')
	
def gtr(update,context):
	am = update.message.reply_text('*Translating...*', parse_mode = ParseMode.MARKDOWN)
	args = update.message.text.split(None,1)
	if len(args) < 2:
		am.edit_text("<b>I am sorry but you havent mentioned the translated language! \nFor using this command you have to to send it on a reply of someones previous message like this👇</b>\n\n🔹/gtr ( <code>ja</code> )🔹\n\n<b>Here the (ja) means Japanese so you have to specify the language. otherwise send it like this👇</b>\n\n🔹/gtr ( <b>ja</b> <code>Text</code> )🔹\n\n<b>Here the (Text) is the text you want to translate and the (ja) is the translated language.\n\nFor knowing supported languages click the button below🔽</b>", parse_mode = 'html', reply_markup = key)
		return
	
	t_txt = args[1].split(' ', 1)
	
	if len(t_txt) < 2:
		try:
			txt = update.message.reply_to_message.text
			lng = args[1]
		except:
			am.edit_text("<b>For using this command you have to to send it on a reply of someones previous message like this👇</b>\n\n🔹/gtr ( <code>ja</code> )🔹\n\n<b>Here the (ja) means Japanese so you have to specify the language. otherwise send it like this👇</b>\n\n🔹/gtr ( <b>ja</b><code> Text</code> )🔹\n\n<b>Here the (Text) is the text you want to translate and the (ja) is the translated language.\n\nFor knowing supported languages click the button below🔽</b>", parse_mode = 'html', reply_markup = key)
			return
	else:
		txt = t_txt[1]
		lng = t_txt[0]
	
	lng = lng.lower()
	
	try:
		m_gtr = gltr(source='auto', target=lng).translate(txt)
	except:
		am.edit_text("<b>Cant able to translate it!! make sure you entered language short form correct.\n\nFor knowing supported languages click the button below🔽</b>", parse_mode = 'html', reply_markup = key)
		return 
	
	if m_gtr == txt:
		am.edit_text('<b>i am really sorry! but language not recognised. Make sure you wont use the output language on the input. i mean like in japanese your text must be like this this (おはよう) not like this (Ohayo). please try again😊</b>', parse_mode = 'html')
		return 
	
	am.edit_text("<b>Translated to [</b><code>{}</code><b>] : </b>🔹<code>{}</code>🔹".format(lng, m_gtr), parse_mode = 'html')
