# Port ilham mansiz
from datetime import datetime

from pytz import timezone
from userbot.events import register
from userbot import CMD_HELP, bot, LOGS, CLEAN_WELCOME, BOTLOG_CHATID
from telethon.events import ChatAction


@bot.on(ChatAction)
async def goodbye_to_chat(event):
    try:
        from userbot.modules.sql_helper.goodbye_sql import get_current_goodbye_settings
        from userbot.modules.sql_helper.goodbye_sql import update_previous_goodbye
    except AttributeError:
        return
    cws = get_current_goodbye_settings(event.chat_id)
    if cws:
        """user_added=False,
        user_joined=False,
        user_left=True,
        user_kicked=True"""
        if (event.user_joined
                or event.user_added) and not (await event.get_user()).bot:
            if CLEAN_WELCOME:
                try:
                    await event.client.delete_messages(event.chat_id,
                                                       cws.previous_goodbye)
                except Exception as e:
                    LOGS.warn(str(e))
            a_user = await event.get_user()
            chat = await event.get_chat()
            me = await event.client.get_me()

            # Current time in UTC
            now_utc = datetime.now(timezone("UTC"))

            # Convert to Jakarta time zone
            jakarta_timezone = now_utc.astimezone(timezone("Asia/Jakarta"))
            if jakarta_timezone.hour < 4:
                pass
            elif 4 <= jakarta_timezone.hour < 6:
                pass
            elif 6 <= jakarta_timezone.hour < 11:
                pass
            elif 11 <= jakarta_timezone.hour < 13:
                pass
            elif 13 <= jakarta_timezone.hour < 15:
                pass
            elif 15 <= jakarta_timezone.hour < 17:
                pass
            elif 17 <= jakarta_timezone.hour < 19:
                pass
            else:
                pass

            title = chat.title if chat.title else "Grup Ini"
            participants = await event.client.get_participants(chat)
            count = len(participants)
            mention = "[{}](tg://user?id={})".format(a_user.first_name,
                                                     a_user.id)
            my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
            first = a_user.first_name
            last = a_user.last_name
            if last:
                fullname = f"{first} {last}"
            else:
                fullname = first
            username = f"@{a_user.username}" if a_user.username else mention
            userid = a_user.id
            my_first = me.first_name
            my_last = me.last_name
            if my_last:
                my_fullname = f"{my_first} {my_last}"
            else:
                my_fullname = my_first
            my_username = f"@{me.username}" if me.username else my_mention
            file_media = None
            current_saved_goodbye_message = None
            if cws and cws.f_mesg_id:
                msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                        ids=int(cws.f_mesg_id))
                file_media = msg_o.media
                current_saved_goodbye_message = msg_o.message
            elif cws and cws.reply:
                current_saved_goodbye_message = cws.reply
            current_message = await event.reply(
                current_saved_goodbye_message.format(mention=mention,
                                                     title=title,
                                                     count=count,
                                                     first=first,
                                                     last=last,
                                                     fullname=fullname,
                                                     username=username,
                                                     userid=userid,
                                                     my_first=my_first,
                                                     my_last=my_last,
                                                     my_fullname=my_fullname,
                                                     my_username=my_username,
                                                     my_mention=my_mention),
                file=file_media)
            update_previous_goodbye(event.chat_id, current_message.id)


@register(outgoing=True, pattern=r"^.setgoodbye(?: |$)(.*)")
async def save_goodbye(event):
    try:
        from userbot.modules.sql_helper.goodbye_sql import add_goodbye_setting
    except AttributeError:
        return await event.edit("`Berjalan Pada Mode Non-SQL!`")
    msg = await event.get_reply_message()
    string = event.pattern_match.group(1)
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"📢GOODBYE PETERCORD📢 \nID GRUP: {event.chat_id}"
                "\nPetercord Memasang Pesan Perintah GOODBYE Digrup, Ini Adalah Catatan Pesan Goodbye "
                "Mohon Jangan Dihapus 🎸Petercord!🎸"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            return await event.edit(
                "`Untuk membuat media sebagai pesan Goodbye, BOTLOG_CHATID Harus disetel.`"
            )
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "`Berhasil Menyimpan Pesan Goodbye {} ツ`"
    if add_goodbye_setting(event.chat_id, 0, string, msg_id) is True:
        await event.edit(success.format('Disini'))
    else:
        await event.edit(success.format('Disini'))


@register(outgoing=True, pattern="^.checkgoodbye$")
async def show_goodbye(event):
    try:
        from userbot.modules.sql_helper.goodbye_sql import get_current_goodbye_settings
    except BaseException:
        await event.edit("`Berjalan Pada Mode Non-SQL!`")
        return
    cws = get_current_goodbye_settings(event.chat_id)
    if not cws:
        await event.edit("`Pesan goodbye belum ada mohon buat.`")
        return
    elif cws and cws.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(cws.f_mesg_id))
        await event.edit(
            "`Anda telah menyimpan goodbye disini.`")
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws and cws.reply:
        await event.edit(
            "`Anda telah menyimpan goodbye disini.`")
        await event.reply(cws.reply)


@register(outgoing=True, pattern="^.rmgoodbye$")
async def del_goodbye(event):
    try:
        from userbot.modules.sql_helper.goodbye_sql import rm_goodbye_setting
    except AttributeError:
        return await event.edit("`Running on Non-SQL mode!`")
    if rm_goodbye_setting(event.chat_id) is True:
        await event.edit("`Menghapus Pesan goodbye Berhasil Dilakukan ツ`")
    else:
        await event.edit("`Anda Tidak Menyimpan Pesan goodbye Apapun Disini Petercord ツ`")


CMD_HELP.update({
    "goodbye":
    ">`.setgoodbye` <pesan goodbye> atau balas ke pesan ketik `.setgoodbye`"
    "\nUsage: Menyimpan pesan goodbye digrup."
    "\n\nFormat Variabel yang bisa digunakan dipesan goodbye:"
    "\n`{mention}, {title}, {count}, {first}, {last}, {fullname}, "
    "{userid}, {username}, {my_first}, {my_fullname}, {my_last}, "
    "{my_mention}, {my_username}`"
    "\n\n>`.checkgoodbye`"
    "\nUsage: Check pesan goodbye yang anda simpan."
    "\n\n>`.rmgoodbye`"
    "\nUsage: Menghapus pesan goodbye yang anda simpan."
})