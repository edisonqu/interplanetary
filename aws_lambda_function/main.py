import asyncio

from fastapi import FastAPI
from yt_metadata import *
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()  # notice that the app instance is called `app`, this is very important.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def read_root():
    URL = "https://www.youtube.com/watch?v=tG7wLK4aAOE"
    return {"Hello": "World"}

@app.get("/metadata/{video_id}")
async def metadata(video_id: str):
    URL = "https://www.youtube.com/watch?v="+video_id
    metadata_json= {
        "url":URL,
        "thumbnail":await get_thumbnail(URL),
        "author": await get_artist(URL),
        "title" : await get_title(URL)
    }
    return metadata_json
