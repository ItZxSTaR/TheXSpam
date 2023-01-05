import logging
import aiohttp
import os
from TheXSpam import OWNERS
from TheXSpam import *
from os import getenv
from pyrogram import Client
from pyrogram.types import *


logging.basicConfig(level=logging.WARNING)


#----------------------------------- REQUIRED CODES --------------------------------------#


API_ID = 22273859

API_HASH = "125c7cf7edc8c0474a0be891eaf69d6c"

SESSION = "AQDCibWLF349oL1Zz7SMwRO1fcHrIlyn7TlF6gAmATlO35_QHu615DmaWNXqasW5KdcYLXtJu_uJ1cQXuFCawO_H4MRxSbbpavR5mpr_U5D40k59RDapL4nRllGr7GsutboGMbx3gg2-SpISwsy_RUkF2wLUWRnH55-O9xBBAeAwgvunfvlKsdb-WLrIo2XF4ec7YdZ62X1C6O4_lbkUDbTCthdDrq5jt3GKYkJUsHvB8OMSm9pTWs_Xv0ctkJDNaqWcgIa1u5kcOiTee2QYrVuV9mDWEIC3HYz3vl8qt8f2-EHSPur0BIEYrIR-h9cmiNwHIOq0ca-YVdJcpbObWd31AAAAAWPASsIA"

ALIVE_PIC = "https://te.legra.ph/file/ab721701ce35ff2856276.jpg"

OWNER_ID = 5968513730


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


aiohttpsession = aiohttp.ClientSession()

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

sudo = os.getenv("SUDO_USERS")
SUDO_USERS = []

if sudo:
    SUDO_USERS = make_int(sudo)

for x in OWNERS:
    SUDO_USERS.append(x)
    SUDO_USERS.append(OWNER_ID)
