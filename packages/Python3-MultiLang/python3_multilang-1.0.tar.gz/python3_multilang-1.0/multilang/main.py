import locale
import os

_folder   = 'languages/' # Standard folder if none set
_fallback = 'en_EN'      # Standard fallback file if none set

def get_language():
    return locale.getlocale()[0]

def set_folder(folder):
    global _folder
    _folder = folder

def set_fallback_language(language):
    global _fallback
    _fallback = language

def text(language, id):
    langs = os.listdir(_folder)
    try:
        with open(f'{_folder}{language}', 'r') as f:
            cont = f.readlines()
        with open(f'{_folder}{_fallback}', 'r') as f:
            cont_fallback = f.readlines()
    except FileNotFoundError:
        print(f"ERROR: language file doesn't exist! ({language})")
        with open(f'{_folder}{_fallback}', 'r') as f:
            cont = f.readlines()
    messages = {}
    try:
        for message in cont:
            message = str(message).split(';')
            messages[message[0]] = message[1]

        TEXT = messages[str(id)]
        return TEXT
    except KeyError:
        try:
            for message in cont_fallback:
                message = str(message).split(';')
                messages[message[0]] = message[1]

            TEXT = messages[str(id)]
            return TEXT
        except Exception:
            print(f"ERROR: id doesn't exist! ({id})")