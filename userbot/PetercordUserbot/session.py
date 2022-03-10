# PORTED BY ILHAM MANSIZ @diemmmmmmmmmm
# PETERCORD USERBOT
# Thnks Full CatUserbot
import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from userbot import API_KEY, API_HASH, STRING_SESSION, BOT_TOKEN
from .client import bot

__version__ = "2.10.6"

loop = None

if STRING_SESSION:
    session = StringSession(str(STRING_SESSION))
else:
    session = "petercorduserbot"

try:
    Petercord = bot(
        session=session,
        api_id=API_KEY,
        api_hash=API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"STRING_SESSION - {str(e)}")
    sys.exit()


Petercord.tgbot = tgbot = bot(
    session="PetercordTgbot",
    api_id=API_KEY,
    api_hash=API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=BOT_TOKEN)
