# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Ported by Ilham mansiz
""" Init file which loads all of the modules """
# Ported by ilham mansiz
# Thnks full Team Ultroid ,Catuserbot ,Petercord
# Tentang aku dan dia

from ..PetercordUserbot.data import petercord_cmd
from ..utils.peter import _cattools, _catutils, _format, install_pip, reply_id
from ..PetercordUserbot.managers import edit_delete, edit_or_replay
from ..PetercordUserbot.logger import logging
from ..PetercordUserbot.cmdhelp import CmdHelp
from ..PetercordUserbot.Petercord import petercordbot, petercordsudo, edit_or_replay, register
from userbot import LOGS, bot, SUDO_USERS
from ..utils._wrappers import *


def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3] for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_modules


ALL_MODULES = sorted(__list_all_modules())
LOGS.info("Modules to load: %s", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]


# Ported by ilham mansiz
# Thnks full Team Ultroid ,Catuserbot ,Petercord
# Tentang aku dan dia

edit_or_reply = eor
Petercord = bot
ilhammansiz = register
register = register
