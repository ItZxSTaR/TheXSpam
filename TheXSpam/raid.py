import asyncio

from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from data import THE_ALTS, RAID
from config import OWNER_ID, SUDO_USERS


# RAIDING FEATURES

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], ["/", "!", "."]))
async def raid(xspam: Client, message: Message):  
      # Hero = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      alt = message.text.split(" ")

      if len(alt) > 2:
            ok = await xspam.get_users(alt[2])
            id = ok.id
            if id in THE_ALTS:
                  await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ")
            elif id == OWNER_ID:
                  await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛꜱ.")
            elif id in SUDO_USERS:
                  await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ")
            else:
                  counts = int(alt[1])
                  fname = ok.first_name
                  mention = f"[{fname}](tg://user?id={id})"
                  for _ in range(counts):
                        reply = choice(RAID)
                        msg = f"{mention} {reply}"
                        await xspam.send_message(message.chat.id, msg)
                        await asyncio.sleep(0.3)

      elif message.reply_to_message and (len(alt) == 2):
            user_id = message.reply_to_message.from_user.id
            ok = await xspam.get_users(user_id)
            id = ok.id
            if id in THE_ALTS:
                  await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ")
            elif id == OWNER_ID:
                  await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛꜱ.")
            elif id in SUDO_USERS:
                  await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ")
            else:
                  counts = int(alt[1])
                  fname = ok.first_name
                  mention = f"[{fname}](tg://user?id={id})"
                  for _ in range(counts):
                        reply = choice(RAID)
                        msg = f"{mention} {reply}"
                        await xspam.send_message(message.chat.id, msg)
                        await asyncio.sleep(0.3)

      else:
          await message.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐚𝐢𝐝\n  » .raid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » .raid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


rusers = []

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["rraid", "replyraid"], ["/", ".", "!"]))
async def rraid(xspam: Client, message: Message):
      global rusers
      alt = message.text.split(" ")

      if len(alt) > 1:
          ok = await xspam.get_users(alt[1])
          id = ok.id
          if id in THE_ALTS:
                await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ")
          elif id == OWNER_ID:
                await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛꜱ.")
          elif id in SUDO_USERS:
                await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ")
          else:
              rusers.append(id)
              await message.reply_text("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅")

      elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          if user_id in THE_ALTS:
                await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ")
          elif user_id == OWNER_ID:
                await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛꜱ.")
          elif user_id in SUDO_USERS:
                await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ")
          else:
              rusers.append(user_id)
              await message.reply_text("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅")

      else:
          await message.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » .rraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » .rraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["drraid", "draid", "dreplyraid"], ["/", ".", "!"]))
async def draid(xspam: Client, message: Message):
      global rusers
      alt = message.text.split(" ")

      if len(alt) > 1:
          ok = await xspam.get_users(alt[1])
          id = ok.id
          if id in rusers:
              rusers.remove(id)
              await message.reply_text("» ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ !! ✅")

      elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if id in rusers:
              rusers.remove(id)
              await message.reply_text("» ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ !! ✅")

      else:
          await message.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » .drraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » .drraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
    

@Client.on_message(~filters.me & filters.incoming)
async def watcher(_, msg: Message):
      global rusers
      id = msg.from_user.id
      if id in rusers:
            reply = choice(RAID)
            await msg.reply_text(reply)
