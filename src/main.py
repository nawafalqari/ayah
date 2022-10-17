from json import dumps
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, PlainTextResponse, FileResponse
from uvicorn import run

from azkar import get_zekr
from azkar import file_data as azkar_data

from quran import get
from quran import file_data as quran_data

app = FastAPI(title="Azkar API", description="API للأذكار")

@app.get("/")
def index():
   return RedirectResponse("https://github.com/nawafalqari/azkar-api")

@app.get("/zekr")
def zekr_route(request: Request):
   return PlainTextResponse(get_zekr(request.query_params._dict))

@app.get("/azkar.json")
def azkar_file():
   return PlainTextResponse(dumps(azkar_data, indent=3, ensure_ascii=False))

@app.get("/azkar-minified.json")
def azkar_file_minified():
   return PlainTextResponse(dumps(azkar_data, ensure_ascii=False))

@app.get("/quran")
def quran_route(sura:str=None, jozz:int=None, page:int=None):
   return PlainTextResponse(get(sura, jozz, page))

@app.get("/quran/{page}")
def quran_page(page:int):
   path = f"data/quran/{page}.jpg"
   try:
      with open(path):
         pass

      return FileResponse(f"data/quran/{page}.jpg")
   except:
      return {"err": True, "message": "invalid page number"}


@app.get("/quran.json")
def quran_file():
   return PlainTextResponse(dumps(quran_data, indent=3, ensure_ascii=False))

@app.get("/quran-minified.json")
def quran_file_minified():
   return PlainTextResponse(dumps(quran_data, ensure_ascii=False))

if __name__ == "__main__":
   run("main:app", host="0.0.0.0", workers=3)