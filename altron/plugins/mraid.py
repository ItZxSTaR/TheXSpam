from pyrogram.types import *
import asyncio
from random import choice
from pyrogram import Client, filters
from helpers.data import *
from config import *


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["mraid"], [".", "/", "!"]))
async def dmraid(xspam: Client, e: Message):
      hero = await e.reply_text("😈 ᴜsᴀɢᴇ:\n !mraid 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ>")   
      TheAltronX = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(TheAltronX) == 2:
          ok = await xspam.get_users(TheAltronX[1])
          id = ok.id
          counts = int(TheAltronX[0])
          omp = await hero.edit_text("`ᴍʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
          await omp.delete()
          for _ in range(counts):
                reply = choice(MRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.001)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = e.chat.id
          counts = int(TheAltronX[0])
          omp = await hero.edit_text("`ᴍʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
          await omp.delete()
          for _ in range(counts):
                reply = choice(MRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.001)

