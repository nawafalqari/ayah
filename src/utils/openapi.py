from fastapi.openapi.utils import get_openapi
from os import getenv

def schema(app):
   def write_schema():
      schema = get_openapi(
         title=getenv("DOCS_TITLE"),
         version=getenv("DOCS_VERSION"),
         routes=app.routes,
      )
      schema["info"] = {
         "title" : getenv("DOCS_TITLE"),
         "version" : getenv("DOCS_VERSION"),
         "description" : getenv("DOCS_DESCRIPTION"),
         "termsOfService": getenv("TERMS_URL"),
         "contact": {
            "name": "Nawaf",
            "url": "https://nawafdev.com",
            "email": "nawafalqari13@gmail.com"
         },
         # "license": {
         #    "name": getenv("DOCS_LISENCE_NAME"),
         #    "url": getenv("DOCS_LISENCE_URL")
         # },
      }

      app.openapi_schema = schema
      return app.openapi_schema
   
   return write_schema