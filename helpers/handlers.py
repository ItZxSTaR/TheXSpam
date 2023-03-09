from pytgcalls.types.stream import StreamAudioEnded
from config import client, call_py
import asyncio
from helpers.queues import QUEUE, clear_queue, get_queue, pop_an_item
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)



async def skip_current_song(chat_id):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            return 1
        else:
            try:
                songname = chat_queue[1][0]
                url = chat_queue[1][1]
                link = chat_queue[1][2]
                type = chat_queue[1][3]
                Q = chat_queue[1][4]
                if type == "Audio":
                    await call_py.change_stream(
                        chat_id,
                        AudioPiped(
                            url,
                            HighQualityAudio(),
                        ),
                    )
                elif type == "Video":
                    if Q == 720:
                        hm = HighQualityVideo()
                    elif Q == 480:
                        hm = MediumQualityVideo()
                    elif Q == 360:
                        hm = LowQualityVideo()
                    await call_py.change_stream(
                        chat_id,
                        AudioVideoPiped(
                            url,
                            HighQualityAudio(),
                            hm
                        )
                    )
                pop_an_item(chat_id)
                return [songname, link, type]
            except:
                await call_py.leave_group_call(chat_id)
                clear_queue(chat_id)
                return 2
    else:
        return 0


async def skip_item(chat_id, h):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        try:
            x = int(h)
            songname = chat_queue[x][0]
            chat_queue.pop(x)
            return songname
        except Exception as e:
            print(e)
            return 0
    else:
        return 0


@call_py.on_stream_end()
async def stream_end_handler(_, u: Update):
    if isinstance(u, StreamAudioEnded):
        chat_id = u.chat_id
        print(chat_id)
        op = await skip_current_song(chat_id)
        if op == 1:
            pass
        elif op == 2:
            await client.send_message(
                chat_id,
                "**❌ Aɴ Eʀʀᴏʀ Oᴄᴄᴜʀᴇᴅ Lᴇᴀᴠɪɴɢ Vᴏɪᴄᴇ Cʜᴀᴛ**",
            )
        else:
            await client.send_message(
                chat_id,
                f"**🥀 Pʟᴀʏɪɴɢ Nᴇxᴛ Sᴏɴɢ **",
                disable_web_page_preview=True
            )
    else:
        pass
        

async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err
