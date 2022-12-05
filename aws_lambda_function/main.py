from __future__ import unicode_literals

import json
import os
from yt_dlp import YoutubeDL
import boto3
import requests

s3 = boto3.client('s3')


def lambda_handler(event, context):
    print(event)
    bucket = 'rekognite'

    if (event['rawPath'] == "/get"):

        URLS = 'https://www.youtube.com/watch?v=ALZHF5UqnU4'
        VIDEO_ID = URLS[-11:]
        print(VIDEO_ID)

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

        s3.put_object(Bucket=bucket, Key=new_song, Body=file)
        print("put inside hte bucket ")

        url = "https://api.nft.storage/upload"
        headers = {
            "Content-Type": "*/*",
            "accept": "application/json",
            "Authorization": f"Bearer {os.getenv('NFT_STORAGE')}"
        }

        with open(f"{song_filename}", 'rb') as f:
            file = f.read()

        response = requests.request("POST", url, headers=headers, data=file)

        res = response.json()
        print(res)

        return {
            "body": res
        }

    return {"nothing": "isfound"}