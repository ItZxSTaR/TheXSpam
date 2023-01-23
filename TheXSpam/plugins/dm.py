# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑨𝒍𝒕𝒓𝒐𝒏
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅


from pyrogram import filters, Client
from pyrogram.types import Message
import asyncio
from TheXSpam import OneWord, RAID, ALTS
from config import SUDO_USERS
from random import choice


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], [".", "/", "!"]))
async def dmraid(xspam: Client, e: Message):
      alt = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(alt) == 2:
          ok = await xspam.get_users(alt[1])
          id = ok.id

          if int(id) in ALTS:
                await e.reply_text(f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴀʟᴛʀᴏɴ x`")
          elif int(id) in SUDO_USERS:
                await e.reply_text(f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`")
          else:
              counts = int(alt[0])
              print(counts)
              await e.reply_text("`ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.01)

      elif e.reply_to_message and (len(alt) == 1):
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id

          if int(id) in ALTS:
                await e.reply_text(f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴀʟᴛʀᴏɴ x`")
          elif int(id) in SUDO_USERS:
                await e.reply_text(f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`")
          else:
              counts = int(alt[0])
              await e.reply_text("`ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.01)

      else:
            await e.reply_text("⚡ ᴜsᴀɢᴇ:\n   !dmraid 13 <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], [".", "!", "/"]))
async def dmspam(client: Client, message: Message):
    alt = message.text.split(" ", 3)

    if  len(alt) == 4:
        quantity, uid, spam_text = int(alt[1]), alt[2], alt[3]

        if int(uid) in ALTS:
            await message.reply_text(f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴀʟᴛʀᴏɴ x`")
        elif int(uid) in SUDO_USERS:
            await message.reply_text(f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`")
        else:
            await message.reply_text("`ᴅᴍ ꜱᴘᴀᴍ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
            for _ in range(quantity):
                await client.send_message(uid, spam_text)
                await asyncio.sleep(0.3)

    elif message.reply_to_message and (len(alt) == 3):
        id = message.reply_to_message.from_user.id
        quantity = int(alt[1])
        spam_text = alt[2]

        if int(id) in ALTS:
            await message.reply_text(f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴀʟᴛʀᴏɴ x`")
        elif int(id) in SUDO_USERS:
            await message.reply_text(f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`")
        else:
            await message.reply_text("`ᴅᴍ ꜱᴘᴀᴍ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
            for _ in range(quantity):
                await client.send_message(id, spam_text)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text("😈 ᴜsᴀɢᴇ:\n .dmspam 13 <ᴜꜱᴇʀ ɪᴅ> Altron\n .dmspam 13 Altron <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>")
