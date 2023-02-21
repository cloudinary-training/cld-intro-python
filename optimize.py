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

# DOCS: https://cloudinary.com/documentation/image_transformations

# Resize an asset
# url, options = cloudinary_url(
#     "llama",
#     width=500,
#     crop="scale"
# )
# print("****Resize: Transform to scale down, maintaining original aspect ratio****\nTransformation URL --> " + url, "\n")

# Crop an asset
# url, options = cloudinary_url(
#     "cld-sample",
#     height=800,
#     width=800,
#     crop="fill"
# )
# print("**** Crop an asset****\nTransformation URL --> " + url, "\n")

# Crop with gravity
# url, options = cloudinary_url(
#     "cld-sample",
#     width=800,
#     height=800,
#     crop="thumb",
#     gravity="auto"
# )
# print("**** Crop with Gravity ****\nTransformation URL --> " + url, "\n")

# Auto format
# url, options = cloudinary_url(
#     "sealion",
#     width=600,
#     height=800,
#     crop="fill",
#     fetch_format="auto"
# )
# print("**** Auto Format ****\nTransformation URL --> " + url, "\n")

# Auto quality
# url, options = cloudinary_url(
#     "sealion",
#     width=600,
#     height=800,
#     crop="fill",
#     quality="auto"
# )
# print("**** Auto Quality ****\nTransformation URL --> " + url, "\n")

# Auto format, Auto quality, Auto Gravity - Cloudinary's special sauce
url, options = cloudinary_url(
    "cld-sample",
    width=600,
    height=800,
    crop="fill",
    gravity="auto",
    fetch_format="auto",
    quality="auto",
)
print("**** Auto Format, Auto Quality, Auto Gravity - Both ****\nTransformation URL --> " + url, "\n")

# Rounding
# url, options = cloudinary_url(
#     "puma",
#     width=300,
#     height=300,
#     crop="thumb",
#     gravity="auto",
#     radius="max"
# )
# print("**** Rounding the corners of an asset with 1:1 aspect ratio****\nTransformation URL --> " + url, "\n")


# Borders
# url, options = cloudinary_url(
#     "iguana",
#     width=300,
#     height=300,
#     crop="fill",
#     gravity="auto",
#     border="10px_solid_green"
# )
# print("**** Adding a green border to an asset ****\nTransformation URL --> " + url, "\n")

# Auto background color
# url, options = cloudinary_url(
#     "llama",
#     width=400,
#     height=400,
#     crop="pad",
#     quality="auto",
#     background="auto"
# )
# print("**** Adding an automatic background color to a padded crop, based on one or more predominant colors in the asset****\nTransformation URL --> " + url, "\n")


# Color effect
# url, options = cloudinary_url(
#     "cld-sample",
#     height=300,
#     crop="scale",
#     quality="auto",
#     effect="tint:40:gold"
# )
# print("**** Add Color Effect ****\nTransformation URL --> " + url, "\n")

# Improve effect
# url, options = cloudinary_url(
#     "i-love-ants",
#     height=400,
#     crop="scale",
#     effect="improve:outdoor"
# )
# print("**** Improve effect for an outdoor asset ****\nTransformation URL --> " + url, "\n")

# Artistic filter
# url, options = cloudinary_url(
#     "puma",
#     height=400,
#     crop="scale",
#     effect="art:hairspray"
# )
# print("**** Add the artistic effect, hairspray ****\nTransformation URL --> " + url, "\n")

# Overlays - Text over image
# url, options = cloudinary_url("cld-sample",
#                               transformation=[
#                                   {'crop': 'fill', 'width': 500},
#                                   {'quality': 'auto'},
#                                   {'color': "#FFFFFF", 'overlay': {'font_family': "arial", 'font_size': 30, 'font_weight': "bold",
#                                                                    'text_decoration': "underline", 'letter_spacing': 3, 'text': "Dalmation!"}},
#                                   {'flags': "layer_apply",
#                                       'gravity': "north_east", 'y': 10, 'x': 10}
#                               ])
# print("**** Overlay - Transform to add text over image in the top right corner ****\nTransformation URL --> " + url, "\n")


# Overlays - Image over video
# url, options = cloudinary_url("tortoise", resource_type="video",
#                               transformation=[
#                                   {'crop': 'fill', 'width': 500},
#                                   {'overlay': 'cld-training-logo'},
#                                   {'flags': "layer_apply", 'gravity': "north_east", 'y': 10, 'x': 10, 'width':100, 'opacity':50},
#                                   {'quality': 'auto'}
#                               ])
# print("**** Overlay - Transform to add a Cloudinary logo overlay to the north east corner of an video ****\nTransformation URL --> " + url, "\n")
