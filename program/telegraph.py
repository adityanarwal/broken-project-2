"""
Video + Music Stream Telegram Bot
Copyright (c) 2022-present levina=lab <https://github.com/levina-lab>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but without any warranty; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/licenses.html>
"""


import os
import re
import uuid
import socket
import psutil
import platform
import shutil

from pyrogram import Client, filters
import upload_file
import TMP_DOWNLOAD_DIRECTORY
import get_file_id
from config import BOT_USERNAME

from program import LOGS
from driver.core import me_bot
from driver.filters import command
from driver.utils import remove_if_exists
from driver.decorators import sudo_users_only, humanbytes

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("telegraph")  & ~filters.edited)
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("Reply to a supported media File❗")
        return
    file_info = get_file_id(replied)
    if not file_info:
        await message.reply_text("File Not supported❗")
        return
    _t = os.path.join(TMP_DOWNLOAD_DIRECTORY, str(replied.message_id))
    if not os.path.isdir(_t):
        os.makedirs(_t)
    _t += "/"
    download_location = await replied.download(_t)
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply_text(message, text=document)
    else:
        await message.reply(
            f"https://telegra.ph{response[0]}", disable_web_page_preview=True
        )
    finally:
        shutil.rmtree(_t, ignore_errors=True)

