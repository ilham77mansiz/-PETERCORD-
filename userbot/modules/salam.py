from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, bot as Petercord
from . import register, petercordbot, petercordsudo, edit_or_reply

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum warahmatullahi Bismillah cari teman ada yang mau gak?")


@Petercord.on(petercordbot(pattern=r"p$", outgoing=True))
@Petercord.on(petercordsudo(pattern=r"p$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`Assalamu'alaikum warahmatullahi Bismillah cari teman ada yang mau gak?`")


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum warahmatullahi wb😊")


@Petercord.on(petercordbot(pattern=r"l$", outgoing=True))
@Petercord.on(petercordsudo(pattern=r"l$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`Wa'alaikumussalam Semoga bermanfaat salamnya`")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumussalam Semoga bermanfaat salamnya")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumussalam Semoga bermanfaat salamnya")


CMD_HELP.update({
    "salam":
    "`.P`\
\nUsage: Untuk Memberi salam.\
\n\n`.L`\
\nUsage: Untuk Menjawab Salam."
})
