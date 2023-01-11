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

# Log the configuration
# ==============================
print("**** Set up and configure the SDK:****\n",
      config.cloud_name, config.api_key, "\n")


# Auto format, Auto quality, Auto Gravity - Cloudinary's special sauce
url, options = cloudinary_url(
    "llama",
    width=500,
    crop="scale",
    gravity="auto",
)
print("**** Auto Format, Auto Quality, Auto Gravity - Both ****\nTransformation URL --> " + url, "\n")
