# Плагин для воспризведения шуток из файла
# author: Miron

import random

def start(core):
    manifest = {
        "name": "Воспроизведения шуток",
        "version": "1.0",
        "require_online": False,

        "commands": {
            "шутка|шутки|шутку|утка|сутки": randomJoke,
            "рассказать шутку про|расскажи шутку про|расскажи утку про": getJoke,
            "рассказать шутку|расскажи шутку|расскажи утку": randomJoke,
            "все шутки|все сутки|все утки": allJokes
        },

        "default_options": {
            "jokes": {
                "мужика и шляпу": "нашел мужик шляпу, а она ему как раз. нашел мужик вторую шляпу, а она ему как два.",
                "окна": "вчера помыл окна, теперь у меня рассвет на два часа раньше",
            }
        }
    }
    return manifest

def start_with_options(core, manifest: dict):
    # Получаем данные
    global jokes, max_len
    jokes = manifest['options']['jokes']
    max_len = len(jokes.keys()) - 1 # Получаем точное количество шуток

def randomJoke(core, phrase):
    i = random.randint(0, max_len)
    joke = jokes[list(jokes)[i]]
    print(joke)
    core.play_voice_assistant_speech(joke)

def getJoke(core, phrase: str):
    if phrase in jokes:
        print(jokes[phrase])
        core.play_voice_assistant_speech(jokes[phrase]) # Используем переменную phrase вместо ключа
    else:
        print('Данной шутки не существует')
        core.play_voice_assistant_speech('Данной шутки не существует')

def allJokes(core, phrase):
    i = 0
    for name in jokes:
        print(str(i + 1) + '. шутка про ' + name)
        core.play_voice_assistant_speech(str(i + 1) + '. шутка про ' + name)
        i += 1