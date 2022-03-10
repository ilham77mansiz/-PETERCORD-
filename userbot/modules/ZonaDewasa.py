# credits to userge
# ported to PETERCORDBOT by ILHAM MANSIEZ
# will be adding more soon
# TENTANG AKU DAN DIA

import asyncio
import os
import urllib

import requests

from userbot import TEMP_DOWNLOAD_DIRECTORY
from . import CmdHelp, Petercord, petercordbot, petercordsudo


@Petercord.on(petercordbot("payudara$"))
@Petercord.on(petercordsudo(pattern="payudara$", allow_sudo=True))
async def boobs(event):
    if event.fwd_from:
        return
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(TEMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("Menemukan beberapa payudara besar untukmu 😂")
    await asyncio.sleep(0.5)
    await a.edit("Ini besar banget nih 😂")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve(
        "http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()

CmdHelp("zonadewasa").add_command(
    'payudara', None, 'Mengirim gambar payudara acak'
).add()
