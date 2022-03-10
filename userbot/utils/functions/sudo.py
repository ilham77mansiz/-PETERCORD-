from userbot import bot, SUDO_USERS
petercord_bot = bot


def str_to_list(text):  # Returns List
    return text.split(" ")


def list_to_str(list):  # Returns String
    str = ""
    for x in list:
        str += f"{x} "
    return str.strip()


def are_all_nums(list):  # Takes List , Returns Boolean
    flag = True
    for item in list:
        if not item.isdigit():
            flag = False
            break
    return flag


def get_sudos():  # Returns List
    sudos = SUDO_USERS
    if sudos is None or sudos == "":
        return [""]
    else:
        return str_to_list(sudos)


def is_sudo(id):  # Take int or str with numbers only , Returns Boolean
    if not str(id).isdigit():
        return False
    sudos = get_sudos()
    if str(id) in sudos:
        return True
    else:
        return False


def add_sudo(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    if not id.isdigit():
        return False
    try:
        sudos = get_sudos()
        sudos.append(id)
        SUDO_USERS, list_to_str(sudos))
        return True
    except Exception as e:
        print(f"Petercord LOG : // functions/sudos/add_sudo : {e}")
        return False


def del_sudo(id):  # Take int or str with numbers only , Returns Boolean
    id=str(id)
    if not id.isdigit():
        return False
    try:
        sudos=get_sudos()
        sudos.remove(id)
        SUDO_USERS, list_to_str(sudos))
        return True
    except Exception as e:
        print(f"Petercord LOG : // functions/sudos/del_sudo : {e}")
        return False


def is_fullsudo(id):
    if id == petercord_bot.uid:
        return True
    id=str(id)
    x=SUDO_USERS
    if x:
        if id in x:
            return True
        return
    return
