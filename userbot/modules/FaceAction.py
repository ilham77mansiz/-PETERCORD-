# Port By @VckyouuBitch From Geez-Projects
# # Copyright (C) 2021 Geez-Project

from . import register, CmdHelp, edit_or_replay
import asyncio


@register(pattern="ftyping ?(.*)", outgoing=True)
@register(pattern="ftyping ?(.*)", ilhammansiz=True)
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_or_replay(event, "`Incorrect Format`")
    await edit_or_replay(event, f"`Starting Fake Typing For {t} sec.`")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@register(pattern="faudio ?(.*)", outgoing=True)
@register(pattern="faudio ?(.*)", ilhammansiz=True)
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_or_replay(event, "`Incorrect Format`")
    await edit_or_replay(event, f"`Starting Fake audio recording For {t} sec.`")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@register(pattern="fvidio ?(.*)", outgoing=True)
@register(pattern="vidio ?(.*)", ilhammansiz=True)
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_or_replay(event, "`Incorrect Format`")
    await edit_or_replay(event, f"`Starting Fake video recording For {t} sec.`")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@register(pattern="fgame ?(.*)", outgoing=True)
@register(pattern="fgame ?(.*)", ilhammansiz=True)
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_or_replay(event, "`Incorrect Format`")
    await edit_or_replay(event, f"`Starting Fake Game Playing For {t} sec.`")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)


CmdHelp("fakeaction").add_command(
    'ftyping',
    '<jumlah teks>',
    'Seakan akan sedang mengetik padahal tidak').add_command(
        'faudio',
        '<jumlah teks>',
        'Berfungsi sama seperti ftyping tapi ini dalam bentuk fake audio').add_command(
            'fgame',
            '<jumlah teks>',
            'Berfungsi sama seperti ftyping tapi ini dalam bentuk fake game').add_command(
                'fvideo',
                '<jumlah teks>',
    'Berfungsi sama seperti ftyping tapi ini dalam bentuk fake vidio').add()
