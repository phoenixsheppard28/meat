from fastapi import FastAPI
from httpx import AsyncClient
from bs4 import BeautifulSoup
import re

app = FastAPI()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.google.com",
}


@app.get("/")
async def hello():
    URL = "https://certifiedhumane.org/take-action-for-farm-animals/shop/"

    async with AsyncClient(headers=headers) as client:
        res = await client.get(URL)
        print(res.text)

        soup = BeautifulSoup(res.text, "lxml")
        rows = soup.find_all(class_=re.compile(r"^row-\d+$"))
        data = [row.get_text(strip=True, separator=",").split(",")[0] for row in rows]
        data = data[1:]

        return data
