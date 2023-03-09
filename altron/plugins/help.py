from pyrogram import filters, Client
from config import bot, SUDO_USERS
from config import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message


@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.user(SUDO_USERS))
@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.me)
async def start(client, message: Message):
    await message.reply_text(
    f"»__ ғᴏʀ ʜᴇʟᴘ ᴍᴇɴᴜ ɢᴏ ᴛᴏ ʏᴏᴜʀ ᴄʀᴇᴀᴛᴇᴅ ʙᴏᴛ's ᴅᴍ__ » **@{BOT_USERNAME}** \n\n__sᴏᴏɴ ᴀᴅᴅɪɴɢ ɪɴʟɪɴᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ʙᴜᴛᴛᴏɴs ɪɴ ᴜsᴇʀʙᴏᴛ ᴊᴏɪɴ__ » **@TheAltron_X**"
    )
    

@bot.on_message(filters.command(["start"], ["/", "!", "$"]))
async def start(client: Client, message: Message):
    HOME_TEXT = """
🤖 **ʜᴇʏᴀ..!!! 
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ __ɪ'ᴍ ᴀɴ ᴜsᴇʀʙᴏᴛ. ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴛʜʀᴏᴡ ᴜsᴇʀʙᴏᴛ. ɪ ᴄᴀɴ sᴘᴀᴍ ᴍsɢ ᴀɴʏ ᴍᴀɴʏ ᴍᴏʀᴇ . ɪ ʜᴀᴠᴇ ʟᴏᴛꜱ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ʏᴏᴜ ʟɪᴋᴇꜱ ᴛʜᴀᴛ__.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ __ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ℹ️__.
"""
    buttons = [
            [
                InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/TheAltron"),
                InlineKeyboardButton("✘ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/Altron_X"),
            ],
            [
                InlineKeyboardButton("✘ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/TheAltronX/AltronUserbot"),
                InlineKeyboardButton("✘ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Shailendra34"),
            ],
            [
                InlineKeyboardButton("✘ ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", callback_data="help_"),
            ]
            ]     
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"https://te.legra.ph/file/7abe179ff252aaabbf2a5.jpg", caption=HOME_TEXT, reply_markup=reply_markup)
    await message.delete()
    
@bot.on_message(filters.command(["help"], ["/", "$"]))
def help_(Client, message: Message):
    HELP_TXT = """🤖 ʜᴏɪ..!!! 
__ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴄʜᴏᴏsᴇ ʏᴏᴜʀ ᴅᴇsɪʀᴇ ᴏᴘᴛɪᴏɴ ɴᴅ ᴇxᴘʟᴏʀᴇ ɪᴛ. \nғᴏʀ ᴀɴʏ ᴋɪɴᴅ ᴏғ ʜᴇʟᴘ ᴏʀ ǫᴜᴇʀʏ ᴊᴜsᴛ ᴊᴏɪɴ @Altron_X ᴀɴᴅ ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇʀʏ. __"""
    
    message.reply_photo(
        photo="https://te.legra.ph/file/7abe179ff252aaabbf2a5.jpg",
        caption=HELP_TXT,
        reply_markup=InlineKeyboardMarkup(
            [
        [
            InlineKeyboardButton(text="︎ᴠᴄ", callback_data="vc"),
            InlineKeyboardButton(text="sᴘᴀᴍ", callback_data="spam"),
            InlineKeyboardButton(text="ʙᴏᴛ", callback_data="bot_cmd"),
        ],
        [
            InlineKeyboardButton(text="ʀᴀɪᴅ", callback_data="raid"), 
            InlineKeyboardButton(text="ᴀᴅᴠᴀɴᴄᴇ", callback_data="advance"), 
        ],   
        [
            InlineKeyboardButton(text="ᴄʟᴏsᴇ 🗑", callback_data="close"),
        ],
    ], 
        ), 
    )
    message.delete()

@bot.on_callback_query()
def callback_query(Client, callback: CallbackQuery):
    if callback.data == "help_":
    
        HELP_TXT = """🤖 ʜᴏɪ..!!! 
__ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴄʜᴏᴏsᴇ ʏᴏᴜʀ ᴅᴇsɪʀᴇ ᴏᴘᴛɪᴏɴ ɴᴅ ᴇxᴘʟᴏʀᴇ ɪᴛ. \nғᴏʀ ᴀɴʏ ᴋɪɴᴅ ᴏғ ʜᴇʟᴘ ᴏʀ ǫᴜᴇʀʏ ᴊᴜsᴛ ᴊᴏɪɴ @Altron_X ᴀɴᴅ ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇʀʏ. __"""
    
        HELP_BUTTON = [
        [
            InlineKeyboardButton(text="ᴠᴄ", callback_data="vc"),
            InlineKeyboardButton(text="sᴘᴀᴍ", callback_data="spam"),
            InlineKeyboardButton(text="ʙᴏᴛ", callback_data="bot_cmd"),
        ],
        [
            InlineKeyboardButton(text="ʀᴀɪᴅ", callback_data="raid"),
            InlineKeyboardButton(text="ᴀᴅᴠᴀɴᴄᴇ", callback_data="advance"), 
        ],   
        [
            InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close"),
            InlineKeyboardButton(text="⬅ ʙᴀᴄᴋ", callback_data="start_"),
        ],
    ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "start_":
        HOME_TEXT = """
🤖 **ʜᴇʏᴀ..!!! 
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ __ɪ'ᴍ ᴀɴ ᴜsᴇʀʙᴏᴛ. ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴛʜʀᴏᴡ ᴜsᴇʀʙᴏᴛ. ɪ ᴄᴀɴ sᴘᴀᴍ ᴍsɢ ᴀɴᴅ ᴍᴀɴʏ ᴍᴏʀᴇ. ɪ ʜᴀᴠᴇ ʟᴏᴛꜱ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ʏᴏᴜ ʟɪᴋᴇꜱ ᴛʜᴀᴛ__.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ __ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ℹ️__.
"""
        BUTTON = [
            [
                InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/TheAltron"),
                InlineKeyboardButton("✘ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/Altron_X"),
            ],
            [
                InlineKeyboardButton("✘ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/TheAltronX/AltronUserbot"),
                InlineKeyboardButton("✘ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Shailendra34"),
            ],
            [
                InlineKeyboardButton("✘ ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", callback_data="help_"),
            ]
        ]     
        reply_markup = InlineKeyboardMarkup(BUTTON)
        callback.edit_message_text(
        HOME_TEXT,
        reply_markup=reply_markup
        )
    elif callback.data == "vc":
        B_HELP = """
» ᴜsᴇʀʙᴏᴛ ᴘʟᴀʏ ᴍᴇɴᴜ:-
        
/p - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ
/e - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴇɴᴅ ᴍᴜsɪᴄ
/s - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴋɪᴘ ᴍᴜsɪᴄ
/pause - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴘᴀᴜsᴇ ᴍᴜsɪᴄ
/resume - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʀᴇsᴜᴍᴇ ᴍᴜsɪᴄ
/playlist - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴄʜᴇᴄᴋ ᴘʟᴀʏʟɪsᴛ
/playfrom [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ] - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴘʟᴀʏ sᴏɴɢs ғʀᴏᴍ ᴀɴᴏᴛʜᴇʀ ɢʀᴏᴜᴘ
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close"),
                InlineKeyboardButton(text="⬅ ʙᴀᴄᴋ", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "spam":
        SPM_HELP = """
» ᴜsᴇʀʙᴏᴛ sᴘᴀᴍ ᴍᴇɴᴜ:-        

!fspam - ғᴏʀ ғᴀsᴛ sᴘᴀᴍ
!spam - ғᴏʀ sᴘᴀᴍ
!delspam - ᴀғᴛᴇʀ sᴘᴀᴍ ᴍsɢ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ
!dspam - ғᴏʀ sʟᴏᴡ sᴘᴀᴍ
!sspam - ғᴏʀ sᴛɪᴄᴋᴇʀ sᴘᴀᴍ

"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close"),
                InlineKeyboardButton(text="⬅ ʙᴀᴄᴋ", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            SPM_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "bot_cmd":
        A_HELP = """
ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ ɪs ᴜsᴇᴅ ғᴏʀ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs        
🤖 ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs ᴍᴇɴᴜ:-
        
/start - ᴛᴏ sᴛᴀʀᴛ ʙᴏᴛ
/help - ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴍsɢ ᴏғ ʙᴏᴛ 
/vcraid - ᴛᴏ ᴠᴄʀᴀɪᴅ ɪɴ ᴀ ᴘᴜʙʟɪᴄ ɢʀᴏᴜᴘ
/araid - ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴀᴜᴅɪᴏ ᴀɴᴅ sᴇɴᴅ ᴄᴍᴅ ʟɪᴋᴇ ᴠᴄʀᴀɪᴅ
/raidend - ᴛᴏ ᴇɴᴅ ʀᴀɪᴅ
/raidpause - ᴛᴏ ᴘᴀᴜsᴇ ʀᴀɪᴅ
/raidresume - ᴛᴏ ʀᴇsᴜᴍᴇ ʀᴀɪᴅ

__sᴏᴏɴ ᴍᴏʀᴇ ᴘʟᴜɢɪɴs__
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close"),
                InlineKeyboardButton(text="⬅ ʙᴀᴄᴋ", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "raid":
        C_HELP = """
» ᴜsᴇʀʙᴏᴛ ʀᴀɪᴅ ᴍᴇɴᴜ:-
        
!raid - ᴛᴏ ʀᴀɪᴅ ᴏɴ ᴀɴ ᴜsᴇʀ
!dmraid - ᴛᴏ ʀᴀɪᴅ ᴏɴ ᴀɴ ᴜsᴇʀ ɪɴ ᴅᴍ 
!sraid - sᴏɴɢ ʟʏʀɪᴄs ʀᴀɪᴅ ᴏɴ ᴀ ᴜsᴇʀ 
!mraid - ғʟɪʀᴛɪɴɢ ʀᴀɪᴅ ᴏɴ ᴀ ᴜsᴇʀ

"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close"),
                InlineKeyboardButton(text="⬅ ʙᴀᴄᴋ", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            C_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )        
    elif callback.data == "advance":
        D_HELP = """
!cl - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴊᴜɴᴋ ғɪʟᴇs
!restart - ᴛᴏ ʀᴇsᴛᴀʀᴛ ᴜsᴇʀʙᴏᴛ
!update - ᴛᴏ ᴜᴘᴅᴀᴛᴇ ᴜsᴇʀʙᴏᴛ
!help - ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴍsɢ
!ping - ᴛᴏ ᴄʜᴇᴄᴋ ᴘɪɴɢ ᴏғ ᴜsᴇʀʙᴏᴛ
!hang - ᴛᴏ sᴇɴᴅ ʜᴀɴɢ ᴍsɢ ɪɴ ᴀ group
!inviteall - ᴛᴏ ᴀᴅᴅ ᴍᴇᴍʙᴇʀs
!join - ᴛᴏ ᴊᴏɪɴ ᴀ ᴘᴜʙʟɪᴄ ᴏʀ ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ
!leave - ᴛᴏ ʟᴇᴀᴠᴇ ᴀ ᴘᴜʙʟɪᴄ ᴏʀ ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ

"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close"),
                InlineKeyboardButton(text="⬅ ʙᴀᴄᴋ", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            D_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )        
    elif callback.data == "close":
        callback.message.delete()
