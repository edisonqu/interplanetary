from __future__ import unicode_literals

import json
import os
from yt_dlp import YoutubeDL
import boto3
import requests
from pytube import YouTube



def lambda_handler(event, context):
    print(event)
    bucket = 'songbucket'

    last_string = event['rawQueryString']
    URLS = "https://www.youtube.com/watch?" + last_string

    print(URLS)

    ydl_opts = {'format': 'm4a/bestaudio/best', 'outtmpl': '/tmp/%(title)s-%(id)s.%(ext)s',
                'ffmpeg_location': '/opt/ffmpeg',
                'postprocessors': [{  # Extract audio using ffmpeg
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }]

                }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URLS, download=True)
        metadata = json.loads(json.dumps(ydl.sanitize_info(info)))

    res = []
    for root, dir, files in os.walk("/tmp/"):
        for file in files:
            if file.endswith(".mp3"):
                res.append(os.path.join(root, file))

    song_filename = res[0]

    with open(f"{song_filename}", 'rb') as f:
        file = f.read()

    new_song = song_filename.lstrip("/tmp/")

    print(new_song)



    url = "https://api.nft.storage/upload"
    headers = {
        "Content-Type": "*/*",
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('NFT_STORAGE')}"
    }

    with open(f"{song_filename}", 'rb') as f:
        file = f.read()


    ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
    SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")
    ENDPOINT_URL = os.getenv("ENDPOINT_URL")

    storage_options = {
        'key': ACCESS_KEY_ID,
        'secret': SECRET_ACCESS_KEY,
        'client_kwargs': {
            'endpoint_url': ENDPOINT_URL
        }
    }
    cmd = f"/home/$USER/programmes/uplink cp {file}"

    os.system(cmd)
    print("put inside hte bucket ")


    response = requests.request("POST", url, headers=headers, data=file)

    res = response.json()
    print(res)

    return {
        "body": res
    }
