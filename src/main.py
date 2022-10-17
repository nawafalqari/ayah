from json import dumps
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, PlainTextResponse, FileResponse
from uvicorn import run

from azkar import get_zekr
from azkar import file_data as azkar_data

from quran import get, get_next_sura, get_previous_sura, get_suras_names
from quran import file_data as quran_data

app = FastAPI(title="Azkar API", description="API للأذكار")

res = lambda r:PlainTextResponse(r)

@app.get("/")
def index():
   return RedirectResponse("https://github.com/nawafalqari/azkar-api")

@app.get("/zekr")
def zekr_route(request: Request):
   return res(get_zekr(request.query_params._dict))

@app.get("/azkar.json")
def azkar_file():
   return res(dumps(azkar_data, indent=3, ensure_ascii=False))

@app.get("/azkar-minified.json")
def azkar_file_minified():
   return res(dumps(azkar_data, ensure_ascii=False))

@app.get("/quran")
def quran_route(sura:str=None, jozz:int=None, page:int=None):
   return res(get(sura, jozz, page))

@app.get("/quran/{page}")
def quran_page(page:int):
   return RedirectResponse(f"https://cdn-azkar-api.nawafhq.repl.co/quran/{page}")

@app.get("/quran/info/suras")
def suras_route():
   return res(dumps(get_suras_names(), ensure_ascii=False))

@app.get("/quran/info/previous_sura")
def previous_sura_route(sura:str):
   return res(get_previous_sura(sura))

@app.get("/quran/info/next_sura")
def next_sura_route(sura:str):
   return res(get_next_sura(sura))

@app.get("/quran.json")
def quran_file():
   return res(dumps(quran_data, indent=3, ensure_ascii=False))

@app.get("/quran-minified.json")
def quran_file_minified():
   return res(dumps(quran_data, ensure_ascii=False))

if __name__ == "__main__":
   run("main:app", host="0.0.0.0", workers=3)