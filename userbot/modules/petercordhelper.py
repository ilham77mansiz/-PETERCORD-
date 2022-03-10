""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.mintabantuan$")
async def usit(e):
    await e.edit(
        f"**Hai Petercord {DEFAULTUSER} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/bismillahselaluadaa)"
        "\n[Repo](https://github.com/ilham77mansiz/-PETERCORD-)"
        "\n[Instagram](Instagram.com/mansiez_ilham2)")


@register(outgoing=True, pattern="^.varsraw$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/ilham77mansiz/-PETERCORD-/Petercord-Userbot/varshelper.txt)")


CMD_HELP.update({
    "bantuan":
    "`.mintabantuan`\
\nUsage: Bantuan Untuk Petercord-Userbot.\
\n`.varsraw`\
\nUsage: Melihat Daftar Vars."
})
