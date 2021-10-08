from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater
from googlesearch import search
from bs4 import BeautifulSoup
import urllib
import requests
import datetime
from geopy.geocoders import Nominatim
from PIL import Image, ImageDraw, ImageFont
import random
from Kushida_Bot.modules.helper_function import list_dict
import os

bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)


def gogle(update,context):
	try:
		args = update.message.text.split(None,1)
		if len(args) <2:
			try:
				text = update.message.reply_to_message.text
			except:
				update.message.reply_text("<b>For using this command you have to send it on a reply. otherwise send it like this👇</b>\n\n🔹/google (<code>Your Word</code>)🔹\n\n<b>Don't neec to use brakets. please try again😊</b>", parse_mode = 'html')
				return 
		else:
			text = args[1]
	
		count = 0
		value = ''
		msg = update.message.reply_text('<b>Searching🔎...</b>',parse_mode = 'html')
		try:
			for query in search(text):
				try:
					if count == 5:
						break
					site = urllib.request.urlopen(query)
					soup = BeautifulSoup(site, "html.parser")
					try:
						des = soup.find('meta', attrs={'name' : 'description'})
					except:
						des = ''
					if des != '':
						des = str(des)
						des = des.replace('<meta content="', '')
						des = des.replace('" name="description"/>', '')
					if len(des) > 100:
						des = des[0:100]
					count = count + 1
					title = soup.title.text
					if len(title) > 60:
						title = title[0:60]
						value = value + "<b><a href ='{}'>🔹{}...</a></b>".format(query, title) + '\n' + "<i>{}</i>".format(des) + '\n\n'
					else:
						value = value + "<b><a href ='{}'>🔹{}</a></b>".format(query, title) + '\n' + "<i>{}</i>".format(des) + '\n\n'
					if count == 3:
						msg.edit_text('<b>Just a little more🔎...</b>', parse_mode = 'html')
				except:
					continue
		except:
			msg.edit_text("<b>Can't able to find it! please re check your searching query.</b>", parse_mode = 'html')
			return 
		key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					text = 'View More',
					url = 'https://www.google.com/search?q={}'.format(text)
				)
			]
		]
	)
		try:
			if '<meta' in value:
				value = value.replace('<meta', '')
			msg.edit_text('<b>Your Searched result🔻</b>\n\n{}'.format(value), disable_web_page_preview = True, reply_markup = key, parse_mode = 'html')
		except:
			msg.edit_text('<b>i am really sorry i cant able to search it please check your query.</b>', parse_mode = 'html')
	except:
		update.message.reply_text("i am really sorry please try again later")


def wethe(update,context):
	try:
		args = update.message.text.split(None, 1)
		user = update.effective_user
		if len(args) < 2:
			update.message.reply_text("<b>For using this command you have to send it like this👇</b>\n\n🔹/weather (<code>Your Location</code>)🔹\n\n<b>Don't use brakets its just for showing. please try again😊</b>", parse_mode = 'html')
			return 
	
		find = update.message.reply_text("<b>getting Details🔎...</b>",parse_mode = 'html')
	
		date_time = datetime.datetime.now()
		time = date_time.strftime('%H:%M:%S')
		date = date_time.strftime('%Y-%m-%d')
		forecast = 'daily'
	
		try:
			geolocator = Nominatim(user_agent="forecast")
			location=geolocator.geocode(args[1])
			latitude = round(location.latitude, 2)
			longitude=round(location.longitude,2)
		except:
			find.edit_text("<b>Can't able to find!! it make sure you entered correct Location Name.</b>", parse_mode = 'html')
			return 
	
		try:
			api_endpoint = f"https://api.weather.com/v2/turbo/vt1dailyForecast?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&geocode={latitude}%2C{longitude}&language=en-IN&units=m"
			response = requests.get(api_endpoint)
			response_data = response.json()
		except:
			find.edit_text("<b>I am really sorry! The API is currently down. Please Try after sometime.</b>", parse_mode = 'html')
			return 
	
		try:
			dates_time_list = response_data["vt1dailyForecast"]["validDate"]
			dates_list = [_.split("T0")[0] for _ in dates_time_list]
			date_index = dates_list.index(date)
		except:
			find.edit_text("<b>I am really Sorry! Something error heppen Please try after sometime.</b>", parse_mode = 'html')
			return 
	
		try:
			temperature_day = response_data["vt1dailyForecast"][
            "day"]["temperature"][date_index]
		
			precipitate_day = response_data["vt1dailyForecast"][
            "day"]["precipPct"][date_index]
		
			uv_description_day = response_data["vt1dailyForecast"][
            "day"]["uvDescription"][date_index]
		
			wind_speed_day = response_data["vt1dailyForecast"][
            "day"]["windSpeed"][date_index]
		
			humidity_day = response_data["vt1dailyForecast"][
            "day"]["humidityPct"][date_index]
		
			phrases_day = response_data["vt1dailyForecast"][
            "day"]["phrase"][date_index] 
		
			narrative_day = response_data["vt1dailyForecast"][
            "day"]["narrative"][date_index]
		
		
		
			temperature_night = response_data["vt1dailyForecast"][
            "night"]["temperature"][date_index]
		
			precipitate_night = response_data["vt1dailyForecast"][
            "night"]["precipPct"][date_index]
		
			uv_description_night = response_data["vt1dailyForecast"][
            "night"]["uvDescription"][date_index]
		
			wind_speed_night = response_data["vt1dailyForecast"][
            "night"]["windSpeed"][date_index]
		
			humidity_night = response_data["vt1dailyForecast"][
            "night"]["humidityPct"][date_index]
		
			phrases_night = response_data["vt1dailyForecast"][
            "night"]["phrase"][date_index] 
		
			narrative_night = response_data["vt1dailyForecast"][
            "night"]["narrative"][date_index]    
                       

			forecast_output = {}
			forecast_output["place"] = args[1]
			forecast_output["time"] = time
			forecast_output["date"] = date
			forecast_output["day"] = {"temperature": temperature_day,
                                  "precipitate": precipitate_day,
                                  "uv_description": uv_description_day,
                                  "wind_speed": wind_speed_day,
                                  "humidity": humidity_day,
                                  "phrases": phrases_day,
                                  "narrative":narrative_day

                                  }

			forecast_output["night"] = {	"temperature": temperature_night,
                                     "precipitate": precipitate_night,
                                     "uv_description": uv_description_night,
                                     "wind_speed": wind_speed_night,
                                     "humidity": humidity_night,
                                     "phrases": phrases_night,
                                     "narrative":narrative_night
                                     }
                                     
		except:
			find.edit_text("<b>Something Error heppen. Please Try after sometime.</b>", parse_mode = 'html')
			return 
	
		if forecast_output['day']['temperature'] != None:
			if forecast_output['day']['phrases'] == None:
				file = list_dict.DAYCLEAN + list_dict.DAYCLOUDY + list_dict.DAYHFCLOUD + list_dict.DAYRAIN + list_dict.DAYSNOW + list_dict.FOG + list_dict.NIGHTCLEAN + list_dict.NIGHTCLOUD + list_dict.NIGHTHFCLOUD + list_dict.NIGHTRAIN + list_dict.NIGHTSNOW + list_dict.STORM
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(file)))
			elif 'Rain' in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYRAIN)))
			elif 'Rain'.lower() in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYRAIN)))
			elif 'Rain'.upper() in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYRAIN)))
			elif 'T-Storms' in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.STORM)))
			elif 'T-Storms'.lower() in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.STORM)))
			elif 'T-Storms'.upper() in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.STORM)))
			elif 'Mostly Cloudy' in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYCLOUDY)))
			elif 'Cloudy' in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYCLOUDY)))
			elif 'Thunder' in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.STORM)))
			elif 'Storm' in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.STORM)))
			elif 'Showers' in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYRAIN)))
			elif 'Clean' in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYCLEAN)))
			elif 'Clear' in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYCLEAN)))
			elif 'Sunny' in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYCLEAN)))
			else:
				file = list_dict.DAYCLEAN + list_dict.DAYCLOUDY + list_dict.DAYHFCLOUD + list_dict.DAYRAIN + list_dict.DAYSNOW + list_dict.FOG + list_dict.NIGHTCLEAN + list_dict.NIGHTCLOUD + list_dict.NIGHTHFCLOUD + list_dict.NIGHTRAIN + list_dict.NIGHTSNOW + list_dict.STORM
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(file)))
		
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype("Kushida_Bot/modules/helper_function/weather/MomcakeBold-WyonA.otf", 75)
			font1 = ImageFont.truetype("Kushida_Bot/modules/helper_function/weather/MomcakeBold-WyonA.otf", 140)
			font2 = ImageFont.truetype("Kushida_Bot/modules/helper_function/weather/Acme-Regular.ttf", 140)
			font3 = ImageFont.truetype('Kushida_Bot/modules/helper_function/weather/MomcakeBold-WyonA.otf', 60)
			font4 = ImageFont.truetype('Kushida_Bot/modules/helper_function/weather/MomcakeBold-WyonA.otf', 35)
		
			draw.text((100, 70),"CURRENTLY",(255,255,255),font=font)
			draw.text((120, 160), "{}".format(forecast_output['day'] ['temperature']), (255,255,255), font= font1)
			draw.text((263, 135), "°", (255,255,255), font= font2)
			draw.text((305, 160), "C", (255,255,255), font= font1)
			draw.text((650, 70), "WEATHER DETAILS", (255,255,255), font= font)
			draw.text((700, 150), "{}".format(forecast_output['day']['phrases']), (255,255,255), font= font3)
			draw.text((730, 205), "{}% Humidity".format(forecast_output['day']['humidity']), (255,255,255), font= font3)
			draw.text((70, 680), "location: {}".format(args[1]), (255,255,255), font= font4)
			draw.text((1000, 680), "Mana Nagase", (255,255,255), font= font4)
		
			image.save('Kushida_Bot/modules/helper_function/weather/edited/{}.jpg'.format(user.id))
			sfile = open('Kushida_Bot/modules/helper_function/weather/edited/{}.jpg'.format(user.id), "rb")
			if forecast_output['night']['temperature'] != None:
				dayf = forecast_output['day']['temperature']
				dayf = str(dayf)
				if '.' in dayf:
					dayf = float(dayf)
				else:
					dayf = int(dayf)
			
				dayf = dayf * 1.8
				dayf = dayf + 32
				dayf = str(dayf)
				if len(dayf) > 5:
					dayf = dayf[0:5]
		
				ngtf = forecast_output['night']['temperature']
				ngtf = str(ngtf)
				if '.' in ngtf:
					ngtf = float(ngtf)
				else:
					ngtf = int(ngtf)
			
				ngtf = ngtf * 1.8
				ngtf = ngtf + 32
				ngtf = str(ngtf)
				if len(ngtf) > 5:
					ngtf = ngtf[0:5]
		
		
				update.message.reply_photo(sfile, caption = "<b>FORECAST OF 🔹{}🔹\n\n🌍 : PLACE: </b><code>{}</code>\n\n<b>DAY FORECAST🔻\n📄DESCRIPTION:</b> <i>{}</i>\n\n<b>🌡 : TEMPERATURE:</b> <code>{}°C ({}°F)</code>\n<b>☀️ : UV INDEX:</b> <code>{}</code>\n<b>💨 : WIND SPEED:</b> <code>{}km/h</code>\n<b>💧 : HUMIDITY: </b><code>{}%</code>\n\n\n<b>NIGHT FORECAST🔻\n📄 : DESCRIPTION: </b><i>{}</i>\n\n<b>🌡 : TEMPERATURE: </b><code>{}°C ({}°F)</code>\n<b>☀️ : UV INDEX: </b><code>{}</code>\n<b>💨 : WIND SPEED: </b> <code>{}km/h</code>\n<b>💧 : HUMIDITY: </b><code>{}%</code>".format(forecast_output['date'], args[1], forecast_output['day']['narrative'], forecast_output['day']['temperature'], dayf, forecast_output['day']['uv_description'], forecast_output['day']['wind_speed'], forecast_output['day']['humidity'], forecast_output['night']['narrative'], forecast_output['night']['temperature'],ngtf, forecast_output['night']['uv_description'], forecast_output['night']['wind_speed'], forecast_output['night']['humidity']), parse_mode = 'html')
				find.delete()
			else:
				dayf = forecast_output['day']['temperature']
				dayf = str(dayf)
				if '.' in dayf:
					dayf = float(dayf)
				else:
					dayf = int(dayf)
			
				dayf = dayf * 1.8
				dayf = dayf + 32
				dayf = str(dayf)
				if len(dayf) > 5:
					dayf = dayf[0:5]
			
				update.message.reply_photo(sfile, caption = "<b>FORECAST OF 🔹{}🔹\n\n🌍 : PLACE: </b><code>{}</code>\n\n<b>DAY FORECAST🔻\n📄DESCRIPTION:</b> <i>{}</i>\n\n<b>🌡 : TEMPERATURE:</b> <code>{}°C ({}°F)</code>\n<b>☀️ : UV INDEX:</b> <code>{}</code>\n<b>💨 : WIND SPEED:</b> <code>{}km/h</code>\n<b>💧 : HUMIDITY: </b><code>{}%</code>".format(forecast_output['date'], args[1], forecast_output['day']['narrative'], forecast_output['day']['temperature'], dayf, forecast_output['day']['uv_description'], forecast_output['day']['wind_speed'], forecast_output['day']['humidity']), parse_mode = 'html')
			
		elif forecast_output['night']['temperature'] != None:
			if forecast_output['day']['phrases'] == None:
				file = list_dict.DAYCLEAN + list_dict.DAYCLOUDY + list_dict.DAYHFCLOUD + list_dict.DAYRAIN + list_dict.DAYSNOW + list_dict.FOG + list_dict.NIGHTCLEAN + list_dict.NIGHTCLOUD + list_dict.NIGHTHFCLOUD + list_dict.NIGHTRAIN + list_dict.NIGHTSNOW + list_dict.STORM
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(file)))
			elif 'Rain' in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYRAIN)))
			elif 'Rain'.lower() in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYRAIN)))
			elif 'Rain'.upper() in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYRAIN)))
			elif 'T-Storms' in forecast_output['night']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.STORM)))
			elif 'T-Storms'.lower() in forecast_output['night']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.STORM)))
			elif 'T-Storms'.upper() in forecast_output['night']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.STORM)))
			elif 'Cloudy' in forecast_output['night']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.NIGHTHFCLOUD)))
			elif 'Thunder' in forecast_output['night']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.STORM)))
			elif 'Storm' in forecast_output['night']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.STORM)))
			elif forecast_output['day']['phrases'] == None:
				file = list_dict.DAYCLEAN + list_dict.DAYCLOUDY + list_dict.DAYHFCLOUD + list_dict.DAYRAIN + list_dict.DAYSNOW + list_dict.FOG + list_dict.NIGHTCLEAN + list_dict.NIGHTCLOUD + list_dict.NIGHTHFCLOUD + list_dict.NIGHTRAIN + list_dict.NIGHTSNOW + list_dict.STORM
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(file)))
			elif 'Rain' in forecast_output['night']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.NIGHTRAIN)))
			elif 'Rain'.lower() in forecast_output['night']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYRAIN)))
			elif 'Rain'.upper() in forecast_output['night']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.DAYRAIN)))
			elif 'Showers' in forecast_output['night']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.NIGHTRAIN)))
			elif 'Clean' in forecast_output['day']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.NIGHTCLEAN)))
			elif 'Clear' in forecast_output['night']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.NIGHTCLEAN)))
			elif 'moon' in forecast_output['night']['phrases']:
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(list_dict.NIGHTCLEAN)))
			else:
				file = list_dict.DAYCLEAN + list_dict.DAYCLOUDY + list_dict.DAYHFCLOUD + list_dict.DAYRAIN + list_dict.DAYSNOW + list_dict.FOG + list_dict.NIGHTCLEAN + list_dict.NIGHTCLOUD + list_dict.NIGHTHFCLOUD + list_dict.NIGHTRAIN + list_dict.NIGHTSNOW + list_dict.STORM
				image = Image.open('Kushida_Bot/modules/helper_function/weather/{}'.format(random.choice(file)))
		
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype("Kushida_Bot/modules/helper_function/weather/MomcakeBold-WyonA.otf", 75)
			font1 = ImageFont.truetype("Kushida_Bot/modules/helper_function/weather/MomcakeBold-WyonA.otf", 140)
			font2 = ImageFont.truetype("Kushida_Bot/modules/helper_function/weather/Acme-Regular.ttf", 140)
			font3 = ImageFont.truetype('Kushida_Bot/modules/helper_function/weather/MomcakeBold-WyonA.otf', 60)
			font4 = ImageFont.truetype('Kushida_Bot/modules/helper_function/weather/MomcakeBold-WyonA.otf', 35)
		
			draw.text((100, 70),"CURRENTLY",(255,255,255),font=font)
			draw.text((120, 160), "{}".format(forecast_output['night'] ['temperature']), (255,255,255), font= font1)
			draw.text((263, 135), "°", (255,255,255), font= font2)
			draw.text((305, 160), "C", (255,255,255), font= font1)
			draw.text((650, 70), "WEATHER DETAILS", (255,255,255), font= font)
			draw.text((700, 150), "{}".format(forecast_output['night']['phrases']), (255,255,255), font= font3)
			draw.text((730, 205), "{}% Humidity".format(forecast_output['night']['humidity']), (255,255,255), font= font3)
			draw.text((70, 680), "location: {}".format(args[1]), (255,255,255), font= font4)
			draw.text((1000, 680), "Mana Nagase", (255,255,255), font= font4)
		
			image.save('Kushida_Bot/modules/helper_function/weather/edited/{}.jpg'.format(user.id))
			sfile = open('Kushida_Bot/modules/helper_function/weather/edited/{}.jpg'.format(user.id), "rb")
			if forecast_output['day']['temperature'] != None:
				dayf = forecast_output['day']['temperature']
				dayf = str(dayf)
				if '.' in dayf:
					dayf = float(dayf)
				else:
					dayf = int(dayf)
			
				dayf = dayf * 1.8
				dayf = dayf + 32
				dayf = str(dayf)
				if len(dayf) > 5:
					dayf = dayf[0:5]
		
				ngtf = forecast_output['night']['temperature']
				ngtf = str(ngtf)
				if '.' in ngtf:
					ngtf = float(ngtf)
				else:
					ngtf = int(ngtf)
			
				ngtf = ngtf * 1.8
				ngtf = ngtf + 32
				ngtf = str(ngtf)
				if len(ngtf) > 5:
					ngtf = ngtf[0:5]
		
		
				update.message.reply_photo(sfile,caption = "<b>FORECAST OF 🔹{}🔹\n\n🌍 : PLACE: </b><code>{}</code>\n\n<b>DAY FORECAST🔻\n📄DESCRIPTION:</b> <i>{}</i>\n\n<b>🌡 : TEMPERATURE:</b> <code>{}°C ({}°F)</code>\n<b>☀️ : UV INDEX:</b> <code>{}</code>\n<b>💨 : WIND SPEED:</b> <code>{}km/h</code>\n<b>💧 : HUMIDITY: </b><code>{}%</code>\n\n\n<b>NIGHT FORECAST🔻\n📄 : DESCRIPTION: </b><i>{}</i>\n\n<b>🌡 : TEMPERATURE: </b><code>{}°C ({}°F)</code>\n<b>☀️ : UV INDEX: </b><code>{}</code>\n<b>💨 : WIND SPEED: </b> <code>{}km/h</code>\n<b>💧 : HUMIDITY: </b><code>{}%</code>".format(forecast_output['date'], args[1], forecast_output['day']['narrative'], forecast_output['day']['temperature'], dayf, forecast_output['day']['uv_description'], forecast_output['day']['wind_speed'], forecast_output['day']['humidity'], forecast_output['night']['narrative'], forecast_output['night']['temperature'],ngtf, forecast_output['night']['uv_description'], forecast_output['night']['wind_speed'], forecast_output['night']['humidity']), parse_mode = 'html')
				find.delete()
			else:
				ngtf = forecast_output['night']['temperature']
				ngtf = str(ngtf)
				if '.' in ngtf:
					ngtf = float(ngtf)
				else:
					ngtf = int(ngtf)
			
				ngtf = ngtf * 1.8
				ngtf = ngtf + 32
				ngtf = str(ngtf)
				if len(ngtf) > 5:
					ngtf = ngtf[0:5]
			
				update.message.reply_photo(sfile,caption = "<b>FORECAST OF 🔹{}🔹\n\n🌍 : PLACE: </b><code>{}</code>\n\n<b>NIGHT FORECAST🔻\n📄 : DESCRIPTION: </b><i>{}</i>\n\n<b>🌡 : TEMPERATURE: </b><code>{}°C ({}°F)</code>\n<b>☀️ : UV INDEX: </b><code>{}</code>\n<b>💨 : WIND SPEED: </b> <code>{}km/h</code>\n<b>💧 : HUMIDITY: </b><code>{}%</code>".format(forecast_output['date'], args[1], forecast_output['night']['narrative'], forecast_output['night']['temperature'],ngtf, forecast_output['night']['uv_description'], forecast_output['night']['wind_speed'], forecast_output['night']['humidity']), parse_mode = 'html')
				find.delete()
				os.remove('Kushida_Bot/modules/helper_function/weather/edited/{}.jpg'.format(user.id))
		else:
			find.edit_text("<b>I am really sorry. data hasen't updated yet! Please try after sometime😊</b>", parse_mode = 'html')
	except:
		update.message.reply_text("<b>I am really sorry. i cant able to find it please try again later</b>", parse_mode = 'html')