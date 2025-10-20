# Плагин для воспроизведения шуток из файла
# author: Miron

import random


def start(core):
    manifest = {
        "name": "Воспроизведения шуток",
        "version": "1.1",
        "require_online": False,
        "description": "Простой плагин для прочтения шуток/анекдотов. Список шуток настраивается в файле конфига.\n"
                       "Шутки/анекдоты записываются в следующем формате: (про) \"название\": \"содержание\".\n"
                       "Предупреждение: через web-менеджер настроек нельзя изменить название анекдота/шутки, или добавить новый.",

        "commands": {
            "шутка|шутки|шутку|утка|сутки|щука|щуки|щуку": randomJoke,
            "рассказать шутку про|расскажи шутку про|расскажи утку про": getJoke,
            "рассказать шутку|расскажи шутку|расскажи утку|рассказать щуку": randomJoke,
            "все шутки|все сутки|все утки|все шутка": allJokes
        },

        "default_options": {
            "мужика и шляпу": "нашел мужик шляпу, а она ему как раз. нашел мужик вторую шляпу, а она ему как два.",
            "окна": "вчера помыл окна, теперь у меня рассвет на два часа раньше",
        }
    }
    return manifest


def start_with_options(core, manifest: dict):
    # Получаем данные
    global jokes, max_len
    jokes = manifest['options']
    max_len = len(jokes.keys()) - 1 # Получаем точное количество шуток


def randomJoke(core, phrase):
    i = random.randint(0, max_len)
    joke = jokes[list(jokes)[i]]
    print(joke)
    core.play_voice_assistant_speech(joke)


def getJoke(core, phrase: str):
    if phrase in list(jokes.keys()):
        print(jokes[phrase])
        core.play_voice_assistant_speech(jokes[phrase]) # Используем переменную phrase вместо ключа
    else:
        print('Шутка или анекдот с этим названием не найдена.')
        core.play_voice_assistant_speech('Шутка или анекдот с этим названием не найдена.')


def allJokes(core, phrase):
    i = 0
    for name in jokes:
        print(str(i + 1) + '. шутка про ' + name)
        core.play_voice_assistant_speech(str(i + 1) + '. шутка про ' + name)
        i += 1
