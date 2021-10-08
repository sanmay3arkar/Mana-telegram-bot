import os
import re
from asyncio import gather, get_event_loop, sleep
from aiohttp import ClientSession
from Python_ARQ import ARQ
from pyrogram import Client, filters, idle
from telegram import Bot, ParseMode
from telegram.ext import Updater

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

API_ID = int(os.environ.get("API_ID", "4272186"))
API_HASH = os.environ.get("API_HASH", "fcacc350c16bd139b6c4313f0ca64e7d")
BOT_TOKEN = os.environ.get("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", None)
ARQ_API_KEY = "XQYJAL-HTSZIK-YALWDS-TJPWMO-ARQ" 
LANGUAGE = "en"
ARQ_API_BASE_URL = "https://thearq.tech"

m_chat = []

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)

bot_token= BOT_TOKEN
bot_id = int(1759027838)
arq = None

async def lunaQuery(query: str, user_id: int):
    query = (
        query
        if LANGUAGE == "en"
        else (await arq.translate(query, "en")).result.translatedText
    )
    resp = (await arq.luna(query, user_id)).result
    return (
        resp
        if LANGUAGE == "en"
        else (
            await arq.translate(resp, LANGUAGE)
        ).result.translatedText
    )


async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(lunaQuery(query, user_id), sleep(2))
    if "Luna" in response:
        responsee = response.replace("Luna", "Mana")
    else:
        responsee = response
    if "Aco" in responsee:
        responsess = responsee.replace("Aco", "Mana")
    else:
        responsess = responsee
    if "Who is Tiana?" in responsess:
        responsess2 = responsess.replace("Who is Mana?", "Heroine Of Telegram")
    else:
        responsess2 = responsess
    await message.reply_text(responsess2)
    await message._client.send_chat_action(chat_id, "cancel")


@bot.on_message(
    ~filters.private
    & filters.text
    & ~filters.edited,
    group=69,
)
async def chat(_, message):
    chatid1 = message.chat.id
    if chatid1 not in m_chat:
    	return 
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,}iris[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match:
            return
    await type_and_send(message)


@bot.on_message(
    filters.private
    & ~filters.edited
)
async def chatpm(_, message):
    chatid2 = message.chat.id
    if chatid2 not in m_chat:
    	return 
    if not message.text:
        await message.reply_text("Uff... Ignoring .... ¯\_(ツ)_/¯")
        return
    await type_and_send(message)

async def main():
    global arq
    session = ClientSession()
    arq = ARQ(ARQ_API_BASE_URL, ARQ_API_KEY, session)

    await bot.start()
    await idle()

def adchat(update,context):
	chat_id = update.effective_chat
	user = update.effective_user
	
	if chat_id.type != 'private':
		promoter = chat.get_member(user.id)

		if (
			not (promoter.status == 'administrator' or promoter.status == "creator")
    ):
			update.message.reply_text("<b>I am really sorry but you don't have the necessary rights to do that. please become an admin first!</b>", parse_mode = 'html')
			return
			
	if chat_id.id in m_chat:
		update.message.reply_text('*Chatbot Already enabled to this chat. please reply on my previous sended message.*', parse_mode = ParseMode.MARKDOWN)
		return 
	try:
		m_chat.append(chat_id.id)
		update.message.reply_text("*Chatbot Successfully Enabled to this chat✅*", parse_mode = ParseMode.MARKDOWN)
	except:
		update.message.reply_text('<b>I am really sorry but server is currently busy please try again later.</b>', parse_mode = 'html')
		
def rchat(update, context):
	chat_id1 = update.effective_chat
	user = update.effective_user
	
	if chat_id1.type != 'private':
		promoter = chat.get_member(user.id)

		if (
			not (promoter.status == 'administrator' or promoter.status == "creator")
    ):
			update.message.reply_text("<b>I am really sorry but you don't have the necessary rights to do that. please become an admin first!</b>", parse_mode = 'html')
			return
			
	if chat_id1.id not in m_chat:
		update.message.reply_text("<b>Chatbot is already disabled on this chat. Please enable first.</b>", parse_mode = 'html')
		return 
	try:
		m_chat.remove(chat_id1.id)
		update.message.reply_text('<b>Chatbot Successfully Disabled✅</b>', parse_mode = 'html')
	except:
		update.message.reply_text('<b>I am really sorry but server is currently busy please try again later.</b>', parse_mode = 'html')
		return 