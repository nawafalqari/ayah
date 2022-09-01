import json
from random import choice
from flask import render_template

def load_azkar(filename:str):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

file_data = load_azkar('azkar.json')

def get_zekr(type:str='random'):
    types = list(file_data.keys())
    if type == 'random':
        return choice(file_data[choice(types)])
    if type in types:
        return choice(file_data[types[types.index(type)]])

    return choice(file_data[choice(types)])

def in_args(args, key):
    return not args.get(key, True)

def convert_shortcut(keyword):
    names = {
        'm': 'أذكار الصباح',
        'morning': 'أذكار الصباح',
        'e': 'أذكار المساء',
        'evening': 'أذكار المساء',
        'as': 'أذكار بعد السلام من الصلاة المفروضة',
        'aftersalah': 'أذكار بعد السلام من الصلاة المفروضة',
        't': 'تسابيح',
        'tsabeh': 'تسابيح',
        'bs': 'أذكار النوم',
        'beforesleeping': 'أذكار النوم',
        'wu': 'أذكار الاستيقاظ',
        'wakingup': 'أذكار الاستيقاظ',
        'qd': 'أدعية قرآنية',
        'quranicduas': 'أدعية قرآنية',
        'pd': 'أدعية الأنبياء',
        'prophetsduas': 'أدعية الأنبياء',
    }

    if keyword == 'json':
        return 'json'
    if keyword not in names:
        return False
    return names[keyword]

def get_zekr_handler(args):
    zekr_name = list(map(convert_shortcut, list(args)))
    if 'json' in zekr_name:
        zekr_name.remove('json')

        if not zekr_name:
            zekr = get_zekr()

            return json.dumps(zekr, ensure_ascii=False)

        random_zekr = choice(zekr_name)
        zekr = get_zekr(random_zekr)

        return json.dumps(zekr, ensure_ascii=False)

    if False in zekr_name:
        return '"ERROR" Unknown parameter'

    if not zekr_name:
        zekr = get_zekr()

        return json.dumps(zekr, ensure_ascii=False)

    random_zekr = choice(zekr_name)
    zekr = get_zekr(random_zekr)

    return render_template('zekr.html', zekr=json.loads(json.dumps(zekr, ensure_ascii=False)))