import asyncio
import functools


# edit/reply & delete
from userbot import SUDO_USERS


async def eod(event, text=None, **args):
    args["func"] = lambda e: e.via_bot_id is None
    time = args.get("time", 5)
    link_preview = args.get("link_preview", False)
    parse_mode = args.get("parse_mode", "md")
    if str(event.sender_id) in SUDO_USERS:
        replied = await event.get_reply_message()
        if replied:
            ult = await replied.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
        else:
            ult = await event.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
    else:
        ult = await event.edit(text, link_preview=link_preview, parse_mode=parse_mode)
    if time:
        await asyncio.sleep(time)
        return await ult.delete()
    return ult


# sudo


def sudo():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            if event.out or str(event.sender_id) in SUDO_USERS:
                await function(event)
            else:
                pass

        return wrapper

    return decorator


# edit or reply


async def eor(
    event,
    text,
    parse_mode=None,
    link_preview=None,
    file_name=None,
    aslink=False,
    linktext=None,
    caption=None,
):
    link_preview = link_preview or False
    reply_to = await event.get_reply_message()
    if len(text) < 4096:
        parse_mode = parse_mode or "md"
        if event.sender_id in SUDO_USERS:
            if reply_to:
                return await reply_to.reply(
                    text, parse_mode=parse_mode, link_preview=link_preview
                )
            return await event.reply(
                text, parse_mode=parse_mode, link_preview=link_preview
            )
        return await event.edit(text, parse_mode=parse_mode, link_preview=link_preview)
    asciich = ["*", "`", "_"]
    for i in asciich:
        text = re.sub(rf"\{i}", "", text)
    if aslink:
        linktext = linktext or "Message was to big so pasted to bin"
        try:
            key = (
                requests.post(
                    "https://nekobin.com/api/documents", json={"content": text}
                )
                .json()
                .get("result")
                .get("key")
            )
            text = linktext + f" [here](https://nekobin.com/{key})"
        except BaseException:
            text = re.sub(r"•", ">>", text)
            kresult = requests.post(
                "https://del.dog/documents", data=text.encode("UTF-8")
            ).json()
            text = linktext + f" [here](https://del.dog/{kresult['key']})"
        if event.sender_id in SUDO_USERS:
            if reply_to:
                return await reply_to.reply(text, link_preview=link_preview)
            return await event.reply(text, link_preview=link_preview)
        return await event.edit(text, link_preview=link_preview)
    file_name = file_name or "output.txt"
    caption = caption or None
    with open(file_name, "w+") as output:
        output.write(text)
    if reply_to:
        await reply_to.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    if event.sender_id in SUDO_USERS:
        await event.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    await event.client.send_file(event.chat_id, file_name, caption=caption)
    await event.delete()
    os.remove(file_name)


async def delete_PETERCORD(event, text, time=None, parse_mode=None, link_preview=None):
    parse_mode = parse_mode or "md"
    link_preview = link_preview or False
    time = time or 5
    if event.sender_id in SUDO_USERS:
        reply_to = await event.get_reply_message()
        PETERCORDevent = (
            await reply_to.reply(text, link_preview=link_preview, parse_mode=parse_mode)
            if reply_to
            else await event.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
        )
    else:
        PETERCORDevent = await event.edit(
            text, link_preview=link_preview, parse_mode=parse_mode
        )
    await asyncio.sleep(time)
    return await PETERCORDevent.delete()
