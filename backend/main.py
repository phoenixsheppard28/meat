from fastapi import FastAPI, Depends
from httpx import AsyncClient
from typing import Annotated
from bs4 import BeautifulSoup
import re
from sqlmodel.orm.session import Session
from database import get_db
import models

hi = []
app = FastAPI()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.google.com",
}


@app.get("/")
async def now():
    pass


async def createCertifiedHumane(db: Annotated[Session, Depends(get_db)]):
    URL = "https://certifiedhumane.org/take-action-for-farm-animals/shop/"
    CERTIFICATION = "Certified Humane"

    async with AsyncClient(headers=headers) as client:
        res = await client.get(URL)

    soup = BeautifulSoup(res.text, "lxml")
    rows = soup.find_all(class_=re.compile(r"^row-\d+$"))
    data = [row.get_text(strip=True, separator=",").split(",")[0] for row in rows]
    data = data[1:]

    m = [models.Brand(id=brand_name) for brand_name in data]
    certification_obj = models.Certification(id=CERTIFICATION)
    for d in m:
        d.certifications.append(certification_obj)
    for brand in m:
        db.add(brand)

    db.commit()
