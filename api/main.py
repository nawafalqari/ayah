from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, PlainTextResponse
from uvicorn import run

from azkar_handler import get_zekr

app = FastAPI(title="Azkar API", description="API للأذكار")

@app.get("/")
def index():
   return RedirectResponse("https://github.com/nawafalqari/azkar-api")

@app.get("/zekr")
def zekr_route(request: Request):
   return PlainTextResponse(get_zekr(request.query_params._dict))

if __name__ == "__main__":
   run("main:app", host="0.0.0.0", workers=3)