# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑨𝒍𝒕𝒓𝒐𝒏
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅

from pyrogram import Client, filters 
from pyrogram.types import Message
from config import SUDO_USERS


@Client.on_message(filters.command(["addall", "inviteall"], ["/", "!", "."]) & filters.user(SUDO_USERS))
async def inviteall(client: Client, message: Message):
    op = await message.reply_text("`Processing...`")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await op.edit_text(f"`Adding Members From` **{chat.username}**")
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        try:
            await client.add_chat_members(tgchat.id, user.id)
        except Exception as e:
            print(e)
