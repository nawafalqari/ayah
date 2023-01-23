from json import load
from os import getenv
from random import choice
from fastapi import HTTPException

def load_adkar() -> dict:
   with open(getenv("ADKAR_FILEPATH"), "r", encoding="utf-8") as file:
      return load(file)

data = load_adkar()

def extract_types(types: str) -> str:
   return translate_shortcut(choice(types.replace(" ", "").split(",")))

def translate_shortcut(keyword):
   names = {
      "m": "أذكار الصباح",
      "e": "أذكار المساء",
      "as": "أذكار بعد السلام من الصلاة المفروضة",
      "t": "تسابيح",
      "bs": "أذكار النوم",
      "wu": "أذكار الاستيقاظ",
      "qd": "أدعية قرآنية",
      "pd": "أدعية الأنبياء",
   }
   if keyword == "random":
      return "random"
   if keyword not in names:
      return keyword
   return names[keyword]


def get_dekr(types: str, *, ignore_errors: bool = False):
   type = extract_types(types)
   types = list(data.keys())

   if type == "random" or ignore_errors:
      return choice(data[choice(types)])
   if type in types:
      return choice(data[type])

   raise HTTPException(406, f"invalid dekr type: {type}")