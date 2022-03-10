# Ilham mansiez
# PetercordBot

from math import ceil
from re import compile

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom

from platform import uname
from userbot.PetercordUserbot.cmdhelp import *
from userbot.PetercordUserbot.Petercord import *
from userbot import BOT_USERNAME, BUTTONS_IN_HELP, CMD_HELP, CMD_HELP_BOT, CUSTOM_HELP, tgbot, uid, ALIVE_NAME

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

PETERCORD_row = BUTTONS_IN_HELP
PETERCORD_emoji = "🎈"
# Petercord
# PETERCORD

bot.uid = uid


def button(page, modules):
    Row = PETERCORD_row

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i: i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append([custom.Button.inline(f"🎻 " + pair,
                                             data=f"Information[{page}]({pair})") for pair in pairs])

    buttons.append(
        [
            custom.Button.inline(
                f"⏪",
                data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"),
            custom.Button.inline(
                f"🚫",
                data="close"),
            custom.Button.inline(
                f"⏩",
                data=f"page({0 if page == (max_pages - 1) else page + 1})"),
        ])
    return [max_pages, buttons]
    # Changing this line may give error in bot as i added some special cmds in
    # PETERCORDBOT channel to get this module work...

    modules = CMD_HELP


if BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "@TEAMSquadUserbotSupport":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            result = await builder.article(
                f"Hey! Only use .help please",
                text=f"🎴 PETERCORD 🎴\n\n📜 MODULES 📜 :`{len(CMD_HELP)}`\n📒 HALAMAN 📒: 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        elif event.text == '':
            result = builder.article(
                "@TEAMSquadUserbotSupport",
                text="""**Hey! This is [PETERCORDBOT.](https://t.me/TEAMSquadUserbotSupport) \nYou can know more about me from the links given below 👇**""",
                buttons=[
                    [
                        custom.Button.url(
                            "📣 CHANNEL 📣",
                            "https://t.me/UserbotTEAM_Tutorial"),
                        custom.Button.url(
                            "📢 GROUP 📢",
                            "https://t.me/TEAMSquadUserbotSupport"),
                    ],
                    [
                        custom.Button.url(
                            "✨ REPO ✨",
                            "https://github.com/Ilham77Mansiz/-PETERCORD-"),
                        custom.Button.url(
                            "🔰 TUTORIAL 🔰",
                            "https://t.me/UserbotTEAM_Tutorial")],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\\((.+?)\\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Harap Deploy PETERCORD USERBOT Anda Sendiri, Jangan Menggunakan Milik PETERCORD {DEFAULTUSER} ",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        await event.edit(
            f"🎴 PETERCORD 🎴\n\n📜 MODULES 📜 : `{len(CMD_HELP)}`\n📒 HALAMAN 📒: {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=False,
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit("MENU CLOSE PETERCORD By. Tentang Aku Dan Dia")
        else:
            reply_pop_up_alert = f"Harap Deploy Petercord Userbot Anda Sendiri, Jangan Menggunakan Milik Petercord {DEFAULTUSER}",
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(callbackquery.CallbackQuery(
        data=compile(b"Information\\[(\\d*)\\]\\((.*)\\)")))
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Harap Deploy PETERCORD USERBOT Anda Sendiri, Jangan Menggunakan Milik PETERCORD {DEFAULTUSER} ",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "📩 " + cmd[0], data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i: i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("⏪", data=f"page({page})")])
        await event.edit(
            f"⬇️File: `{commands}`\n📩Number of commands : `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(callbackquery.CallbackQuery(data=compile(
        b"commands\\[(.*)\\[(\\d*)\\]\\]\\((.*)\\)")))
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Harap Deploy PETERCORD USERBOT Anda Sendiri, Jangan Menggunakan Milik PETERCORD {DEFAULTUSER} ",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"⬇️File: `{cmd}`\n\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"⬇️Terdata: {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                result += f"❌BERBAHAYA: {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"⬇️Terdata: {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
        else:
            result += f"⬇️Terdata: {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"❌BERBAHAYA: {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"ℹ️Info: {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"🛠 DAFTAR PETERCORD\n Commands: `{CUSTOM_HELP[:1]}{command['command']}`\n"
        else:
            result += f"🛠 PERINTAH\n Commands: `{CUSTOM_HELP[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"💬 PESAN: `{command['usage']}`\n"
        else:
            result += f"⌨ DAFTAR PETERCORD: `{command['usage']}`\n"
            result += f"📩 SAMPEL MODULES: `{COMMAND_HAND_LER[:1]}{command['example']}`\n"

        await event.edit(
            result,
            buttons=[
                custom.Button.inline("⏪", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )
