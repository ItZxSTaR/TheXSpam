# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑨𝒍𝒕𝒓𝒐𝒏
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅


from config import SUDO_USERS
from pyrogram import Client, filters
from pyrogram.types import Message
from TheXSpam import GROUP


# JOIN COMMAND

@Client.on_message(filters.command(["join"], ["/", "!", "."]) & filters.user(SUDO_USERS))
async def join(client: Client, message: Message):
    op = message.text[6:]
    if not op:
        return await message.reply_text("`Need a chat username or invite link to join.`")
    elif op.isnumeric():
        return await message.reply_text("`Can't join a chat with chat id. Give username or invite link.`")
    try:
        await client.join_chat(op)
        await message.reply_text(f"**Joined**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")
  
         
# LEAVE COMMAND

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["leave", "remove"], [".", "!", "/"]))
async def leave(pam: Client, e: Message):
    hero = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    if len(e.text) > 7:
        try:
           await pam.leave_chat(hero[0])
           await e.reply_text(f"**Left Successfully ✅**")
        except Exception as ex:
           await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
    else:
        chat = e.chat.id
        ok = e.from_user.id
        if int(chat) == int(ok):
            return await e.reply_text(f"⚡ ᴜsᴀɢᴇ:\n !leave <chat username or id> or !leave [type in Group for Direct leave]")
        elif int(chat) in GROUP:
              return await e.reply_text(f"**Error**")
        try:
           await pam.leave_chat(chat)
           await e.reply_text(f"**Left Successfully ✅ **")
        except Exception as ex:
           await e.reply_text(f"**ERROR:** \n\n{str(ex)}")


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
