from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from os import getenv

router = APIRouter()

@router.get("/discord")
def discord():
   return RedirectResponse(getenv("DISCORD_URL"), 308)

@router.get("/twitter")
def twitter():
   return RedirectResponse(getenv("TWITTER_URL"), 308)