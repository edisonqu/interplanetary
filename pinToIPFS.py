import os

import requests
import dotenv
import json

dotenv.load_dotenv()

url = "https://api.nft.storage/upload"
headers = {
    "Content-Type": "*/*",
    "accept":"application/json",
    "Authorization":f"Bearer {os.getenv('YOUR_STORAGE_API_KEY')}"
}


# files = [
#     ('file',("joji die for you but it's 2_23am [4nfveWsiThM].m4a",open("audio/joji die for you but it's 2_23am [4nfveWsiThM].m4a",'rb'),'application/octet-stream'))
# ]
with open("audio/joji die for you but it's 2_23am [4nfveWsiThM].m4a", 'rb') as f:
    file = f.read()

response = requests.request("POST",url,headers=headers,data=file)

print(response.json())