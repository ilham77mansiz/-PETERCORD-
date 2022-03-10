# Copyright (C) 2020 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port from UniBorg to Userbot by yincen17

import asyncio
import zipfile
from . import CmdHelp, petercord_cmd, register
from datetime import date
import time
import os
from userbot import ZIP_DOWNLOAD_DIRECTORY, bot
from userbot.utils import progress

# ====================
today = date.today()
# ====================


@petercord_cmd(pattern="compress(?: |$)(.*)")
@register(pattern="compress ?(.*)", ilhammansiz=True)
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    mone = await edit_or_reply(event, "Processing ...")

    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):

        os.makedirs(TMP_DOWNLOAD_DIRECTORY)

    if event.reply_to_msg_id:

        reply_message = await event.get_reply_message()

        try:

            time.time()

            downloaded_file_name = await borg.download_media(
                reply_message, TMP_DOWNLOAD_DIRECTORY
            )

            directory_name = downloaded_file_name

            await edit_or_reply(event, "Finish downloading to my local")

            zipfile.ZipFile(
                directory_name + ".zip",
                "w",
                zipfile.ZIP_DEFLATED).write(directory_name)

            await bot.send_file(
                event.chat_id,
                directory_name + ".zip",
                caption="Zipped By Ilham mansiez",
                force_document=True,
                allow_cache=False,
                reply_to=event.message.id,
            )

            try:

                os.remove(directory_name + ".zip")

                os.remove(directory_name)

            except BaseException:

                pass

            await edit_or_reply(event, "task Completed")

            await asyncio.sleep(3)

            await event.delete()

        except Exception as e:  # pylint:disable=C0103,W0703

            await mone.edit(str(e))

    elif input_str:

        directory_name = input_str

        zipfile.ZipFile(
            directory_name + ".zip",
            "w",
            zipfile.ZIP_DEFLATED).write(directory_name)

        await edit_or_reply(event,
                            "Local file compressed to `{}`".format(directory_name + ".zip")
                            )


@petercord_cmd(pattern="addzip(?: |$)(.*)")
@register(pattern="addzip ?(.*)", ilhammansiz=True)
async def addzip(add):
    """ Copyright (c) 2020 azrim @github"""
    # Prevent Channel Bug to use update
    if add.is_channel and not add.is_group:
        await add.edit("`Command isn't permitted on channels`")
        return
    if add.fwd_from:
        return
    if not add.is_reply:
        await add.edit("`Reply to a file to compress it.`")
        return
    mone = await add.edit("`Processing...`")
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        os.makedirs(ZIP_DOWNLOAD_DIRECTORY)
    if add.reply_to_msg_id:
        reply_message = await add.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await bot.download_media(
                reply_message,
                ZIP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "[DOWNLOADING]")
                ),
            )
            success = str(downloaded_file_name).replace("./zips/", "")
            await add.edit(f"`{success} Successfully added to list`")
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
            return


@petercord_cmd(pattern="upzip(?: |$)(.*)")
@register(pattern="upzip ?(.*)", ilhammansiz=True)
async def upload_zip(up):
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        await up.edit("`Files not found`")
        return
    mone = await up.edit("`Zipping File...`")
    input_str = up.pattern_match.group(1)
    curdate = today.strftime("%m%d%y")
    title = str(input_str) if input_str else "zipfile" + f"{curdate}"
    zipf = zipfile.ZipFile(title + '.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(ZIP_DOWNLOAD_DIRECTORY, zipf)
    zipf.close()
    c_time = time.time()
    await bot.send_file(
        up.chat_id,
        title + ".zip",
        force_document=True,
        allow_cache=False,
        reply_to=up.message.id,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, mone, c_time, "[UPLOADING]", input_str)
        ),
    )
    os.rmdir(ZIP_DOWNLOAD_DIRECTORY)
    await up.delete()


@petercord_cmd(pattern="rmzip(?: |$)(.*)")
@register(pattern="rmzip ?(.*)", ilhammansiz=True)
async def remove_dir(rm):
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        await rm.edit("`Directory not found`")
        return
    os.rmdir(ZIP_DOWNLOAD_DIRECTORY)
    await rm.edit("`Zip list removed`")


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            os.remove(os.path.join(root, file))


CmdHelp("zipfile").add_command(
    "compress", '<reply to file>', "make files to zip"
).add_command(
    "addzip", '<reply to file>', "add files to zip list"
).add_command(
    "upzip", '[optional: <zip title>]', "upload zip list"
).add_command(
    "rmzip", '[optional: <zip title>]', "clear zip list"
).add()
