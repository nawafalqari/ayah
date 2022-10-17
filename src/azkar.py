from json import load, dumps
from random import choice

def load_data(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        return load(file)

file_data = load_data("data/azkar.json")

def get_zekr(args: dict):
    zker_name = list(map(convert_shortcut, list(args)))
    if "json" in zker_name:
        zker_name.remove("json")
        if not zker_name:
            zekr = get()
            return dumps(zekr, ensure_ascii=False)
        random_zekr = choice(zker_name)
        zekr = get(random_zekr)
        return dumps(zekr, ensure_ascii=False)
    if not zker_name:
        zekr = get()
        return dumps(zekr, ensure_ascii=False)
    random_zekr = choice(zker_name)
    zekr = get(random_zekr)
    return dumps(zekr, ensure_ascii=False)


def get(type: str = "random"):
    types = list(file_data.keys())
    if type == "random":
        return choice(file_data[choice(types)])
    if type in types:
        return choice(file_data[types[types.index(type)]])
    return choice(file_data[choice(types)])


def in_args(args, key):
    return not args.get(key, True)


def convert_shortcut(keyword):
    names = {
        "m": "أذكار الصباح",
        "morning": "أذكار الصباح",
        "e": "أذكار المساء",
        "evening": "أذكار المساء",
        "as": "أذكار بعد السلام من الصلاة المفروضة",
        "aftersalah": "أذكار بعد السلام من الصلاة المفروضة",
        "t": "تسابيح",
        "tsabeh": "تسابيح",
        "bs": "أذكار النوم",
        "beforesleeping": "أذكار النوم",
        "wu": "أذكار الاستيقاظ",
        "wakingup": "أذكار الاستيقاظ",
        "qd": "أدعية قرآنية",
        "quranicduas": "أدعية قرآنية",
        "pd": "أدعية الأنبياء",
        "prophetsduas": "أدعية الأنبياء",
    }
    if keyword == "json":
        return "json"
    if keyword not in names:
        return False
    return names[keyword]