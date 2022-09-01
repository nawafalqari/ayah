from json import load
from random import choice

def load_azkar(filename:str):
   with open(filename, 'r', encoding='utf-8') as file:
      return load(file)

file_data = load_azkar('azkar.json')

def getZekr(args:dict):
   zekrNames = list(map(convertShortcut, list(args)))

   if "json" in zekrNames:
      zekrNames.remove("json")

      if not zekrNames:
         zekr = get()

         return zekr

      randomZekr = choice(zekrNames)
      zekr = get(randomZekr)

      return zekr

   if not zekrNames:
      zekr = getZekr()

      return zekr

   randomZekr = choice(zekrNames)
   zekr = get(randomZekr)

   return zekr

def get(type:str="random"):
   types = list(file_data.keys())
   if type == 'random':
      return choice(file_data[choice(types)])
   if type in types:
      return choice(file_data[types[types.index(type)]])

   return choice(file_data[choice(types)])

def inArgs(args, key):
   return not args.get(key, True)


def convertShortcut(keyword):
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