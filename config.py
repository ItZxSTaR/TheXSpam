import logging
import aiohttp

from TheXSpam import ALTS
from os import getenv
from pyrogram import Client


logging.basicConfig(level=logging.WARNING)


#----------------------------------- REQUIRED CODES --------------------------------------#

API_ID = int(getenv("API_ID", "25981592"))
API_HASH = getenv("API_HASH", "709f3c9d34d83873d3c7e76cdd75b866")
SESSION = getenv("SESSION", "altx131")
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/ab721701ce35ff2856276.jpg")
OWNER_ID = int(getenv("OWNER_ID", "1410250744"))


#-------------------------------- OPTIONAL -------------------------------------#

SESSION2 = getenv("SESSION2")
SESSION3 = getenv("SESSION3")
SESSION4 = getenv("SESSION4")
SESSION5 = getenv("SESSION5")
SESSION6 = getenv("SESSION6")
SESSION7 = getenv("SESSION7")
SESSION8 = getenv("SESSION8")
SESSION9 = getenv("SESSION9")
SESSION10 = getenv("SESSION10")


#------------------------- CLIENTS -----------------------------#

if SESSION:
    client = Client(SESSION, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client = None

if SESSION2:
    client2 = Client(SESSION2, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client2 = None

if SESSION3:
    client3 = Client(SESSION3, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client3 = None

if SESSION4:
    client4 = Client(SESSION4, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client4 = None

if SESSION5:
    client5 = Client(SESSION5, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client5 = None

if SESSION6:
    client6 = Client(SESSION6, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client6 = None
        
if SESSION7:
    client7 = Client(SESSION7, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client7 = None

if SESSION8:
    client8 = Client(SESSION8, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client8 = None

if SESSION9:
    client9 = Client(SESSION9, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client9 = None

if SESSION10:
    client10 = Client(SESSION10, API_ID, API_HASH, plugins=dict(root="TheXSpam"))
else:
    client10 = None


#----------------------------- DON'T MESS ------------------------------#

aioHttpSession = aiohttp.ClientSession()

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

sudo = getenv("SUDO_USERS")
SUDO_USERS = []

SUDO_USERS.append(OWNER_ID)
if sudo:
    SUDO_USERS = make_int(sudo)

for x in ALTS:
    SUDO_USERS.append(x)
