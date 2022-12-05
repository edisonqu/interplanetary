# import requests
#
# name = "DVRST - My Toy-CqGOwGQtCFk.m4a".replace(" ",'+')
#
# URL = f"https://rekognite.s3.us-east-2.amazonaws.com/{name}"
# response = requests.get(URL)
#
#
#
# open("tmp/"+name, "wb").write(response.content)

from s3fs import *
import os
import dotenv
import pandas as pd
import numpy as np
import boto3
from botocore.config import Config


dotenv.load_dotenv()
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





bucket = "mybucket"
key = "song.mp3"

# Creating a random dataframe.
df = pd.DataFrame(np.random.uniform(0,1,[10**3,3]), columns=list('ABC'))

# Saving as CSV


df.to_csv(
  f"s3://{bucket}/{key}",
  index=False,
  storage_options=storage_options)


# new_df = pd.read_csv(
#   f"s3://{bucket}/{key}",
#   storage_options=storage_options)
#
# print(new_df)

