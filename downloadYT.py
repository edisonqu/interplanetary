import shutil
from yt_dlp import YoutubeDL
import json
import os


URLS = 'https://www.youtube.com/watch?v=4nfveWsiThM'
VIDEO_ID = URLS[-11:]
print(VIDEO_ID)

ydl_opts = {    'format': 'm4a/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]}



with YoutubeDL(ydl_opts) as ydl:


    info = ydl.extract_info(URLS, download=True)
    metadata = json.loads(json.dumps(ydl.sanitize_info(info)))

    res = []
    for root, dir, files in os.walk("./"):
        for file in files:
            if file.endswith(".m4a"):
                res.append(os.path.join(root, file))

    shutil.move(res[0],"audio")

    print(metadata)


