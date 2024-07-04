import openai

__is_api_set = False
__is_init = False
__messages = []


def set_api_key(api_key):
    global __is_api_set
    openai.api_key = api_key
    __is_api_set = True
    print("Api key is set succesfully")

linktypes_first = [
("стандартная ссылка","testlink.cat"),
("почта","info@gmail.com"),
("телеграм-юзернейм","@mychannel"),
]

__model = ""
__length = 100000

def init(linkname = "thelink", linktypes=None, model = "gpt-3.5-turbo", length = 4000):
    global __messages
    global __is_init
    global __model
    global __length

    __model = model
    __length = length

    linkname = linkname.replace("<","").replace(">","").replace("/","").replace("\\","")

    if linktypes is None:
        linktypes = linktypes_first

    vars = ""
    for n in linktypes:
        vars += f"{n[0]} ({n[1]}), "

    sys_msg = f"""
    Будет отправлен текст. Необходимо выделить в нем ссылки, с помощью тега <{linkname}></{linkname}>. 
Ссылкой может являться: {vars}
Ссылка может быть написана с ошибкой. В таком случае ошибку нужно исправить. Пример:
Ввод: "Люди на politics,rus часто недопонимают других людей"
Вывод: "Люди на <{linkname}>politics.rus</{linkname}> часто недопонимают других людей"
Текст может быть похож на ссылку, но быть ошибкой. В таком случае его не нужно выделять
Ввод: "Нужно понимать, где искать Помощь.РФ готова её предоставить!"
Вывод: "Нужно понимать, где искать Помощь.РФ готова её предоставить!" - Помощь.РФ в данном случае опечатка.
Нужно выделить только то, что предоставлено среди вариантов: {vars}
В тексте могут содержаться HTML теги, если какой либо из тегов является ссылкой - его не нужно трогать или как либо изменять. Пример HTLM тегов, которые трогать не нужно: <href> <a>. Если название тега совпадает с <{linkname}>, его все еще не нужно никак менять.
Могут быть конструкции, похожие на ссылки из за опечатки, но ими не являться. Например, если слово после точки будет написано через пробел от второго составляющего слова. В таком случае данную конструкцию НЕ НУЖНО выделять как ссылку. Примеры возможных ошибок: люди живут счастливо.ру лет у нас самый вкусный; этим занимаются большие федерации.ком пании делают все, чтобы…; мы поплыли на север.су дно устойчиво; there is a lot of nice looking countries.fr ench may be the example; there are countries with communism still.ch ina is one of them
Я отправлю текст - нужно написать ТОЛЬКО измененный текст, ничего не добавляя от себя.
    """

    __messages = [
        {"role": "system", "content": sys_msg},
    ]

    __is_init = True


def add_tags_to_text(text):
    is_not_finished = True
    res = ""

    textarr = split_text(text,__length)

    for txt in textarr:
        while is_not_finished:
            try:
                res += linkify(txt)
                is_not_finished=True
            except RuntimeError:
                pass
    return res

def split_text(text,n=4000):
    return [text[i:i + n] for i in range(0, len(text), n)]

def linkify(text):
    global __messages
    if __is_api_set and __is_init:
        print("Text is processing...")
        __messages.append({"role": "user", "content": text})
        response = openai.ChatCompletion.create(
            model=__model,
            messages=__messages,
        )

        result = response['choices'][0]['message']['content']
        return result

    else:
        if __is_api_set:
            print("API key was never set! Use set_api_key(api_key)!")
        elif __is_init:
            print("Program was never set up! Use init(linkname, linktypes) to set it up!")
        return "None"
