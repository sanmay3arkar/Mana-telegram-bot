from telegram import (
Bot,
InlineKeyboardMarkup,
InlineKeyboardButton,
ParseMode)
from telegram.ext import (
Updater, 
CommandHandler, 
CallbackQueryHandler, ConversationHandler,
MessageHandler,
Filters)
from telegram.utils import helpers
from Kushida_Bot.modules import(
console,
admin,
bans,
Info,
anime,
manga,
character,
airing,
calculator,
blacklist,
chatbot,
currencyconverter,
fun,
games,
mute,
notes,
reverse,
rules,
Telegraph,
translate,
warning,
welcome,
Wikipedia,
YouTube,
search)
import asyncio

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

FIRST, SECOND = range(2)

def start(update,context):
	user = update.effective_user
	chat = update.effective_chat
	url = helpers.create_deep_linked_url(bot.username, 'help_private')
	url1 = helpers.create_deep_linked_url(bot.username, 'add', group = True)
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					text = '➕ Add to your Group',
					url = url1
				)
			],
			[
				InlineKeyboardButton(
					text = 'Support💬',
					url ='https://t.me/Nagase_Mana_Support'
				),
				InlineKeyboardButton(
					text = 'Updates🔄',
					url = 'https://t.me/Nagase_Mana_Updates'
				)
			],
			[
				InlineKeyboardButton(
					text = "Network🌐",
					url = "https://t.me/Phantoms_Network"
				)
			],
			[
				InlineKeyboardButton(
					text = 'Help',
					url = url
				)
			]
		]
	)
	if chat.type == "private":
		img = "https://telegra.ph/file/f367b8f31c224fa3cf3a3.jpg"
		update.message.reply_photo(img, caption = "<b>Helo there {}!! I am Mana Nagase.\n\nNice to meet you😊\n\nIf you want me to manage your group then add me on your group. Click the “Help” button if you want to know how to use me😊</b>".format(user.first_name), parse_mode = 'html', reply_markup = key)
	else:
		key1 = InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						text = "Full Song",
						url = 'https://youtu.be/7bPgTVea4Fo'
					)
				]
			]
		)
		img = "https://telegra.ph/file/f367b8f31c224fa3cf3a3.jpg"
		update.message.reply_photo(img, caption = "<b>Heya!! I am here...\n\nMy name is Mana Nagase.\n\nWanna hear my song then play the music below😊</b>", parse_mode = 'html')
		msg = open("Kushida_Bot/modules/helper_function/song for you （サニーピースver.）.mp3", 'rb')
		update.message.reply_audio(msg, reply_markup = key1)

def heelp(update,context):
	chat = update.effective_chat
	if chat.type != 'private':
		url = helpers.create_deep_linked_url(bot.username, 'help_keyboard')
		hkey = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					text = 'Support Chat 💬',
					url = 'https://t.me/Nagase_Mana_Support'
				)
			],
			[
				InlineKeyboardButton(
					text = 'Help',
					url = url
				)
			]
		]
	)
		update.message.reply_text("<b>If you want to know how to use my command\n\nThen you can click the help button below. \n\nor if you have any tecnical question then click the support chat button😊</b>", parse_mode = 'html', reply_markup = hkey)
		return
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				text = 'AFK',
				callback_data = '1'
				),
				InlineKeyboardButton(
				text = 'Admin',
				callback_data = '2'
				),
				InlineKeyboardButton(
				text = 'Disabling',
				callback_data = '3'
				),
			],
			[
				InlineKeyboardButton(
				text = 'BlackList',
				callback_data = '4'
				),
				InlineKeyboardButton(
				text = 'Bans',
				callback_data = '5'
				),
				InlineKeyboardButton(
				text = 'Rules',
				callback_data = '6'
				),
			],
			[
				InlineKeyboardButton(
				text = 'Anime',
				callback_data = '7'
				),
				InlineKeyboardButton(
				text = 'Music DL',
				callback_data = '8'
				),
				InlineKeyboardButton(
				text = 'Video DL',
				callback_data = '9'
				),
			],
			[
				InlineKeyboardButton(
				text = 'Info',
				callback_data = '10'
				),
				InlineKeyboardButton(
				text = 'Search',
				callback_data = '11'
				),
				InlineKeyboardButton(
				text = 'Wikipedia',
				callback_data = '12'
				),
			],
			[
				InlineKeyboardButton(
				text = 'Fun',
				callback_data = '13'
				),
				InlineKeyboardButton(
				text = 'ChatBot',
				callback_data = '14'
				),
				InlineKeyboardButton(
				text = 'Games',
				callback_data = '15'
				),
			],
			[
				InlineKeyboardButton(
				text = 'Calculator',
				callback_data = '16'
				),
				InlineKeyboardButton(
				text = 'Translate',
				callback_data = '17'
				),
				InlineKeyboardButton(
				text = 'Currency',
				callback_data = '18'
				),
			],
			[
				InlineKeyboardButton(
				text = 'Notes',
				callback_data = '19'
				),
				InlineKeyboardButton(
				text = 'Telegraph',
				callback_data = '20'
				),
				InlineKeyboardButton(
				text = 'Welcome',
				callback_data = '21'
				),
			],
			[
				InlineKeyboardButton(
				text = 'Warn',
				callback_data = '22'
				),
				InlineKeyboardButton(
				text = 'Weather',
				callback_data = '23'
				),
			]
		]
	)
	update.message.reply_text('<b>At the Below you can found My all Commands Help. click any of those buttons😊</b>', reply_markup = key, parse_mode = 'html')
	return FIRST

def qry(update,context):
	query = update.callback_query
	query.answer()
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					text = 'Back',
					callback_data = 'B'
				)
			]
		]
	)
	if query.data == '1':
		query.edit_message_text("*Here is the help for AFK Command:*\n\n`~/afk <reason>`* : Make yourself AFK (Away From Keyboard)*", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '2':
		query.edit_message_text("*Here is the help for Admin Commands:*\n\n`~/admins`* : To view the group admin list*\n\n`~/promote <on a reply>` *: To promote a member to admin*\n\n`~/depromote <on a reply>` *: To remove a user from admin*\n\n`~/pin <message/reply>` *: For pin a message on group*\n\n`~/unpin` *: For unpin last pinned message from group*\n\n`~/title <on a reply>` *: To set a Custom title of a group admin*\n\n`~/rmtitle <on a reply>` *: To remove the custom title of a group admin*\n\n*NOTE : 1)* _You can see_ *<on a reply>* _it means you have to send this command on a reply of a member previous message._", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '3':
		query.edit_message_text("*Here is the help for Disabling Commands:*\n\n`~/mute <on a reply>`* : For mute a member to send messages on the group*\n\n `~/unmute <on a reply>` *: To unmute / allow a member to to send messages again to group*\n\n`~/tmute <on a reply><Day/Hour/Minute>` * : To mute a user for a specific time*\n\n`~/mutelist` *: To see the all muted user list*\n\n*NOTE : 1)* _You can see_*<on a reply>* _it means you have to send this command on a reply of a member previous message._\n\n*2)* _There is another thing_ *<Day/Hour/Minute>* _It means you need to mention the time like_ *EX: <01 / 12 / 22>* _it means 1 day 12 hour 22 minute. You can specify a less time too like_ *EX: <00 / 00 /05>* _it means 0 day 0 hour 5 minute._", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '4':
		query.edit_message_text("*Here is the help for BlackList Commands:*\n\n`~/adblklist <reply/word>`* : For add any word / sticker on the black list. so the bot will delete it if someone send the blacklisted thing on the group*\n\n`~/blklist` *: To see the current blacklisted word / sticker*\n\n`~/rmblklist <word / id>`* : To remove the added word / sticker from blacklist*\n\n*NOTE : 1)* _At the avobe you can see there is_ *<reply/Word>* _it means if you want to add a sticker / .gif on the blacklist then you have to send this command on a reply of this file or if you want to add a word on the black list then you may directly type the word._\n\n*2)* _Another thing you can see avobe_ *<word / id>* _it means if you want to remove a word from blacklist then you can directly type the word. of if you want to remove a sticker / .gif file from blacklist then you have to send the sticker id with the command. for found the sticker it use /blklist Command_", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '5':
		query.edit_message_text("*Here is the help for Bans Commands:*\n\n`~/ban <on a reply>`* : For ban a user from group*\n\n`~/tban <Day/Hour/Minute>` *: To ban a member for a specific time.*\n\n`~/unban <on a reply>`* : To unban a member on the group*\n\n*NOTE : 1)* _You can see_ *<on a reply>* _it means you have to send this command on a reply of a member previous message._\n\n*2)* _There is another thing_ *<Day/Hour/Minute>* _It means you need to mention the time like_ *EX: <01 / 12 / 22>* _it means 1 day 12 hour 22 minute. You can specify a less time too like_ *EX: <00 / 00 /05>* _it means 0 day 0 hour 5 minute._", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '6':
		query.edit_message_text("*Here is the help for Rules Commands:*\n\n`~/setrules <reply / text>`* : For set Rules on the group.*\n\n`~/setrulesbutton <format>` *: For set upto 3 inline buttons with rules command (format mentioned below)*\n\n`~/rules` *: To see the group rules.*\n\n`~/rmrules` *: To remove the current seted rules on the group*\n\n*NOTE : 1)* _At the avobe you can see_ *<reply / text>* _it means you may send this command on a reply previously sended message or you may type the rules with the command_\n\n*2)* _there are another thing_ *<format>* _it means you can send message at this format eith this command_ `/setrulesbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link` _like this_.", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '7':
		query.edit_message_text("*Here is the help for Anime Commands:*\n\n`~/anime <anime name>`* : To find Details about a specific anime series.*\n\n`~/manga <manga name>` *: To find details about a specific manga series*\n\n`~/character <character name>` *: To find detail about a specific anime character*\n\n`~/airing <Name>` *: To find about currently airing anime*", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '8':
		query.edit_message_text("*Here is the help for Music DL Command:*\n\n`~/song <song name>`* : For download any song from YouTube*\n\n*NOTE :* _Make sure the song you want to download it availeable on YouTube_", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '9':
		query.edit_message_text("*Here is the help for Video DL Command:*\n\n`~/video <video name>`* : For download any video from YouTube*\n\n*NOTE :* _Make sure the video you want to download its availeable on YouTube._", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '10':
		query.edit_message_text("*Here is the help for Info Commands:*\n\n`~/setme <text / reply>`* : To set your Bio on the bot*\n\n`~/rmme` *: To remove your seted Bio in the bot*\n\n`~/info <id / None>` *: To see a specific user info*\n\n*NOTE : 1)* _At the avobe you can see there are_ *<text / reply>* _it means you can send the text with the command or You may reply this command on another message_\n\n*2)* _There also you can see_ *<id / None>* _it means you may send a user id with the command or you can send only the command_", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '11':
		query.edit_message_text("*Here is the help for Search Command:*\n\n`~/google <Text>`* : To search somethong on google*\n\n`~/reverse <reply image>` *: For search an image on google image search*\n\n*NOTE : *_at the avobe you can see_ *<reply image>* _it means you have to send this command on reply of a image_.", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '12':
		query.edit_message_text("*Here is the help for Wikipedia Command:*\n\n`~/wiki <topic>`* : To search something on wikipedia*", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '13':
		query.edit_message_text("*Here is the help for Fun Commands:*\n\n`~/slap <reply / text>`* : For slap someone by words*\n\n`~/abuse <on a reply>` *: To abuse someone by simple fun words*\n\n`~/decide <question>` *: Bot will answer your question with randomly Yes and No*\n\n`~/pat <reply / text>` *: For pat someone with word and gifs*\n\n`~/shout <text>` *: To say your word Loudly*\n\n`~/weebify <text>` *: returns a weebified text*\n\n*NOTE : 1)* _At the avobe you can see there are_ *<reply / text>* _it means you can send the text with the command or You may reply this command on another message_\n\n*2)* _You can see_ *<on a reply>* _it means you have to send this command on a reply of a member previous message._", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '14':
		query.edit_message_text("*Here is the help for ChatBot Command:*\n\n`~/addchatbot`* : For turning on the chatbot on your group / private chat*\n\n`~/rmchatbot` *: To stop the chatbot on your group / private chat*\n\n*NOTE : *_If you turned the chatbot on your group then you have to talk with chatbot on reply otherwise bot wont reply you_", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '15':
		query.edit_message_text("*Here is the help for Games Commands:*\n\n`~/toss`* : For Flip a coin. bot will randomly select heads and tales*\n\n`~/roll` *: For roll a dice. bot will randomly select a number from dice*\n\n`~/truth` *: Bot will send you a question and you have to answer it correctly*\n\n`~/dare` *: Bot will ask you to do something and you have to do it*", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '16':
		query.edit_message_text("*Here is the help for Calculator Command:*\n\n`~/solve <equation>`* : For doing normal calculation like 100 × 100 + 10*", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '17':
		query.edit_message_text("*Here is the help for Translate Commands:*\n\n`~/tr <text / reply>`* : For Translating another language to english*\n\n`~/gtr <language><reply / text>` *: For Translating to a specific language*\n\n*NOTE : 1)* _At the above you can see there are_ *<reply / text>* _it means you can send the text with the command or You may reply this command on another message. Make sure the translateable language isnt written in english words_\n\n*2)* _There is another thing_ *<language>* _it means you have to enter the short form of the specific language(you will find the button of language list when you use the command). make sure the translateable language isnt written on the translated language words._", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '18':
		query.edit_message_text("*Here is the help for Currency Converter Command:*\n\n`~/convert <1st currency><2nd Currency><Amount>`* : For chacking a currency current price*\n\n*NOTE : *_At the above there are_ *<1st currency>* _and_ *<2nd currency>* _and_ *<amount>* _there the 1st currency means the compare currency and the 2nd currency is the converted currency and the amount is the how much you want to convert. like_ *EUR USD 10*", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '19':
		query.edit_message_text("*Here is the help for Notes Commands:*\n\n`~/upnote <note title : reply / text>`* : For uploading important notes.*\n\n`~/mynotes` *: To see your current note list.*\n\n`~/dlnote <note title>` *: To download / view your note*\n\n`~/deletenote <note title>` *: For deleteing an un important note*\n\n*NOTE : 1)* _At the above there are_ *<note title : reply / text>* _it means note title is must important. and then you may reply to another message then the bot will save it or you may type the note manually but if you type the note manually then after note title : symbol is must must important._", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '20':
		query.edit_message_text("*Here is the help for Telegraph Commands:*\n\n`~/tgn <reply / text>`* : To upload any text on telegra.ph*\n\n`~/tgp <on a reply>` *: To upload any photo / gif on telegra.ph*\n\n`~/tgv <on a reply>` *: To upload any video on telegra.ph*\n\n*NOTE : 1)* _At the above you can see there are_ *<reply / text>* _it means you can send the text with the command or You may reply this command on another message / photo._\n\n*2)* _You can see_ *<on a reply>* _it means you have to send this command on a reply of another message._", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '21':
		query.edit_message_text("*Here is the help for Welcome Commands:*\n\n`~/addwelcome <reply / text>`* : For set welcome message on the group.*\n\n`~/setwelbutton <format>` *: For set upto 3 inline buttons with welcome message (format mentioned below)*\n\n`~/welcome` *: To see the group welcome message.*\n\n`~/rmwelcome` *: To remove the current seted welcome message on the group*\n\n*NOTE : 1)* _At the above you can see_ *<reply / text>* _it means you may send this command on a reply of previously sended message or you may type the rules with the command_\n\n*2)* _there are another thing_ *<format>* _it means you can send message at this format eith this command_ `/setrulesbutton <code>Button1 Name-Button1 Link#Button2 Name-Button2 Link#Button3 Name-Button 3 Link` _like this_.", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '22':
		query.edit_message_text("*Here is the help for Warn Command:*\n\n`~/warn <reason / None>`* : For sending a warning to a user on your group.*\n\n`~/report <reason>` *: To report someone to admins on the group\n\nNOTE : *_At the above you can see_ *<reason / None>* _it means you can send a reason with the warning or you may only use the commad_.", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	elif query.data == '23':
		query.edit_message_text("*Here is the help for Weather Command:*\n\n`~/weather <place>`* : To see the current weather of a specific location*\n\n*NOTE : *_At the above you can see_ *<place>* _it means you have to mention the location name. (make sure you specify your locatio correct) like_ */weather india delhi* ", parse_mode = ParseMode.MARKDOWN, reply_markup = key)
	return SECOND

def a(update,context):
	query = update.callback_query
	if query.data == 'B':
		query.answer()
		key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
				text = 'AFK',
				callback_data = '1'
				),
				InlineKeyboardButton(
				text = 'Admin',
				callback_data = '2'
				),
				InlineKeyboardButton(
				text = 'Disabling',
				callback_data = '3'
				),
			],
			[
				InlineKeyboardButton(
				text = 'BlackList',
				callback_data = '4'
				),
				InlineKeyboardButton(
				text = 'Bans',
				callback_data = '5'
				),
				InlineKeyboardButton(
				text = 'Rules',
				callback_data = '6'
				),
			],
			[
				InlineKeyboardButton(
				text = 'Anime',
				callback_data = '7'
				),
				InlineKeyboardButton(
				text = 'Music DL',
				callback_data = '8'
				),
				InlineKeyboardButton(
				text = 'Video DL',
				callback_data = '9'
				),
			],
			[
				InlineKeyboardButton(
				text = 'Info',
				callback_data = '10'
				),
				InlineKeyboardButton(
				text = 'Search',
				callback_data = '11'
				),
				InlineKeyboardButton(
				text = 'Wikipedia',
				callback_data = '12'
				),
			],
			[
				InlineKeyboardButton(
				text = 'Fun',
				callback_data = '13'
				),
				InlineKeyboardButton(
				text = 'ChatBot',
				callback_data = '14'
				),
				InlineKeyboardButton(
				text = 'Games',
				callback_data = '15'
				),
			],
			[
				InlineKeyboardButton(
				text = 'Calculator',
				callback_data = '16'
				),
				InlineKeyboardButton(
				text = 'Translate',
				callback_data = '17'
				),
				InlineKeyboardButton(
				text = 'Currency',
				callback_data = '18'
				),
			],
			[
				InlineKeyboardButton(
				text = 'Notes',
				callback_data = '19'
				),
				InlineKeyboardButton(
				text = 'Telegraph',
				callback_data = '20'
				),
				InlineKeyboardButton(
				text = 'Welcome',
				callback_data = '21'
				),
			],
			[
				InlineKeyboardButton(
				text = 'Warn',
				callback_data = '22'
				),
				InlineKeyboardButton(
				text = 'Weather',
				callback_data = '23'
				),
			]
		]
	)
		query.edit_message_text('<b>At the Below you can found My all Commands Help. click any of those buttons😊</b>', reply_markup = key, parse_mode = 'html')
		return FIRST

updates.dispatcher.add_handler(CommandHandler("google", search.gogle, run_async = True))
updates.dispatcher.add_handler(CommandHandler("weather", search.wethe, run_async = True))
updates.dispatcher.add_handler(CommandHandler("song", YouTube.song, run_async = True))
updates.dispatcher.add_handler(CommandHandler("video", YouTube.videos, run_async = True))
updates.dispatcher.add_handler(CommandHandler("wiki", Wikipedia.wik, run_async = True))
updates.dispatcher.add_handler(CommandHandler("warn", warning.warn, run_async = True))
updates.dispatcher.add_handler(CommandHandler("report", warning.report, run_async = True))
updates.dispatcher.add_handler(CommandHandler("tr", translate.tr, run_async = True))
updates.dispatcher.add_handler(CommandHandler("gtr", translate.gtr, run_async = True))
updates.dispatcher.add_handler(CommandHandler("tgn", Telegraph.tgn, run_async = True))
updates.dispatcher.add_handler(CommandHandler("tgp", Telegraph.tgp, run_async = True))
updates.dispatcher.add_handler(CommandHandler("tgv", Telegraph.tgv, run_async = True))
updates.dispatcher.add_handler(CommandHandler("setrules", rules.Main().setrules, run_async = True))
updates.dispatcher.add_handler(CommandHandler("setrulesbutton", rules.setbutton, run_async = True))
updates.dispatcher.add_handler(CommandHandler("rules", rules.rule, run_async = True))
updates.dispatcher.add_handler(CommandHandler("rmrules", rules.rmrul, run_async = True))
updates.dispatcher.add_handler(CommandHandler("reverse", reverse.reverse, run_async = True))
updates.dispatcher.add_handler(CommandHandler("upnote", notes.upnote, run_async = True))
updates.dispatcher.add_handler(CommandHandler("mynotes", notes.note, run_async = True))
updates.dispatcher.add_handler(CommandHandler("deletenote", notes.delnote, run_async = True))
updates.dispatcher.add_handler(CommandHandler("dlnote", notes.dlnote, run_async = True))
updates.dispatcher.add_handler(CommandHandler("mute", mute.mute, run_async = True))
updates.dispatcher.add_handler(CommandHandler("tmute", mute.tmute, run_async = True))
updates.dispatcher.add_handler(CommandHandler("unmute", mute.unmute, run_async = True))
updates.dispatcher.add_handler(CommandHandler("mutelist", mute.mutelst, run_async = True))
updates.dispatcher.add_handler(CommandHandler("setme", Info.setme, run_async = True))
updates.dispatcher.add_handler(CommandHandler("rmme", Info.rmme, run_async = True))
updates.dispatcher.add_handler(CommandHandler("info", Info.info, run_async = True))
updates.dispatcher.add_handler(CommandHandler("toss", games.toss, run_async = True))
updates.dispatcher.add_handler(CommandHandler("roll", games.dice, run_async = True))
updates.dispatcher.add_handler(CommandHandler("truth", games.truth, run_async = True))
updates.dispatcher.add_handler(CommandHandler("dare", games.dare, run_async = True))
updates.dispatcher.add_handler(CommandHandler("weebify", fun.weebify, run_async = True))
updates.dispatcher.add_handler(CommandHandler("decide", fun.decide, run_async = True))
updates.dispatcher.add_handler(CommandHandler("abuse", fun.abuse, run_async = True))
updates.dispatcher.add_handler(CommandHandler("slap", fun.slap, run_async = True))
updates.dispatcher.add_handler(CommandHandler("pat", fun.pat, run_async = True))
updates.dispatcher.add_handler(CommandHandler("shout", fun.shout, run_async = True))
updates.dispatcher.add_handler(CommandHandler("convert", currencyconverter.convert, run_async = True))
updates.dispatcher.add_handler(CommandHandler("adblklist", blacklist.adblklist, run_async = True))
updates.dispatcher.add_handler(CommandHandler("blklist", blacklist.blklist, run_async = True))
updates.dispatcher.add_handler(CommandHandler("rmblklist", blacklist.rmblklist, run_async = True))
updates.dispatcher.add_handler(CommandHandler("solve", calculator.solve, run_async = True))
updates.dispatcher.add_handler(CommandHandler("airing", airing.air, run_async = True))
updates.dispatcher.add_handler(CommandHandler("character", character.chara, run_async = True))
updates.dispatcher.add_handler(CommandHandler("manga", manga.mangaa, run_async = True))
updates.dispatcher.add_handler(CommandHandler("anime", anime.xxx, run_async = True))
updates.dispatcher.add_handler(CommandHandler("admins", admin.admn, run_async = True))
updates.dispatcher.add_handler(CommandHandler("pin", admin.pin, run_async = True))
updates.dispatcher.add_handler(CommandHandler("unpin", admin.unpin, run_async = True))
updates.dispatcher.add_handler(CommandHandler("promote", admin.promote, run_async = True))
updates.dispatcher.add_handler(CommandHandler("depromote", admin.demote, run_async = True))
updates.dispatcher.add_handler(CommandHandler("title", admin.set_title, run_async = True))
updates.dispatcher.add_handler(CommandHandler("rmtitle", admin.rm_title, run_async = True))
updates.dispatcher.add_handler(CommandHandler("ban", bans.ban, run_async = True))
updates.dispatcher.add_handler(CommandHandler("tban", bans.tban, run_async = True))
updates.dispatcher.add_handler(CommandHandler("unban", bans.unban, run_async = True))
updates.dispatcher.add_handler(CommandHandler("addwelcome", welcome.Main().setrules, run_async = True))
updates.dispatcher.add_handler(CommandHandler("setwelbutton", welcome.setbutton, run_async = True))
updates.dispatcher.add_handler(CommandHandler("setwelbutton", welcome.setbutton, run_async = True))
updates.dispatcher.add_handler(CommandHandler("welcome", welcome.rule, run_async = True))
updates.dispatcher.add_handler(CommandHandler("rmwelcome", welcome.rmrul, run_async = True))
updates.dispatcher.add_handler(CommandHandler("addchatbot", chatbot.adchat, run_async = True))
updates.dispatcher.add_handler(CommandHandler("rmchatbot", chatbot.rchat, run_async = True))
updates.dispatcher.add_handler(CommandHandler("gban", console.gban, run_async = True))
updates.dispatcher.add_handler(CommandHandler("sadmin", console.sadmin, run_async = True))
updates.dispatcher.add_handler(CommandHandler("sudouser", console.sudouser, run_async = True))
updates.dispatcher.add_handler(CommandHandler("rmgban", console.rmgban, run_async = True))
updates.dispatcher.add_handler(CommandHandler("rmsadmin", console.rmsadmin, run_async = True))
updates.dispatcher.add_handler(CommandHandler("rmsudo", console.rmsudouser, run_async = True))
updates.dispatcher.add_handler(CommandHandler("upblk", console.s_blklist, run_async = True))
updates.dispatcher.add_handler(CommandHandler("upchbot", console.chbt, run_async = True))
updates.dispatcher.add_handler(CommandHandler("upbio", console.Bio, run_async = True))
updates.dispatcher.add_handler(CommandHandler("upsnote", console.s_note, run_async = True))
updates.dispatcher.add_handler(CommandHandler("uprules", console.uprule, run_async = True))
updates.dispatcher.add_handler(CommandHandler("upwel", console.upwel, run_async = True))
updates.dispatcher.add_handler(CommandHandler("afk", console.afk, run_async = True))
updates.dispatcher.add_handler(CommandHandler("command", console.special, run_async = True))
updates.dispatcher.add_handler(CommandHandler("specialuser", console.admlist, run_async = True))
updates.dispatcher.add_handler(CommandHandler("stats", console.statt, run_async = True))
updates.dispatcher.add_handler(CommandHandler("console", console.console, run_async = True))

updates.dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('start', heelp, Filters.regex('help_private'), run_async = True)],
states = {FIRST:[
	CallbackQueryHandler(qry, pattern = '^1$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^2$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^3$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^4$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^5$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^6$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^7$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^8$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^9$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^10$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^11$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^12$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^13$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^14$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^15$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^16$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^17$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^18$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^19$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^20$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^21$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^22$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^23$', run_async = True)
],
	SECOND:[
		CallbackQueryHandler(a, pattern = '^1$', run_async = True),
	CallbackQueryHandler(a, pattern = '^2$', run_async = True),
	CallbackQueryHandler(a, pattern = '^3$', run_async = True),
	CallbackQueryHandler(a, pattern = '^4$', run_async = True),
	CallbackQueryHandler(a, pattern = '^5$', run_async = True),
	CallbackQueryHandler(a, pattern = '^6$', run_async = True),
	CallbackQueryHandler(a, pattern = '^7$', run_async = True),
	CallbackQueryHandler(a, pattern = '^8$', run_async = True),
	CallbackQueryHandler(a, pattern = '^9$', run_async = True),
	CallbackQueryHandler(a, pattern = '^10$', run_async = True),
	CallbackQueryHandler(a, pattern = '^11$', run_async = True),
	CallbackQueryHandler(a, pattern = '^12$', run_async = True),
	CallbackQueryHandler(a, pattern = '^13$', run_async = True),
	CallbackQueryHandler(a, pattern = '^14$', run_async = True),
	CallbackQueryHandler(a, pattern = '^15$', run_async = True),
	CallbackQueryHandler(a, pattern = '^16$', run_async = True),
	CallbackQueryHandler(a, pattern = '^17$', run_async = True),
	CallbackQueryHandler(a, pattern = '^18$', run_async = True),
	CallbackQueryHandler(a, pattern = '^19$', run_async = True),
	CallbackQueryHandler(a, pattern = '^20$', run_async = True),
	CallbackQueryHandler(a, pattern = '^21$', run_async = True),
	CallbackQueryHandler(a, pattern = '^22$', run_async = True),
	CallbackQueryHandler(a, pattern = '^23$', run_async = True),
	CallbackQueryHandler(a, pattern = '^B$', run_async = True)
	]}, fallbacks = [CommandHandler('help', heelp, Filters.regex('help_private'))], run_async = True,
allow_reentry=True))
updates.dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('start', heelp, Filters.regex('help_keyboard'), run_async = True)],
states = {FIRST:[
	CallbackQueryHandler(qry, pattern = '^1$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^2$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^3$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^4$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^5$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^6$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^7$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^8$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^9$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^10$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^11$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^12$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^13$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^14$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^15$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^16$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^17$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^18$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^19$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^20$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^21$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^22$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^23$', run_async = True)
],
	SECOND:[
		CallbackQueryHandler(a, pattern = '^1$', run_async = True),
	CallbackQueryHandler(a, pattern = '^2$', run_async = True),
	CallbackQueryHandler(a, pattern = '^3$', run_async = True),
	CallbackQueryHandler(a, pattern = '^4$', run_async = True),
	CallbackQueryHandler(a, pattern = '^5$', run_async = True),
	CallbackQueryHandler(a, pattern = '^6$', run_async = True),
	CallbackQueryHandler(a, pattern = '^7$', run_async = True),
	CallbackQueryHandler(a, pattern = '^8$', run_async = True),
	CallbackQueryHandler(a, pattern = '^9$', run_async = True),
	CallbackQueryHandler(a, pattern = '^10$', run_async = True),
	CallbackQueryHandler(a, pattern = '^11$', run_async = True),
	CallbackQueryHandler(a, pattern = '^12$', run_async = True),
	CallbackQueryHandler(a, pattern = '^13$', run_async = True),
	CallbackQueryHandler(a, pattern = '^14$', run_async = True),
	CallbackQueryHandler(a, pattern = '^15$', run_async = True),
	CallbackQueryHandler(a, pattern = '^16$', run_async = True),
	CallbackQueryHandler(a, pattern = '^17$', run_async = True),
	CallbackQueryHandler(a, pattern = '^18$', run_async = True),
	CallbackQueryHandler(a, pattern = '^19$', run_async = True),
	CallbackQueryHandler(a, pattern = '^20$', run_async = True),
	CallbackQueryHandler(a, pattern = '^21$', run_async = True),
	CallbackQueryHandler(a, pattern = '^22$', run_async = True),
	CallbackQueryHandler(a, pattern = '^23$', run_async = True),
	CallbackQueryHandler(a, pattern = '^B$', run_async = True)
	]}, fallbacks = [CommandHandler('help', heelp, Filters.regex('help_keyboard'))], run_async = True,
allow_reentry=True))

updates.dispatcher.add_handler(ConversationHandler(
entry_points=[CommandHandler('help', heelp, run_async = True)],
states = {FIRST:[
	CallbackQueryHandler(qry, pattern = '^1$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^2$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^3$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^4$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^5$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^6$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^7$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^8$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^9$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^10$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^11$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^12$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^13$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^14$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^15$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^16$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^17$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^18$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^19$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^20$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^21$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^22$', run_async = True),
	CallbackQueryHandler(qry, pattern = '^23$', run_async = True)
],
	SECOND:[
		CallbackQueryHandler(a, pattern = '^1$', run_async = True),
	CallbackQueryHandler(a, pattern = '^2$', run_async = True),
	CallbackQueryHandler(a, pattern = '^3$', run_async = True),
	CallbackQueryHandler(a, pattern = '^4$', run_async = True),
	CallbackQueryHandler(a, pattern = '^5$', run_async = True),
	CallbackQueryHandler(a, pattern = '^6$', run_async = True),
	CallbackQueryHandler(a, pattern = '^7$', run_async = True),
	CallbackQueryHandler(a, pattern = '^8$', run_async = True),
	CallbackQueryHandler(a, pattern = '^9$', run_async = True),
	CallbackQueryHandler(a, pattern = '^10$', run_async = True),
	CallbackQueryHandler(a, pattern = '^11$', run_async = True),
	CallbackQueryHandler(a, pattern = '^12$', run_async = True),
	CallbackQueryHandler(a, pattern = '^13$', run_async = True),
	CallbackQueryHandler(a, pattern = '^14$', run_async = True),
	CallbackQueryHandler(a, pattern = '^15$', run_async = True),
	CallbackQueryHandler(a, pattern = '^16$', run_async = True),
	CallbackQueryHandler(a, pattern = '^17$', run_async = True),
	CallbackQueryHandler(a, pattern = '^18$', run_async = True),
	CallbackQueryHandler(a, pattern = '^19$', run_async = True),
	CallbackQueryHandler(a, pattern = '^20$', run_async = True),
	CallbackQueryHandler(a, pattern = '^21$', run_async = True),
	CallbackQueryHandler(a, pattern = '^22$', run_async = True),
	CallbackQueryHandler(a, pattern = '^23$', run_async = True),
	CallbackQueryHandler(a, pattern = '^B$', run_async = True)
	]},
	fallbacks = [CommandHandler('help', heelp, run_async = True)],
))
updates.dispatcher.add_handler(CommandHandler('start', start, run_async = True))
updates.dispatcher.add_handler(CallbackQueryHandler(rules.Main().stbtn, pattern = '^s_btn$', run_async = True))
updates.dispatcher.add_handler(CallbackQueryHandler(rules.Main().stbtn, pattern = '^rm_btn$', run_async = True))
updates.dispatcher.add_handler(CallbackQueryHandler(rules.Main().stbtn, pattern = '^prev$', run_async = True))
updates.dispatcher.add_handler(CallbackQueryHandler(welcome.Main().stbtn, pattern = '^ss_btn$', run_async = True))
updates.dispatcher.add_handler(CallbackQueryHandler(welcome.Main().stbtn, pattern = '^rrm_btn$', run_async = True))
updates.dispatcher.add_handler(CallbackQueryHandler(welcome.Main().stbtn, pattern = '^pprev$', run_async = True))
updates.dispatcher.add_handler(CallbackQueryHandler(notes.que, run_async = True))

updates.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, console.n_member, run_async = True))
updates.dispatcher.add_handler(MessageHandler(Filters.chat_type.groups & Filters.all, console.tuser, run_async = True))
updates.start_polling()

loop = asyncio.get_event_loop()
loop.run_until_complete(chatbot.main())
