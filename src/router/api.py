from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from os import getenv
from os.path import isfile, join

from utils.adkar import get_dekr
from utils.quran import get_quran, suras, get_previous_sura, get_next_sura
from utils.documentation import *

router = APIRouter(prefix="/api")

@router.get("/dekr", **DEKR)
def api_dekr(types: str = "random", ignore_errors: bool = False):
   return get_dekr(types, ignore_errors=ignore_errors)

@router.get("/quran/sura/{sura:str}", **QURAN_SURA)
def api_quran_sura(sura: str):
   return get_quran(sura=sura)
   
@router.get("/quran/jozz/{jozz:int}", **QURAN_JOZZ)
def api_quran_jozz(jozz: int):
   return get_quran(jozz=jozz)
   
@router.get("/quran/page/{page:int}", **QURAN_PAGE)
def api_quran_page(page: int):
   return get_quran(page=page)


@router.get("/quran", **QURAN)
def api_quran(sura: str = None, jozz: int = None, page: int = None):
   return get_quran(sura, jozz, page)

@router.get("/quran/images/{page}", **QURAN_IMAGES, response_class=FileResponse)
def api_quran_page(page: int):
   path = join(getenv("QURAN_IMAGES_PATH"), f"{page}.jpg")

   if not isfile(path):
      raise HTTPException(406, "invalid page number")
   return FileResponse(path)

@router.get("/quran/suras", **QURAN_SURAS)
def api_quran_suras():
   return suras

@router.get("/quran/previous_sura", **QURAN_PREVIOUS_SURA)
def api_quran_previous_sura(sura: str):
   return get_previous_sura(sura)

@router.get("/quran/next_sura", **QURAN_NEXT_SURA)
def api_quran_next_sura(sura: str):
   return get_next_sura(sura)