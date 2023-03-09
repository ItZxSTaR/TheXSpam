import os
import sys
from os import getenv
import logging
import aiohttp
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.types import *
from pytgcalls import PyTgCalls


logging.basicConfig(level=logging.WARNING)
                    
if os.path.exists("Internal"):
    load_dotenv("Internal")

#---------------------DON'T MESS WITH THESE REQUIRED CODES-------------------------------

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_USERNAME = getenv("BOT_USERNAME", "")
SESSION = getenv("SESSION")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TheAltronX/AltronUserbot")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list
  
sudo = getenv("SUDO_USERS")
SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)

aiohttpsession = aiohttp.ClientSession()

#-----------------------------OPTIONAL--------------------------------

SESSION2 = getenv("SESSION2")
SESSION3 = getenv("SESSION3")
SESSION4 = getenv("SESSION4")
SESSION5 = getenv("SESSION5")
SESSION6 = getenv("SESSION6")
SESSION7 = getenv("SESSION7")
SESSION8 = getenv("SESSION8")
SESSION9 = getenv("SESSION9")
SESSION10 = getenv("SESSION10")

#-------------------------BOT-----------------------------

bot = Client(
    'AltronUserbot',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

#-------------------------CLIENTS-----------------------------

if SESSION:
    client = Client(SESSION, API_ID, API_HASH, plugins=dict(root="altron"))
    call_py = PyTgCalls(client, overload_quiet_mode=False)
else:
    client = None
    call_py = None

if SESSION2:
    client2 = Client(SESSION2, API_ID, API_HASH, plugins=dict(root="altron"))
    call_py2 = PyTgCalls(client2, overload_quiet_mode=False)
else:
    client2 = None
    call_py2 = None

if SESSION3:
    client3 = Client(SESSION3, API_ID, API_HASH, plugins=dict(root="altron"))
    call_py3 = PyTgCalls(client3, overload_quiet_mode=False)
else:
    client3 = None
    call_py3 = None

if SESSION4:
    client4 = Client(SESSION4, API_ID, API_HASH, plugins=dict(root="altron"))
    call_py4 = PyTgCalls(client4, overload_quiet_mode=False)
else:
    client4 = None
    call_py4 = None

if SESSION5:
    client5 = Client(SESSION5, API_ID, API_HASH, plugins=dict(root="altron"))
    call_py5 = PyTgCalls(client5, overload_quiet_mode=False)
else:
    client5 = None
    call_py5 = None

if SESSION6:
    client6 = Client(SESSION6, API_ID, API_HASH, plugins=dict(root="altron"))
    call_py6 = PyTgCalls(client6, overload_quiet_mode=False)
else:
    client6 = None
    call_py6 = None
        
if SESSION7:
    client7 = Client(SESSION7, API_ID, API_HASH, plugins=dict(root="altron"))
    call_py7 = PyTgCalls(client7, overload_quiet_mode=False)
else:
    client7 = None
    call_py7 = None

if SESSION8:
    client8 = Client(SESSION8, API_ID, API_HASH, plugins=dict(root="altron"))
    call_py8 = PyTgCalls(client8, overload_quiet_mode=False)
else:
    client8 = None
    call_py8 = None

if SESSION9:
    client9 = Client(SESSION9, API_ID, API_HASH, plugins=dict(root="altron"))
    call_py9 = PyTgCalls(client9, overload_quiet_mode=False)
else:
    client9 = None
    call_py9 = None

if SESSION10:
    client10 = Client(SESSION10, API_ID, API_HASH, plugins=dict(root="altron"))
    call_py10 = PyTgCalls(client10, overload_quiet_mode=False)
else:
    client10 = None
    call_py10 = None
