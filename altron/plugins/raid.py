from pyrogram.types import *
import asyncio
from random import choice
from pyrogram import Client, filters
from helpers.data import *
from config import *


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], [".", "/", "!"]))
async def dmraid(xspam: Client, e: Message):
      hero = await e.reply_text("⚡ ᴜsᴀɢᴇ:\n !raid 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ>")   
      TheAltronX = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(TheAltronX) == 2:
          ok = await xspam.get_users(TheAltronX[1])
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴀʟᴛʀᴏɴ x`"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`"
                await e.reply_text(text)
          else:
              counts = int(TheAltronX[0])
              omp = await hero.edit_text("`ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              await omp.delete()
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.001)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = e.chat.id
          if int(id) in VERIFIED_USERS:
                text = f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴀʟᴛʀᴏɴ x`"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`"
                await e.reply_text(text)
          else:
              counts = int(TheAltronX[0])
              omp = await hero.edit_text("`ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              await omp.delete()
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.001)

