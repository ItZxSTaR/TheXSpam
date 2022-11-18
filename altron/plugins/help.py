from pyrogram import filters
from config import SUDO_USERS, client
from pyrogram.types import Message


@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.user(SUDO_USERS))
@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.me)
async def start(client, message: Message):
    await message.reply_text(
    f"»__ ғᴏʀ ʜᴇʟᴘ ᴍᴇɴᴜ ɢᴏ ᴛᴏ ᴛʜɪs ʙᴏᴛ's ᴅᴍ__ » **@AltronRobot** \n\n__sᴏᴏɴ ᴀᴅᴅɪɴɢ ɪɴʟɪɴᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ʙᴜᴛᴛᴏɴs ɪɴ ᴜsᴇʀʙᴏᴛ. ᴊᴏɪɴ__ » **@TheAltron_X @TheAltron**"
    )
