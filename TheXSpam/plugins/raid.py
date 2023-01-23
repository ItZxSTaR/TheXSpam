import asyncio

from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from TheXSpam import ALTS, RAID
from config import OWNER_ID, SUDO_USERS


# RAIDING FEATURES

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], ["/", "!", "."]))
async def raid(xspam: Client, e: Message):  
      Hero = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(Hero) == 2:
          counts = int(Hero[0])
          ok = await xspam.get_users(Hero[1])
          id = ok.id
          if int(id) in ALTS:
                await e.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ")
          elif int(id) == OWNER_ID:
                await e.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛꜱ.")
          elif int(id) in SUDO_USERS:
                await e.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ")
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.3)

      elif e.reply_to_message and (len(Hero) == 1):
          counts = int(Hero[0])
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in ALTS:
                await e.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ")
          elif int(id) == OWNER_ID:
                await e.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛꜱ.")
          elif int(id) in SUDO_USERS:
                await e.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ")
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.3)

      else:
          await e.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐚𝐢𝐝\n  » .raid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » .raid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


rusers = []

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["rraid", "replyraid"], ["/", ".", "!"]))
async def rraid(xspam: Client, e: Message):
      global rusers
      Hero = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)

      if len(Hero[0]) > 0:
          ok = await xspam.get_users(Hero[0])
          id = ok.id
          if int(id) in ALTS:
                await e.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ")
          elif int(id) == OWNER_ID:
                await e.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛꜱ.")
          elif int(id) in SUDO_USERS:
                await e.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ")
          else:
              rusers.append(id)
              await e.reply_text("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅")

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          if int(user_id) in ALTS:
                await e.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ")
          elif int(user_id) == OWNER_ID:
                await e.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛꜱ.")
          elif int(user_id) in SUDO_USERS:
                await e.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ")
          else:
              rusers.append(user_id)
              await e.reply_text("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅")

      else:
          await e.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » .rraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » .rraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["drraid", "draid", "dreplyraid"], ["/", ".", "!"]))
async def draid(pam: Client, e: Message):
      global rusers
      Hero = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(Hero[0]) > 0:
          ok = await pam.get_users(Hero[0])
          id = ok.id
          if id in rusers:
              rusers.remove(id)
              await e.reply_text("» ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ !! ✅")

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await pam.get_users(user_id)
          id = ok.id
          if id in rusers:
              rusers.remove(id)
              await e.reply_text("» ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ !! ✅")

      else:
          await e.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » .drraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » .drraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
    

@Client.on_message( ~filters.me & filters.incoming)
async def watcher(_, msg: Message):
    global rusers
    id = msg.from_user.id
    if int(id) in rusers:
       reply = choice(RAID)
       await msg.reply_text(reply)
