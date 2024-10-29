from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import random
import os
from pydantic import BaseModel
from typing import Optional, Any

urls = [
    "https://www.commitstrip.com/wp-content/uploads/2020/10/Strip-Daily-meeting-650-finalenglish.jpg",
    "https://www.commitstrip.com/wp-content/uploads/2020/09/Strip-Devis-Cloud-650-finalenglishv2.jpg",
    "https://www.commitstrip.com/wp-content/uploads/2021/04/Strip-Les-erreurs-qui-en-cachent-dautres-650-finalenglish.jpg",
    "https://www.commitstrip.com/wp-content/uploads/2021/12/Strip-Donn%C3%A9e-de-prod-en-staging-650-finalenglish.jpg",
    "https://www.commitstrip.com/wp-content/uploads/2021/02/Stripo-Cest-lhistoire-de-PHP-et-React-800-finalenglish.jpg",
    "https://www.commitstrip.com/wp-content/uploads/2020/05/Strip-Lavis-Chloroquine-650-finalenglish.jpg",
    "https://www.commitstrip.com/wp-content/uploads/2020/03/Strip-Troll-de-prof-650-finalenglish.jpg",
    "https://www.commitstrip.com/wp-content/uploads/2019/10/Strip-2019-lann%C3%A9e-du-Python-650-finalenglishLOGO.jpg",
    "https://www.commitstrip.com/wp-content/uploads/2019/08/Strip-Bilan-de-projet-650-finalenglishV2.jpg"
]

class Comics(BaseModel):
    #book_id: ObjectId()
    uri: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "uri": "Strip-Bilan-de-projet"
            }
        }

app = FastAPI()
templates = Jinja2Templates(directory=os.path.abspath(os.path.expanduser('templates')))

@app.get("/")
def comic(request: Request):
    comicNum = random.randrange(0,9)
    comicUrl = urls[comicNum]
    pod_name = os.getenv("HOSTNAME")
    return templates.TemplateResponse('index.html', context={'request': request, 'comicUrl': comicUrl, 'pod_name': pod_name})
