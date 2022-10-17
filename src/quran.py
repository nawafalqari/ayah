from json import load, dumps
from arabic_reshaper import ArabicReshaper

def load_data(filename: str):
   with open(filename, "r", encoding="utf-8") as file:
      return load(file)

file_data = load_data("data/quran.json")
reshaper = ArabicReshaper({"delete_harakat": True})

def get(sura, jozz, page):
   data = None
   if sura:
      data = get_sura(sura)
   elif jozz:
      data = get_jozz(jozz)
   elif page:
      data = get_page(page)
   else:
      data = get_sura_data(sura, jozz, page)

   return dumps(data, ensure_ascii=False)

def get_sura(sura:str):
   sura = find_sura(sura)
   if not sura:
      return {"err": True, "message": "Invalid sura name"}
   sura = get_sura_data(sura)
   if sura.get("err"):
      return sura

   sura["img"] = f"https://cdn-azkar-api.nawafhq.repl.co/quran/{sura['page']}"
   return sura

def get_jozz(jozz:int):
   jozz = get_sura_data(jozz=jozz)
   if jozz.get("err"):
      return jozz
   
   jozz["img"] = f"https://cdn-azkar-api.nawafhq.repl.co/quran/{jozz['page']}"
   return jozz

def get_page(page:int):
   page = get_sura_data(page=page)
   if page.get("err"):
      return page
   
   page["img"] = f"https://cdn-azkar-api.nawafhq.repl.co/quran/{page['page']}"
   return page

def get_suras_names():
   suras_names = []
   for aya in file_data:
      name = aya["sura_name_ar"]
      if name in suras_names:
         continue
      suras_names.append(name)

   return suras_names

def find_sura(sura:str):
   suras = get_suras_names()
   reshaped_sura = reshaper.reshape(sura)
   for s in suras:
      if reshaper.reshape(s) == reshaped_sura:
         return s

def get_sura_data(sura:str=None, jozz:int=None, page:int=None):

   for aya in file_data:
      aya_name = aya["sura_name_ar"]
      aya_jozz = aya["jozz"]
      aya_page = aya["page"]

      if sura == aya_name:
         return aya
      if jozz == aya_jozz:
         return aya
      if page == aya_page:
         return aya

   return {"err": True, "message": "Invalid parameter: (sura) or (jozz) or (page)"}

def get_previous_sura(sura:str):
   sura = find_sura(sura)
   if not sura:
      return dumps({"err": True, "message": "Invalid sura name"})
   suras = get_suras_names()
   if sura == suras[0]:
      return dumps({"first": True})
   return dumps({"sura": suras[suras.index(sura)-1]}, ensure_ascii=False)

def get_next_sura(sura:str):
   sura = find_sura(sura)
   if not sura:
      return dumps({"err": True, "message": "Invalid sura name"})
   suras = get_suras_names()
   if sura == suras[-1]:
      return dumps({"last": True})
   return dumps({"sura": suras[suras.index(sura)+1]}, ensure_ascii=False)