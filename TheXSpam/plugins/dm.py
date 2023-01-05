from pyrogram import filters, Client
from pyrogram.types import Message
import asyncio
from random import choice
from TheXSpam import *
from config import *


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], [".", "/", "!"]))
@Client.on_message(filters.me & filters.command(["dmraid"], [".", "/", "!"]))
async def dmraid(xspam: Client, e: Message):
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
              await e.reply_text("`ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.01)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴀʟᴛʀᴏɴ x`"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`"
                await e.reply_text(text)
          else:
              counts = int(TheAltronX[0])
              await e.reply_text("`ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.01)

      else:
            await e.reply_text("⚡ ᴜsᴀɢᴇ:\n !dmraid 13 <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], [".", "!", "/"]))
@Client.on_message(filters.me & filters.command(["dmspam"], [".", "!", "/"]))
async def suspam(client: Client, message: Message):
      PyX = message.text.split(" ", 3)
      quantity = int(PyX[1])
      UserId = int(PyX[2])
      spam_text = PyX[3]

      if UserId and spam_text is not None:
            for _ in range(quantity):
                  await client.send_message(UserId, spam_text)
                  await asyncio.sleep(0.01)
      else:
            await message.reply_text("😈 Usage:\n !dmspam 10 <UserId> Altron")
