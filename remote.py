# read from .env file
from dotenv import load_dotenv
load_dotenv()

from cloudinary.utils import cloudinary_url
from cloudinary import config
import json
# import cloudinary

# get reference to config instance, returns HTTPS
config = config(secure=True)
print(config.cloud_name)
print(config.api_key)

# DOCS: https://cloudinary.com/documentation/fetch_remote_images#remote_image_fetch_url
# To do a remote fetch, you will need to go to security, settings, and uncheck "fetched url"

# Fetching image
url, options = cloudinary_url(
    "https://upload.wikimedia.org/wikipedia/commons/1/18/Bradypus.jpg",
    type="fetch")
print("**** Fetching Remote image ****\nTransformation URL --> " + url, "\n")

# Fetching remote image, and making some transformations in the URL build
# url, options = cloudinary_url("https://upload.wikimedia.org/wikipedia/commons/0/02/Capybara.jpg",
#                 type="fetch",
#                 width=300,
#                 height=300,
#                 crop='fill',
#                 gravity="face",
#                 radius="max")
# print("**** Fetching Remote image ****\nTransformation URL --> " + url, "\n")

# Mapping a cloud folder remote-images to a path to images on the internet
# URL prefix: https://cloudinary-training.github.io/cld-advanced-concepts/assets/images/

# url, options = cloudinary_url(
#     "remote-images/dolphin.jpg", width="300", zoom="300", crop="thumb")
# print("**** Auto Upload - Lazy Migration ****\nTransformation URL --> " + url, "\n")
