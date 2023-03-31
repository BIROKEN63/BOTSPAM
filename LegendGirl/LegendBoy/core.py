import datetime
import os
import sys
import time

from LegendBS.get_time import get_time
from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl import start_time
from LegendGirl.Config import *

from .. import sudos


@Client.on_message(filters.user(sudos) & filters.command(["ping"], prefixes=HANDLER))
async def ping(_, e: Message):
    start = datetime.datetime.now()
    uptime = get_time((time.time() - start_time))
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    for i in range(1, 26):
        lol = globals()[f"Client{i}"]
        if lol is not None:
            await lol.send_message(
                chat.id, f"⚜️Ping Pong\n\n✨ Ping :`{ms}`\n✨ Uptime: `{uptime}`"
            )
            await asyncio.sleep(0.3)


@Client.on_message(
    filters.user(sudos) & filters.command(["restart", "reboot"], prefixes=HANDLER)
)
async def restarter(Legend: Client, message: Message):
    await message.reply_text("**Bot Is Restarting**\n\n Please Wait 5 min till bot is restart.\nAfter 5 Min Type {HANDLER}ping")
    try:
        await Legend.stop()
    except Exception as error:
        print(str(error))

    args = [sys.executable, "-m", "LegendGirl"]
    os.execl(sys.executable, *args)
    quit()
