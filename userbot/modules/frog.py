# Yang Hapus Besok Mati Aminnn
# Port By @Vckyouuu
# Tentang Aku Dan dia


from telethon.errors import ChatSendStickersForbiddenError

from . import edit_or_reply, petercord_cmd, register
from userbot import CMD_HELP, bot


@petercord_cmd(pattern="frog ?(.*)",)
@register(pattern="frog ?(.*)", ilhammansiz=True)
async def honkasays(event):
    await edit_or_reply(event, "`Sedang Memprosess Ya Anjeng, Kontol Diem kau lagi aku cari..`")
    text = event.pattern_match.group(1)
    if not text:
        return await edit_or_reply(event, "`Beri Aku Bebeberapa Teks Ya anjeng babi lah kau, Contoh .frog Kontol kau`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text) <= 9:
            results = await bot.inline_query("honka_says_bot", text)
            await results[2].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text) >= 14:
            results = await bot.inline_query("honka_says_bot", text)
            await results[0].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await bot.inline_query("honka_says_bot", text)
            await results[1].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await edit_or_reply(event, "`Kontollah! Saya tidak bisa menggunakan hal-hal sebaris di sini...Anjeng yang betullah`")
    except ChatSendStickersForbiddenError:
        await edit_or_reply(event, "Maaf ya Kontol, saya tidak bisa mengirim stiker ke sini Babi!!")

CMD_HELP.update(
    {"frog": "**Modules:** __Frog__\n\n**Perintah:** `.frog <teks>`\
    \n**Penjelasan:** Mengirim sebuah animasi sticker kodok."})
