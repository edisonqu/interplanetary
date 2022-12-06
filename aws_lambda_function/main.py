

from fastapi import FastAPI
from yt_metadata import get_metadata


app = FastAPI()  # notice that the app instance is called `app`, this is very important.

@app.get("/")
async def read_root():
    URL = "https://www.youtube.com/watch?v=tG7wLK4aAOE"
    return {"Hello": "World"}

@app.post("/metadata/")
async def metadata(URL: str):
    return URL
