from __future__ import unicode_literals

import json
import os
from yt_dlp import YoutubeDL
import boto3

s3 = boto3.client('s3')


def lambda_handler(event, context):
    print(event)
    bucket = 'rekognite'

    if (event['rawPath'] == "/get"):

        URLS = 'https://www.youtube.com/watch?v=EOFA9kPQ_uU&'
        VIDEO_ID = URLS[-11:]

        ydl_opts = {'format': 'm4a/bestaudio/best', 'outtmpl': '/tmp/%(title)s-%(id)s.%(ext)s',
                    'ffmpeg_location': '/opt/ffmpeg',
                    'postprocessors': [{  # Extract audio using ffmpeg
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                    }]}

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

        song_new_name = song_filename.lstrip("/tmp/")

        s3.put_object(Bucket=bucket, Key=song_new_name, Body=file)
        print("put inside hte bucket ")

        return {
            "body": "Success!"
        }

    return {"nothing": "isfound"}