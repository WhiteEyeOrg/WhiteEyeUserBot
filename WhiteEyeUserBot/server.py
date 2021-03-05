import asyncio
import datetime

from telethon.tl.tlobject import TLObject
from telethon.tl.types import MessageEntityPre
from telethon.utils import add_surrogate

from WhiteEyeUserBot.Configs import Config


def mentionuser(name, userid):
    return f"[{name}](tg://user?id={userid})"


def htmlmentionuser(name, userid):
    return f"<a href='tg://user?id={userid}'>{name}</a>"


# kanged from uniborg @spechide
# https://github.com/SpEcHiDe/UniBorg/blob/d8b852ee9c29315a53fb27055e54df90d0197f0b/uniborg/utils.py#L250


def parse_pre(text):
    text = text.strip()
    return (
        text,
        [MessageEntityPre(offset=0, length=len(add_surrogate(text)), language="")],
    )


def yaml_format(obj, indent=0, max_str_len=256, max_byte_len=64):
    """
    Pretty formats the given object as a YAML string which is returned.
    (based on TLObject.pretty_format)
    """
    result = []
    if isinstance(obj, TLObject):
        obj = obj.to_dict()

    if isinstance(obj, dict):
        if not obj:
            return "dict:"
        items = obj.items()
        has_items = len(items) > 1
        has_multiple_items = len(items) > 2
        result.append(obj.get("_", "dict") + (":" if has_items else ""))
        if has_multiple_items:
            result.append("\n")
            indent += 2
        for k, v in items:
            if k == "_" or v is None:
                continue
            formatted = yaml_format(v, indent)
            if not formatted.strip():
                continue
            result.append(" " * (indent if has_multiple_items else 1))
            result.append(f"{k}:")
            if not formatted[0].isspace():
                result.append(" ")
            result.append(f"{formatted}")
            result.append("\n")
        if has_items:
            result.pop()
        if has_multiple_items:
            indent -= 2
    elif isinstance(obj, str):
        # truncate long strings and display elipsis
        result = repr(obj[:max_str_len])
        if len(obj) > max_str_len:
            result += "…"
        return result
    elif isinstance(obj, bytes):
        # repr() bytes if it's printable, hex like "FF EE BB" otherwise
        if all(0x20 <= c < 0x7F for c in obj):
            return repr(obj)
        else:
            return (
                "<…>" if len(obj) > max_byte_len else " ".join(f"{b:02X}" for b in obj)
            )
    elif isinstance(obj, datetime.datetime):
        # ISO-8601 without timezone offset (telethon dates are always UTC)
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    elif hasattr(obj, "__iter__"):
        # display iterables one after another at the base indentation level
        result.append("\n")
        indent += 2
        for x in obj:
            result.append(f"{' ' * indent}- {yaml_format(x, indent + 2)}")
            result.append("\n")
        result.pop()
        indent -= 2
    else:
        return repr(obj)

    return "".join(result)


async def edit_delete(event, text, time=None, parse_mode=None, link_preview=None):
    parse_mode = parse_mode or "md"
    link_preview = link_preview or False
    time = time or 5
    if event.sender_id in Config.SUDO_USERS:
        reply_to = await event.get_reply_message()
        catevent = (
            await reply_to.reply(text, link_preview=link_preview, parse_mode=parse_mode)
            if reply_to
            else await event.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
        )
    else:
        catevent = await event.edit(
            text, link_preview=link_preview, parse_mode=parse_mode
        )
    await asyncio.sleep(time)
    return await catevent.delete()


async def edit_or_reply(
    event,
    text,
    parse_mode=None,
    link_preview=None,
    file_name=None,
    aslink=False,
    linktext=None,
    caption=None,
):
    link_preview = link_preview or False
    reply_to = await event.get_reply_message()
    if len(text) < 4096:
        parse_mode = parse_mode or "md"
        if event.sender_id in Config.SUDO_USERS:
            if reply_to:
                return await reply_to.reply(
                    text, parse_mode=parse_mode, link_preview=link_preview
                )
            return await event.reply(
                text, parse_mode=parse_mode, link_preview=link_preview
            )
        return await event.edit(text, parse_mode=parse_mode, link_preview=link_preview)
    asciich = ["*", "`", "_"]
    for i in asciich:
        text = re.sub(rf"\{i}", "", text)
    if aslink:
        linktext = linktext or "Message was to big so pasted to bin"
        try:
            key = (
                requests.post(
                    "https://nekobin.com/api/documents", json={"content": text}
                )
                .json()
                .get("result")
                .get("key")
            )
            text = linktext + f" [here](https://nekobin.com/{key})"
        except:
            text = re.sub(r"•", ">>", text)
            kresult = requests.post(
                "https://del.dog/documents", data=text.encode("UTF-8")
            ).json()
            text = linktext + f" [here](https://del.dog/{kresult['key']})"
        if event.sender_id in Config.SUDO_USERS:
            if reply_to:
                return await reply_to.reply(text, link_preview=link_preview)
            return await event.reply(text, link_preview=link_preview)
        return await event.edit(text, link_preview=link_preview)
    file_name = file_name or "output.txt"
    caption = caption or None
    with open(file_name, "w+") as output:
        output.write(text)
    if reply_to:
        await reply_to.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    if event.sender_id in Config.SUDO_USERS:
        await event.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    await event.client.send_file(event.chat_id, file_name, caption=caption)
    await event.delete()
    os.remove(file_name)


# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 13:01:02 2020
@author: OHyic
"""
# import selenium drivers

import imghdr
import logging
import os
import struct
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logger = logging.getLogger("IMAGE_DL")


class GoogleImageScraper:
    def __init__(
        self,
        webdriver_path,
        image_path,
        search_key,
        number_of_images,
        headless=False,
        min_resolution=(0, 0),
        max_resolution=(1920, 1080),
    ):
        # Check parameter types
        if type(number_of_images) != int:
            logger.info(
                "GoogleImageScraper Error : Number of images must be integer value."
            )
            return
        if not os.path.exists(image_path):
            logger.info(
                "GoogleImageScraper Notification : Image path not found. Creating a new folder."
            )
            os.makedirs(image_path)
        self.search_key = search_key
        self.number_of_images = number_of_images
        self.webdriver_path = webdriver_path
        self.image_path = image_path
        self.url = (
            "https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947"
            % (search_key)
        )
        self.headless = headless
        self.min_resolution = min_resolution
        self.max_resolution = max_resolution

    def find_image_urls(self):
        """
        This function search and return a list of image urls based on the search key.
        Example:
            google_image_scraper = GoogleImageScraper("webdriver_path","image_path","search_key",number_of_photos)
            image_urls = google_image_scraper.find_image_urls()

        """
        logger.info(
            "GoogleImageScraper Notification: Scraping for image link... Please wait."
        )
        image_urls = []
        count = 0
        options = Options()
        if self.headless:
            options.add_argument("--headless")
        try:
            driver = webdriver.Chrome(self.webdriver_path, chrome_options=options)
            driver.get(self.url)
            time.sleep(5)
        except:
            logger.info("Driver Failed : Chrome Version is OutDated.")

        for indx in range(1, self.number_of_images + 1):
            try:
                # Find and click image
                imgurl = driver.find_element_by_xpath(
                    '//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img' % (str(indx))
                )
                imgurl.click()

                # Select image from the popup
                time.sleep(3)
                images = driver.find_elements_by_class_name("n3VNCb")
                for image in images:

                    # Only download images that ends with jpg/png/jpeg extensions

                    if image.get_attribute("src")[-3:].lower() in [
                        "jpg",
                        "png",
                        "jpeg",
                    ]:
                        print("%d. %s" % (count, image.get_attribute("src")))
                        image_urls.append(image.get_attribute("src"))
                        count += 1
                        break

                # Scroll page to load next image
                driver.execute_script("window.scrollTo(0, " + str(indx * 150) + ");")
                time.sleep(3)
            except Exception:
                logger.info(
                    "GoogleImageScraper Skip: Unable to get the link for this photo"
                )

        driver.close()
        return image_urls

    def save_images(self, image_urls):
        # Save images into file directory
        """
        This function takes in an array of image urls and save it into the prescribed image path/directory.
        Example:
            google_image_scraper = GoogleImageScraper("webdriver_path","image_path","search_key",number_of_photos)
            image_urls=["https://example_1.jpg","https://example_2.jpg"]
            google_image_scraper.save_images(image_urls)

        """
        logger.info("GoogleImageScraper Notification: Saving Image... Please wait.")
        for indx, image_url in enumerate(image_urls):
            try:

                filename = self.search_key + str(indx) + ".jpg"
                image_path = os.path.join(self.image_path, filename)
                print("%d .Image saved at: %s" % (indx, image_path))
                image = requests.get(image_url)
                if image.status_code == 200:
                    with open(image_path, "wb") as f:
                        f.write(image.content)
                    image_resolution = self.get_image_size(image_path)

                    if image_resolution != None:
                        if (
                            image_resolution[0] < self.min_resolution[0]
                            or image_resolution[1] < self.min_resolution[1]
                            or image_resolution[0] > self.max_resolution[0]
                            or image_resolution[1] > self.max_resolution[1]
                        ):
                            # print("GoogleImageScraper Notification: %s did not meet resolution requirements."%(image_url))
                            os.remove(image_path)

            except Exception:
                logger.info("Unable To Locate Url, Skipping.")
        logger.info("GoogleImageScraper Notification: Download Completed.")

    def get_image_size(self, fname):
        with open(fname, "rb") as fhandle:
            head = fhandle.read(24)
            if len(head) != 24:
                return None
            what = imghdr.what(None, head)
            if what == "png":
                check = struct.unpack(">i", head[4:8])[0]
                if check != 0x0D0A1A0A:
                    return None
                width, height = struct.unpack(">ii", head[16:24])
            elif what == "gif":
                width, height = struct.unpack("<HH", head[6:10])
            elif what == "jpeg":
                try:
                    fhandle.seek(0)  # Read 0xff next
                    size = 2
                    ftype = 0
                    while not 0xC0 <= ftype <= 0xCF or ftype in (0xC4, 0xC8, 0xCC):
                        fhandle.seek(size, 1)
                        byte = fhandle.read(1)
                        while ord(byte) == 0xFF:
                            byte = fhandle.read(1)
                        ftype = ord(byte)
                        size = struct.unpack(">H", fhandle.read(2))[0] - 2
                    # We are at a SOFn block
                    fhandle.seek(1, 1)  # Skip `precision' byte.
                    height, width = struct.unpack(">HH", fhandle.read(4))
                except Exception:  # IGNORE:W0703
                    return None
            else:
                return None
            return width, height
