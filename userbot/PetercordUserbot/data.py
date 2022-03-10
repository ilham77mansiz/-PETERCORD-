# Thanks full TEAM ULTROID
# PORTED BY ILHAM MANSIZ @diemmmmmmmmmm
# PETERCORD USERBOT
# CREDITS @diemmmmmmmmmm TEAM ULTROID


from time import gmtime, strftime
from traceback import format_exc

from telethon import events

import inspect
import re
import sys
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from time import gmtime, strftime
from userbot.utils.tools import bash
from userbot.utils.tools import time_formatter
from telethon import __version__ as telever
from telethon import events
from telethon.errors.rpcerrorlist import ChatSendInlineForbiddenError, FloodWaitError
from telethon.utils import get_display_name
from .File import blacklist_chats_list
from userbot.modules.sql_helper.globals import gvarstatus

from userbot import BOTLOG_CHATID, CMD_HELP, CUSTOM_HELP, LOGS, SUDO_USERS
from userbot.utils.sudo import petercord_bot
from userbot.utils._wrappers import eor


hndlr = "\\" + CUSTOM_HELP


def petercord_cmd(allow_sudo=True, **args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args["pattern"]
    groups_only = args.get("groups_only", False)
    admins_only = args.get("admins_only", False)
    allow_sudo = args.get("allow_sudo", True)
    args.get("allow_edited_updates", False)
    args["incoming"] = args.get("incoming", False)
    args["outgoing"] = True
    if bool(args["incoming"]):
        args["outgoing"] = False

    if pattern is not None:
        if pattern.startswith(r"\#"):
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(hndlr + pattern)
        reg = re.compile("(.*)")
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = (
                    cmd.group(1)
                    .replace("$", "")
                    .replace("?(.*)", "")
                    .replace("(.*)", "")
                    .replace("(?: |)", "")
                    .replace("| ", "")
                    .replace("( |)", "")
                    .replace("?((.|//)*)", "")
                    .replace("?P<shortname>\\w+", "")
                )
            except BaseException:
                pass
            try:
                CMD_HELP[file_test].append(cmd)
            except BaseException:
                CMD_HELP.update({file_test: [cmd]})
        except BaseException:
            pass

    if gvarstatus("blacklist_chats") is not None:
        args["blacklist_chats"] = True
        args["chats"] = blacklist_chats_list()

    if "admins_only" in args:
        del args["admins_only"]
    if "groups_only" in args:
        del args["groups_only"]

    if "allow_edited_updates" in args:
        del args["allow_edited_updates"]

    def decorator(func):
        async def wrapper(event):
            if not allow_sudo:
                if not event.out:
                    return
            if not event.out and (str(event.sender_id) not in SUDO_USERS):
                return
            chat = await event.get_chat()
            naam = get_display_name(chat)
            if event.fwd_from:
                return
            if groups_only and event.is_private:
                return await eor(event, "`Use this in group/channel.`")
            if admins_only and not chat.admin_rights:
                return await eor(event, "`I am not an admin.`")
            try:
                await func(event)
            except FloodWaitError as fwerr:
                await petercord_bot.send_message(
                    int(BOTLOG_CHATID),
                    f"`FloodWaitError:\n{str(fwerr)}\n\nSleeping for {time_formatter((fwerr.seconds + 10)*1000)}`",
                )
                sleep(fwerr.seconds + 10)
                await petercord_bot.send_message(
                    int(BOTLOG_CHATID),
                    "`Bot is working again`",
                )
                await petercord_bot.send_message(
                    int(BOTLOG_CHATID),
                    "`Bot is working again`",
                )
            except ChatSendInlineForbiddenError:
                return await eor(event, "`Inline Locked In This Chat.`")
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException as e:
                LOGS.exception(e)
                date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                ftext = "**Petercord  Client Error:** `Forward this to` @TEAMSquadUserbotSupport\n\n"
                ftext += "`Py-Petercord Version: " + str(telever)
                ftext += "\n Petercord  Version: " + str(telever)
                ftext += "\nTelethon Version: " + str(telever) + "\n\n"
                ftext += "--------START  Petercord CRASH LOG--------"
                ftext += "\nDate: " + date
                ftext += "\nGroup: " + str(event.chat_id) + " " + str(naam)
                ftext += "\nSender ID: " + str(event.sender_id)
                ftext += "\nReplied: " + str(event.is_reply)
                ftext += "\n\nEvent Trigger:\n"
                ftext += str(event.text)
                ftext += "\n\nTraceback info:\n"
                ftext += str(format_exc())
                ftext += "\n\nError text:\n"
                ftext += str(sys.exc_info()[1])
                ftext += "\n\n--------END  Petercord  CRASH LOG--------"
                ftext += "\n\n\nLast 5 commits:\n"

                stdout, stderr = await bash('git log --pretty=format:"%an: %s" -5')
                result = str(stdout.strip()) + str(stderr.strip())

                ftext += result + "`"

                await petercord_bot.send_message(
                    int(BOTLOG_CHATID),
                    ftext,
                )

        petercord_bot.add_event_handler(wrapper, events.NewMessage(**args))
        try:
            CMD_HELP[file_test].append(wrapper)
        except Exception:
            CMD_HELP.update({file_test: [wrapper]})
        return wrapper

    return decorator
