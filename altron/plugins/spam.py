import asyncio
from random import choice

from pyrogram.types import Message
from pyrogram import filters, Client
from config import SUDO_USERS
from helpers.data import GROUP, PORMS


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["delspam", "deletespam"], [".", "!", "/"]))
async def delspam(client: Client, message: Message):
    quantity = int(message.command[1])
    spam_text = ' '.join(message.command[2:])

    if (len(spam_text) > 0) or (quantity > 0):
        await message.delete()
        for _ in range(quantity):
            msg = await client.send_message(message.chat.id, spam_text)
            await asyncio.sleep(1)
            await msg.delete()
            await asyncio.sleep(1)
    else:
        await message.reply_text("😈 Usage:\n !delspam 10 Altron")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["spam", "spamming"], [".", "!", "/"]))
async def suspam(client: Client, message: Message):
    quantity = int(message.command[1])
    spam_text = ' '.join(message.command[2:])

    if message.reply_to_message and len(spam_text) == 0:
        spam_text = message.reply_to_message
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text)
            await asyncio.sleep(0.1)
    elif message.reply_to_message and len(spam_text) > 0:
        id = message.reply_to_message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text, reply_to_message_id=id)
            await asyncio.sleep(0.1)
    elif len(spam_text) > 0:
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text)
            await asyncio.sleep(0.1)
    else:
        await message.reply_text("😈 Usage:\n !spam 10 Altron")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["fastspam", "fspam"], [".", "!", "/"]))
async def spspam(client: Client, message: Message):
    quantity = int(message.command[1])
    spam_text = ' '.join(message.command[2:])
    
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text, reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.001)
        return

    elif len(spam_text) > 0:
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text)
            await asyncio.sleep(0.001)
    else:
        await message.reply_text("😈 Usage:\n !fspam 10 Umm")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["slowspam", "dspam", "delayspam"], [".", "!", "/"]))
async def sperm(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text, reply_to_message_id=reply_to_id)
            await asyncio.sleep(2)
        return
    elif len(spam_text) > 0:
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text)
            await asyncio.sleep(2)
    else:
        await message.reply_text("⚡ Usage:\n !slowspam 10 Umm")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], [".", "!", "/"]))
async def pussy(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("**reply to a sticker with amount you want to spam**")
        return
    if not message.reply_to_message.sticker:
        await message.edit_text(text="**reply to a sticker with amount you want to spam**")
        return
    else:
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.2)

        if message.chat.type == "private":
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id, sticker
                )
                await asyncio.sleep(0.2)


@Client.on_message(filters.command(["pspam", "pornspam"], [".", "/", "!"]) & filters.user(SUDO_USERS))
async def pspam(client: Client, message: Message):
    if int(message.chat.id) in GROUP:
        await message.reply_text("» ꜱᴏʀʀʏ, ᴛʜɪꜱ ɪꜱ ᴀʟᴛʀᴏɴ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘ.")
        return

    quantity = message.command[1]
    for _ in range(quantity):
        PORM = choice(PORMS)
        await client.send_video(message.chat.id, PORM)
        await asyncio.sleep(0.2)
    else:
        await message.reply_text("🔞 Usage:\n !pspam 10")



@Client.on_message(filters.command('join', [".", "!", "/"]) & filters.user(SUDO_USERS))
async def fuck(client: Client, message: Message):
    hero = message.text[6:]
    if not hero:
        return await message.reply_text("Need a chat username or invite link to join.")
    if hero.isnumeric():
        return await message.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        await client.join_chat(hero)
        await message.reply_text(f"**Joined ✅**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command('leave', [".", "!", "/"]) & filters.user(SUDO_USERS))
async def leftfuck(client: Client, message: Message):
    hero = message.text[6:]
    if not hero:
        return await message.reply_text("Need a chat username or invite link to leave.")
    if hero.isnumeric():
        return await message.reply_text("Can't leave a chat with chat id. Give username or invite link.")
    try:
        await client.leave_chat(hero)
        await message.reply_text(f"**Left ❌**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")
