from json import load
from os import getenv
from fastapi import HTTPException
from arabic_reshaper import ArabicReshaper

def load_quran() -> dict:
   with open(getenv("QURAN_FILEPATH"), "r", encoding="utf-8") as file:
      return load(file)

def get_suras_names():
   suras_names = []
   for aya in data:
      name = aya["sura_name_ar"]
      if name in suras_names:
         continue
      suras_names.append(name)

   return suras_names

data = load_quran()
reshaper = ArabicReshaper({"delete_harakat": True})
suras = get_suras_names()

def get_quran(sura: str = None, jozz: int = None, page: int = None):
   if sura:
      return get_sura(sura)
   elif jozz:
      return get_jozz(jozz)
   elif page:
      return get_page(page)
   else:
      return get_sura_data(sura, jozz, page)

def get_sura(sura: str):
   sura = get_sura_data(translate_sura(sura))
   
   # sura["img"]
   return sura

def get_jozz(jozz: int):
   jozz = get_sura_data(jozz=jozz)
   
   # jozz["img"]
   return jozz

def get_page(page: int):
   page = get_sura_data(page=page)

   # page["img"]
   return page

def get_sura_data(sura: str = None, jozz: int = None, page: int = None):
   for ayah in data:
      ayah_name = ayah["sura_name_ar"]
      ayah_jozz = ayah["jozz"]
      ayah_page = ayah["page"]

      if sura == ayah_name:
         return ayah
      if jozz == ayah_jozz:
         return ayah
      if page == ayah_page:
         return ayah

   raise HTTPException(406, "must provide a valid sura or jozz or page")

def translate_sura(sura: str):
   reshaped = reshaper.reshape(sura)
   for sura in suras:
      if reshaper.reshape(sura) == reshaped:
         return sura

   raise HTTPException(406, f"invalid sura name: {sura}")


def get_previous_sura(sura: str):
   sura = translate_sura(sura)
   if not sura:
      raise HTTPException(406, f"invalid sura name: {sura}")
   
   if sura == suras[0]:
      return {"sura": None, "first": True, "last": False}
   return {"sura": suras[suras.index(sura) - 1], "first": False, "last": False}

def get_next_sura(sura: str):
   sura = translate_sura(sura)
   if not sura:
      raise HTTPException(406, f"`invalid` sura name: {sura}")

   if sura == suras[-1]:
      return {"sura": None, "first": False, "last": True}
   return {"sura": suras[suras.index(sura) + 1], "first": False, "last": False}