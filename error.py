import json
from logging import NOTSET, lastResort
# read from .env file
from dotenv import load_dotenv
load_dotenv()

import cloudinary
from cloudinary.utils import cloudinary_url

# get reference to config instance, return "https" URLs by setting secure=True
config = cloudinary.config(secure=True)
print(config.cloud_name)
print(config.api_key)

# Showing error of gravity with scale - for demo purposes
url, options = cloudinary_url(
    "llama",
    width=500,
    crop="scale",
    gravity="auto",
)
print("**** Demonstrating Error ****\nTransformation URL --> " + url, "\n")
