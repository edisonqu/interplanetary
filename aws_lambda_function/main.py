import json
import os
from yt_dlp import YoutubeDL


def lambda_handler(event, context):
    # TODO implement

    print(event)
    if (event['rawPath'] == "/get"):
        URLS = 'https://www.youtube.com/watch?v=EOFA9kPQ_uU&'
        VIDEO_ID = URLS[-11:]
        print(VIDEO_ID)

        ydl_opts = {'format': 'm4a/bestaudio/best',
                    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
                    'postprocessors': [{  # Extract audio using ffmpeg
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                    }]}

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(URLS, download=False)
            metadata = json.loads(json.dumps(ydl.sanitize_info(info)))

        return {
            'body': metadata
        }
    return {"nothing": "isfound"}