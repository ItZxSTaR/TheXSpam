import asyncio
from random import choice

from pyrogram.types import Message
from pyrogram import filters, Client

from config import SUDO_USERS
from TheXSpam import GROUP, PORM


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], [".", "!", "/"]))
async def altspam(client: Client, message: Message):
    alt = message.text.split(" ", 2)

    if  len(alt) == 3:
        quantity, spam_text = int(alt[1]), alt[2]

        if message.reply_to_message:
            id = message.reply_to_message_id
            for _ in range(quantity):
                await message.reply_text(spam_text, reply_to_message_id=id)
                await asyncio.sleep(0.3)
        else:
            cid = message.chat.id
            for _ in range(quantity):
                await client.send_message(cid, spam_text)
                await asyncio.sleep(0.3)

    elif message.reply_to_message:
        spam_text = message.reply_to_message.text
        quantity = int(alt[1])
        cid = message.chat.id
        for _ in range(quantity):
            await client.send_message(cid, spam_text)
            await asyncio.sleep(0.3)

    else:
        await message.reply_text(f"😈 **ᴜsᴀɢᴇ:**\n  » !spam 13 Altron\n  » !spam 13 <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>\n\n**To do spam with replying to a user:**\n  » !spam 13 Altron <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")


@Client.on_message(filters.command(["pspam", "pornspam"], [".", "/", "!"]) & filters.user(SUDO_USERS))
async def pspam(client: Client, message: Message):
    cid = message.chat.id
    if int(cid) in GROUP:
        await message.reply_text("» ꜱᴏʀʀʏ, ᴛʜɪꜱ ɪꜱ ᴀʟᴛʀᴏɴ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘ.")
        return

    altp = message.text.split(" ", 2)
    if len(altp) > 1:
        quantity = int(altp[1])
        for _ in range(quantity):
            porm = choice(PORM)
            await client.send_video(cid, porm)
            await asyncio.sleep(0.3)
    else:
        await message.reply_text(f"🔞 **ᴜsᴀɢᴇ:**  !pspam 13")
