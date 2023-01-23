from fastapi import APIRouter
from fastapi.responses import FileResponse
from os import getenv
from os.path import join

from utils.adkar import data as adkar
from utils.quran import data as quran
from utils.documentation import ADKAR_JSON, QURAN_JSON

router = APIRouter(prefix="/files")

@router.get("/adkar.json", **ADKAR_JSON)
def files_adkhar():
   return adkar

@router.get("/quran.json", **QURAN_JSON)
def files_quran():
   return quran

@router.get("/{file}")
def images_file(file: str):
   return FileResponse(join(getenv("IMAGES_PATH"), file))