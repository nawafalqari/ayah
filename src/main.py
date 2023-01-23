from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from uvicorn import run
from os import getenv

from config import load_constants
load_constants()

from router import api, links, files
from utils.openapi import schema

app = FastAPI(
   title="Ayah",
   swagger_ui_parameters={
      "useUnsafeMarkdown": True
   },
   docs_url=getenv("DOCS_URL"),
   redoc_url=None,
)
app.openapi = schema(app)
templates = Jinja2Templates("templates")

app.include_router(api)                            # /api
app.include_router(links, include_in_schema=False) # /
app.include_router(files)                          # /files

urls = {
   "docs": getenv("DOCS_URL"),
   "github": getenv("GITHUB_URL"),
   "discord": getenv("DISCORD_URL"),
   "twitter": getenv("TWITTER_URL")
}

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def index(request: Request):
   return templates.TemplateResponse("index.html", {"request": request, "urls": urls})

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
   return FileResponse("images/ayah-full-width.png")

if __name__ == "__main__":
   
   if getenv("DEBUG") == "True":
      run("main:app", reload=True)
   else:
      run("main:app", host=getenv("HOST") or "127.0.0.1", port=int(getenv("PORT")) or 8000, workers=int(getenv("WORKERS")) or 1)