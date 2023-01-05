# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑨𝒍𝒕𝒓𝒐𝒏
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅


import os
from TheXSpam import *
from pyrogram import Client, filters
from pyrogram.types import *


@Client.on_message(commandpro(["op", "nice", "cute", "hot", "!save", "x", "kid"]) & filters.me)
async def downloader(client: Client, message: Message):
    targetcontent = message.reply_to_message
    load = await client.download_media(targetcontent)
    await client.send_document("me", load)
    os.remove(load)