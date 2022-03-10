# frm Ultroid
# port by Koala @manusiarakitann
# @petercord

from . import register, edit_or_reply
from userbot import CMD_HELP, bot


@register(pattern="gcast (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await edit_or_reply(event, "`Berikan Saya Text Untuk Di Broadcast`")
    tt = event.text
    msg = tt[6:]
    kk = await edit_or_reply(event, "`• 📢 Global Broadcast Di Prosess Cok...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"**╭✠╼━━━━━━❖━━━━━━━✠╮** Broadcast Terkirim Ke =** `{done}` **Grup, Broadcast Gagal Terkirim =** `{er}`**Grup**╰✠╼━━━━━━❖━━━━━━━✠╯**")


CMD_HELP.update(
    {
        "gcast": ".gcast\
    \nBroadcast ke Seluruh Grup."
    })
