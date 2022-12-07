import pytube


async def get_thumbnail(URL):
    return pytube.YouTube(URL).thumbnail_url
async def get_artist(URL):
    return pytube.YouTube(URL).author
async def get_title(URL):
    return pytube.YouTube(URL).title
