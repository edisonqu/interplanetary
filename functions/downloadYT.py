from __future__ import unicode_literals

import shutil
from yt_dlp import YoutubeDL
import json
import os
from pinToIPFS import pinToIPFS

URLS = 'https://www.youtube.com/watch?v=NwUo8N7depg'
VIDEO_ID = URLS[-11:]
print(VIDEO_ID)

ydl_opts = {    'format': 'm4a/bestaudio/best', 'outtmpl': 'functions/tmp/%(title)s-%(id)s.%(ext)s',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]}

with YoutubeDL(ydl_opts) as ydl:
    print('%(title)s-%(id)s.%(ext)s')

    info = ydl.extract_info(URLS, download=True)
    metadata = json.loads(json.dumps(ydl.sanitize_info(info)))

    res = []
    for root, dir, files in os.walk("../"):
        for file in files:
            if file.endswith(".mp3"):
                res.append(os.path.join(root, file))

    song_filename = res[0]
    print(metadata)

    try:
        metadata_filename = f'metadeta_{metadata["title"]}.json'
        metadata_file = open(metadata_filename,'x')


        with open(metadata_filename, 'w') as f:
            json.dump(metadata,f,indent=4)


        # shutil.move(song_filename, "audio")
        shutil.move(metadata_filename, "song_metadata")
    except Exception:
        print(Exception.args)
        pass

    print("moved to the folder")

    # cid = pinToIPFS(song_filename)['value']['cid']
    # print("https://ipfs.io/ipfs/"+cid)
    # print(f"https://{cid}.ipfs.nftstorage.link/")


