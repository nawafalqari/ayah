from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from uvicorn import run

from azkar_handler import getZekr

app = FastAPI(title="Azkar API", description="API للأذكار")

@app.get("/")
def index():
   return RedirectResponse("https://github.com/nawafalqari/azkar-api")

@app.get("/zekr")
def zekrRoute(request: Request):
   return getZekr(request.query_params._dict)

if __name__ == "__main__":
   run("main:app", host="0.0.0.0", workers=3)