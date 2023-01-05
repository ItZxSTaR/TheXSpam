from pyrogram.types import Message
import asyncio
from random import choice
from pyrogram import Client, filters
from TheXSpam import *
from config import *


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], [".", "/", "!"]))
@client.on_message(filters.me & filters.command(["raid"], [".", "/", "!"]))
async def dmraid(xspam: Client, e: Message):
      TheAltronX = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(TheAltronX) == 2:
          ok = await xspam.get_users(TheAltronX[1])
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴀʟᴛʀᴏɴ x`"
                await e.reply_text(text)
          else:
              counts = int(TheAltronX[0])
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.2)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴀʟᴛʀᴏɴ x`"
                await e.reply_text(text)
          else:
              counts = int(TheAltronX[0])
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"[{ok.first_name}](tg://user?id={id}) {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.2)

      else:
            await e.reply_text("⚡ ᴜsᴀɢᴇ:\n !raid 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["sraid"], [".", "/", "!"]))
@client.on_message(filters.me & filters.command(["sraid"], [".", "/", "!"]))
async def dmraid(xspam: Client, e: Message):
      TheAltronX = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(TheAltronX) == 2:
          ok = await xspam.get_users(TheAltronX[1])
          counts = int(TheAltronX[0])
          for _ in range(counts):
                reply = choice(SRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.2)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          counts = int(TheAltronX[0])
          for _ in range(counts):
                reply = choice(SRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.2)
      
      else:
            await e.reply_text("» ᴜsᴀɢᴇ:\n !sraid 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["mraid"], [".", "/", "!"]))
@client.on_message(filters.me & filters.command(["mraid"], [".", "/", "!"]))
async def dmraid(xspam: Client, e: Message):
      TheAltronX = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(TheAltronX) == 2:
          ok = await xspam.get_users(TheAltronX[1])
          counts = int(TheAltronX[0])
          for _ in range(counts):
                reply = choice(MRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          counts = int(TheAltronX[0])
          for _ in range(counts):
                reply = choice(MRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("😈 ᴜsᴀɢᴇ:\n !mraid 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ>")
