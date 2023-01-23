from os import environ
from os.path import join
from pathlib import Path
from multiprocessing import cpu_count

DEBUG = True
HOST = "127.0.0.1"
PORT = 8000
WORKERS = (2 * cpu_count()) + 1

BASE_DIR = str(Path(__file__).resolve().parent)
ADKAR_FILEPATH = join(BASE_DIR, "data", "adkar.json")
QURAN_FILEPATH = join(BASE_DIR, "data", "quran.json")
QURAN_IMAGES_PATH = join(BASE_DIR, "data", "images")

IMAGES_PATH = join(BASE_DIR, "images")

DISCORD_URL = "https://discord.gg/Az8McWNAcg"
TWITTER_URL = "https://twitter.com/nawafalqari2"
GITHUB_URL = ""

DOCS_URL = "/docs"
DOCS_TITLE = "Ayah - آية"
DOCS_VERSION = "1.0.0BETA"
DOCS_DESCRIPTION = "API مفتوح المصدر للأذكار والقرآن والأحاديث"
DOCS_LISENCE_NAME = "MIT"
DOCS_LISENCE_URL = ""

TERMS_URL = "/terms"

def load_constants():
   constants = globals().copy()

   for const, value in constants.items():
      if const.isupper():
         environ[const] = str(value)