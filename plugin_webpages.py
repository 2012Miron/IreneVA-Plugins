import webbrowser

def start(core):
    manifest = {
        "name": 'Открытие ссылок',
        "version": '1.0',
        "require_online": False,
        "commands": {
            "открой": openlink
        },

        "default_options": {
            "links": {
                "гугл": 'https://www.google.com/',
                "гит хаб": 'https://github.com/',
                "плагины ирины": 'https://github.com/janvarev/Irene-Voice-Assistant/issues/1'
            }
        }
    }
    return manifest

def start_with_options(core, manifest: dict):
    global links # Делаем ссылки доступными для чтения
    links = manifest['options']['links']

def openlink(core, phrase: str):
    if phrase in list(links.keys()):
        webbrowser.open(links[phrase], 2)
