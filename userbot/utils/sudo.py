from userbot import bot, SUDO_USERS, SUDO

CMD_HELP = {}
petercord_bot = bot


def sudoers():
    return SUDO_USERS


def should_allow_sudo():
    if SUDO == "True":
        return True
    else:
        return False


def owner_and_sudos():
    return [str(petercord_bot.uid), *sudoers()]
