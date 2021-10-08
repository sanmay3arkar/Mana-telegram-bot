import os
import re
import requests
import urllib
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from telegram import InputMediaPhoto, TelegramError
from telegram import Bot, ParseMode
from telegram.ext import Updater


bot = Bot("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA")

updates = Updater("1929797199:AAFLk4hTedHqMiL7sddYhFqWJtqtJKTeiBA", use_context = True)

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


def reverse(update,context):
    xx = update.message.reply_text('*Searching🔎...*', parse_mode = ParseMode.MARKDOWN)

    msg = update.effective_message
    chat_id = update.effective_chat.id
    bot, args = context.bot, context.args
    rtmid = msg.message_id
    user = update.effective_user

    reply = msg.reply_to_message
    if reply:
        if reply.sticker:
            file_id = reply.sticker.file_id
        elif reply.photo:
            file_id = reply.photo[-1].file_id
        elif reply.document:
            file_id = reply.document.file_id
        else:
            xx.edit_text("Reply to an image or sticker to lookup.")
            return
        image_file = bot.get_file(file_id)
        image_file.download('Kushida_Bot/modules/helper_function/reverse/{}.png'.format(user.id))
        if args:
            txt = args[0]
            try:
                lim = int(txt)
            except:
                lim = 2
        else:
            lim = 2
    elif args and not reply:
        splatargs = msg.text.split(" ")
        if len(splatargs) == 3:
            img_link = splatargs[1]
            try:
                lim = int(splatargs[2])
            except:
                lim = 2
        elif len(splatargs) == 2:
            img_link = splatargs[1]
            lim = 2
        else:
            xx.edit_text("/reverse <link> <amount of images to return.>")
            return
        try:
            urllib.request.urlretrieve(img_link, "{}.png".format(user.id))
        except HTTPError as HE:
            if HE.reason == "Not Found":
                xx.edit_text("Image not found.")
                return
            elif HE.reason == "Forbidden":
                xx.edit_text(
                    "Couldn't access the provided link, The website might have blocked accessing to the website by bot or the website does not existed."
                )
                return
        except URLError as UE:
            xx.edit_text(f"{UE.reason}")
            return
        except ValueError as VE:
            xx.edit_text(f"{VE}\nPlease try again using http or https protocol.")
            return
    else:
        xx.edit_text(
            "Please reply to a sticker, or an image to search it!\nDo you know that you can search an image with a link too? /reverse [picturelink] <amount>."
        )
        return

    try:
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {
            "encoded_image": ('{}.png'.format(user.id), open('Kushida_Bot/modules/helper_function/reverse/{}.png'.format(user.id), "rb")),
            "image_content": "",
        }
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers["Location"]

        if response != 400:
            xx.edit_text(
                "Image was successfully uploaded to Google."
                "\nParsing it, please wait.",
            )
        else:
            xx.edit_text(
               "Google told me to go away."
            )
            os.remove('Kushida_Bot/modules/helper_function/reverse/{}.png'.format(user.id))
            return

        os.remove('Kushida_Bot/modules/helper_function/reverse/{}.png'.format(user.id))
        match = ParseSauce(fetchUrl + "&hl=en")
        guess = match["best_guess"]
        if match["override"] and not match["override"] == "":
            imgspage = match["override"]
        else:
            imgspage = match["similar_images"]

        if guess and imgspage:
            xx.edit_text(
                f"[{guess}]({fetchUrl})\nProcessing...",
                parse_mode="Markdown",
                disable_web_page_preview=True,
            )
        else:
            xx.edit_text("Couldn't find anything.")
            return

        images = scam(imgspage, lim)
        if len(images) == 0:
            xx.edit_text(
                f"[{guess}]({fetchUrl})\n[Visually similar images]({imgspage})"
                "\nCouldn't fetch any images.",
                parse_mode="Markdown",
                disable_web_page_preview=True,
            )
            return

        imglinks = []
        for link in images:
            lmao = InputMediaPhoto(media=str(link))
            imglinks.append(lmao)

        bot.send_media_group(chat_id=chat_id, media=imglinks, reply_to_message_id=rtmid)
        xx.edit_text(
            f"[{guess}]({fetchUrl})\n[Visually similar images]({imgspage})",
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
    except TelegramError as e:
        print(e)
    except Exception as exception:
        print(exception)


def ParseSauce(googleurl):
    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")

    results = {"similar_images": "", "override": "", "best_guess": ""}

    try:
        for bess in soup.findAll("a", {"class": "PBorbe"}):
            url = "https://www.google.com" + bess.get("href")
            results["override"] = url
    except:
        pass

    for similar_image in soup.findAll("input", {"class": "gLFyf"}):
        url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
            similar_image.get("value")
        )
        results["similar_images"] = url

    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()

    return results


def scam(imgspage, lim):
    single = opener.open(imgspage).read()
    decoded = single.decode("utf-8")
    if int(lim) > 10:
        lim = 10

    imglinks = []
    counter = 0

    pattern = r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
    oboi = re.findall(pattern, decoded, re.I | re.M)

    for imglink in oboi:
        counter += 1
        imglinks.append(imglink)
        if counter >= int(lim):
            break

    return imglinks