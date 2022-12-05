import requests

name = "DVRST - My Toy-CqGOwGQtCFk.m4a".replace(" ",'+')

URL = f"https://rekognite.s3.us-east-2.amazonaws.com/{name}"
response = requests.get(URL)



open("tmp/"+name, "wb").write(response.content)
