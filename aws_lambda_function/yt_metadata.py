import pytube
from pytube import YouTube



def get_metadata(URL):
    meta = pytube.YouTube(URL).thumbnail_url
    print(meta)