from . import edit_or_replay, register
import heroku3
from telethon.tl.functions.users import GetFullUserRequest
from userbot import HEROKU_APP_NAME, HEROKU_API_KEY, SUDO_USERS, CUSTOM_HELP

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = SUDO_USERS


@register(pattern="sudo ?(.*)",)
async def sudo(event):
    sudo = "True" if SUDO_USERS else "False"
    users = SUDO_USERS
    if sudo == "True":
        await edit_or_replay(event, f"**Petercord Userbot mengaktifkan**\nSudo - `Menyala`\nSudo user(s) - `{users}`")
    else:
        await edit_or_replay(event, f"**Petercord Userbot menonaktifkan**\nSudo - `Tidak Aktif`")


@register(pattern="cmdhelp ?(.*)",)
async def handler(event):
    hndlr = CUSTOM_HELP

    sudohndlr = CUSTOM_HELP
    await edit_or_replay(event, f"Command Handler - {hndlr}\nSudo Handler - {sudohndlr}")


@register(pattern="addsudo ?(.*)",)
async def tb(event):
    ok = await edit_or_replay(event, "Menambahkan sudo...")
    petercord = "SUDO_USERS"
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
        return
    heroku_var = app.config()
    if event is None:
        return
    try:
        target = await get_user(event)
    except Exception:
        await ok.edit(f"Reply to a user.")
    if sudousers:
        newsudo = f"{sudousers} {target}"
    else:
        newsudo = f"{target}"
    await ok.edit(f"Added `{target}` Sudo telah aktif mohon. Restarting.. tunggu beberapa minute...")
    heroku_var[petercord] = newsudo


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
