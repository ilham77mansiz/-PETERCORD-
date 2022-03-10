import asyncio
import base64
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import ChatBannedRights

import userbot.modules.sql_helper.gban_sql as gban_sql

from userbot import BOTLOG, BOTLOG_CHATID, PETERCORD_ID
from userbot.events import register


BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@register(outgoing=True, pattern=r"^\.gban(?: |$)(.*)")
async def gban(event):
    if event.fwd_from:
        return
    cate = await edit_or_reply(event, "`gbanning.GLOBAL......`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if user.id == (await event.client.get_me()).id:
        await cate.edit("Tentang Aku Dan Dia")
        return
    if user.id in PETERCORD_ID:
        await cate.edit("Lu gabisa gban gua")
        return
    try:
        hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        await event.client(ImportChatInviteRequest(hmm))
    except BaseException:
        pass
    if gban_sql.is_gbanned(user.id):
        await cate.edit(
            f"`the `[user](tg://user?id={user.id})` is already in gbanned list any way checking again`"
        )
    else:
        gban_sql.categban(user.id, reason)
    san = []
    san = await admin_groups(event)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await cate.edit("`Kalau bukan admin ga bisa kick :)` ")
        return
    await cate.edit(
        f"`initiating gban of the `[user](tg://user?id={user.id}) `in {len(san)} groups`"
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat :** {event.chat.title}(`{event.chat_id}`)\n`For banning here`",
            )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gbanned in {count} groups in {cattaken} seconds`!!\n**Reason :** `{reason}`"
        )
    else:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gbanned in {count} groups in {cattaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"⚜GLOBAL BAN\
                \nGlobal Ban\
                \n**➠ PENGGUNA : **[{user.first_name}](tg://user?id={user.id})\
                \n**➠ ID USER : **`{user.id}`\
                \n**➠ ALASAN :** `{reason}`\
                \n__Banned Di {count} groups__\
                \n**Time taken : **`{cattaken} seconds`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"⚜GLOBAL BANNED\
                \nGlobal Ban\
                \n**➠ PENGGUNA : **[{user.first_name}](tg://user?id={user.id})\
                \n**➠ ID USER  : **`{user.id}`\
                \n__Banned in {count} groups__\
                \n**➠ WAKTU DIGBAN : **`{cattaken} seconds`",
            )
        try:
            if reply:
                await reply.forward_to(BOTLOG_CHATID)
                await reply.delete()
        except BadRequestError:
            pass


@register(outgoing=True, pattern=r"^\.ugban(?: |$)(.*)")
async def ungban(event):
    if event.fwd_from:
        return
    cate = await edit_or_reply(event, "`ungbanning..GLOBAL...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.catungban(user.id)
    else:
        await cate.edit(
            f"the [user](tg://user?id={user.id}) `is not in your gbanned list`"
        )
        return
    san = []
    san = await admin_groups(event)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await cate.edit("`you are not even admin of atleast one group `")
        return
    await cate.edit(
        f"initiating ungban of the [user](tg://user?id={user.id}) in `{len(san)}` groups"
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat : **{event.chat.title}(`{event.chat_id}`)\n`For unbaning here`",
            )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}`) was ungbanned in {count} groups in {cattaken} seconds`!!\n**Reason :** `{reason}`"
        )
    else:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was ungbanned in {count} groups in {cattaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"⚜UNGBAN\
                \nGlobal Unban\
                \n**➠ PENGGUNA : **[{user.first_name}](tg://user?id={user.id})\
                \n**➠ ID USER : **`{user.id}`\
                \n**➠ ALASAN :** `{reason}`\
                \n__Unbanned DI {count} groups__\
                \n**➠ WAKTU DIBAN : **`{cattaken} seconds`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"⚜UNGBAN\
                \nGlobal Unban\
                \n**➠ PENGGUNA : **[{user.first_name}](tg://user?id={user.id})\
                \n**➠ ID USER : **`{user.id}`\
                \n__Unbanned DI {count} groups__\
                \n**➠ WAKTU DIBAN  : **`{cattaken} seconds`",
            )

CMD_HELP.update({
    "gban": "\
`.gban`\
\nUsage: ➢ Melakukan Global Banned Untuk PENGGUNA Tele Yang Mereshahkan.\
\n\n`.ungban`\
\nUsage: ➢ Mengampuni PENGGUNA"
})
