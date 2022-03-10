# PORTED BY ILHAM MANSIZ @diemmmmmmmmmm
# PETERCORD USERBOT
# Thnks Full CatUserbot

import asyncio
import os

from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery

from userbot import SUDO_USERS

OWNER_ID = int(os.environ.get("OWNER_ID") or 0)


def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        if c_q.query.user_id and (
            c_q.query.user_id == OWNER_ID
            or c_q.query.user_id in SUDO_USERS
        ):
            try:
                await func(c_q)
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds + 5)
            except MessageNotModifiedError:
                pass
        else:
            await c_q.answer(
                "Only My Master can Access This !!\n\nDeploy your own PetercordUserbot.",
                alert=True,
            )

    return wrapper
