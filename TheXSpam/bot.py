# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑨𝒍𝒕𝒓𝒐𝒏
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅

import sys
import datetime
import heroku3

from os import execle, environ

from config import ALIVE_PIC, SUDO_USERS, OWNER_ID, HEROKU_APP_NAME, HEROKU_API_KEY

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import __version__ as pyro_vr


VERSION = 3.3

ALT = f"""❖ 𝐏𝐘 𝐀𝐋𝐓𝐑𝐎𝐍 ❖

➠ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.10.4`
➠ **ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ** : `{pyro_vr}`
➠ **ᴀʟᴛʀᴏɴ ᴠᴇʀsɪᴏɴ**  : `{VERSION}`
➠ **ʀᴇᴘᴏ** : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/ItZxSTaR/TheXSpam)\n"""

ALIVE_BUTTON = InlineKeyboardMarkup([[
       InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/TheAltron"),
       InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/AltronChats")
]])


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], ["/", ".", "!"]))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"◇ ᴛʜᴇ ᴀʟᴛʀᴏɴ\n◇ ᴘɪɴɢ: `{ms}ms`\n◇ ᴠᴇʀsɪᴏɴ: `{VERSION}`")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], ["/", ".", "!"]))
async def alive(xspam: Client, msg: Message):
       if ".jpg" in ALIVE_PIC or ".png" in ALIVE_PIC:
              await xspam.send_photo(msg.chat.id, ALIVE_PIC, caption=ALT, reply_markup=ALIVE_BUTTON)
       if ".mp4" in ALIVE_PIC or ".MP4," in ALIVE_PIC:
              await xspam.send_video(msg.chat.id, ALIVE_PIC, caption=ALT, reply_markup=ALIVE_BUTTON)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["reboot", "restart"], ["/", ".", "!"]))
async def restart_bot(_, message: Message):
    msg = await message.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
    args = [sys.executable, "main.py"]
    await msg.edit("» ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ...\n» ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴀғᴛᴇʀ 𝟷 ᴍɪɴᴜᴛᴇ ")
    execle(sys.executable, *args, environ)


@Client.on_message(filters.user(OWNER_ID) & filters.command(["sudo"], ["/", ".", "!"]))
async def add_sudo(_, message: Message):
       if not message.reply_to_message:
              await message.reply_text("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ !!")
              return
       elif HEROKU_APP_NAME is None:
              await message.reply_text("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
              return
       elif HEROKU_API_KEY is None:
              await message.reply_text("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_API_KEY**")
              return
       else:
              heroku = heroku3.from_key(HEROKU_API_KEY)
              app = heroku.app(HEROKU_APP_NAME)

       ok = await message.reply_text(f"» __ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...__")
       heroku_var = app.config()

       sudousers = environ.get("SUDO_USERS")
       target = message.reply_to_message.from_user.id
       if len(sudousers) > 0:
              newsudo = f"{sudousers} {target}"
       else:
              newsudo = f"{target}"
       await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» `ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
       heroku_var["SUDO_USERS"] = newsudo   
