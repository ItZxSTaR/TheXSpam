# © @PyXen
from config import SUDO_USERS, ALIVE_PIC
from data import bot_msg, spam_msg, raid_msg, dm_msg

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton


FIRST_TEXT = f"★ 𝙏𝙝𝙚𝙓𝙎𝙥𝙖𝙢 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @PyXen**"

HELP_BUTTON = InlineKeyboardMarkup([
    [InlineKeyboardButton("• ʙᴏᴛ •", callback_data="bot")],
    [
      InlineKeyboardButton("• ꜱᴘᴀᴍ •", callback_data="spam"),
      InlineKeyboardButton("• ʀᴀɪᴅ •", callback_data="raid")
    ],
    [InlineKeyboardButton("• ᴅᴍ •", callback_data="dm")]
  ])

BACK_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("< Back", callback_data="back")]])


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help"], [".", "!", "/"]))
async def help(client: Client, message: Message):
    await client.send_photo(
        chat_id=message.chat.id,
        photo=ALIVE_PIC,
        caption=FIRST_TEXT,
        reply_markup=HELP_BUTTON
    )


@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    query = callback_query.data
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id

    if query == "back":
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=FIRST_TEXT, reply_markup=HELP_BUTTON)

    elif query == "bot":
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=bot_msg, reply_markup=BACK_BUTTON)

    elif query == "spam":
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=spam_msg, reply_markup=BACK_BUTTON)

    elif query == "raid":
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=raid_msg, reply_markup=BACK_BUTTON)

    elif query == "dm":
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dm_msg, reply_markup=BACK_BUTTON)
