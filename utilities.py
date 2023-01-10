import json
from logging import NOTSET, lastResort

from dotenv import load_dotenv
load_dotenv()

import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.api import delete_resources_by_tag, resources_by_tag
from cloudinary.utils import cloudinary_url

# get reference to config instance, return "https" URLs by setting secure=True
config = cloudinary.config(secure=True)
print(config.cloud_name)
print(config.api_key)

# Log the configuration
# ==============================
print("**** Set up and configure the SDK:****\n",
      config.cloud_name, config.api_key, "\n")

# To create only a URL
url, options = cloudinary_url(
    "anteater"
)
print("**** Return only the URL --> " + url, "\n")

# To create only a URL (video)
url, options = cloudinary_url(
    "tortoise.mp4",
    resource_type = "video"
)
print("**** Return only the URL --> " + url, "\n")


# To create an image tag
print(cloudinary.CloudinaryImage("puma").image())

# To create an video tag
print(cloudinary.CloudinaryVideo("tortoise").video())

# Build URL using build_url method (image)
print(cloudinary.CloudinaryImage("puma").build_url()) 

# Build URL using build_url method (video)
print(cloudinary.CloudinaryVideo("tortoise").build_url())

# run upload
# result = cloudinary.uploader.upload('https://res.cloudinary.com/jen-brissman/image/upload/puma')
# print upload response and secure URL
# print(json.dumps(result,indent=2))
# print (result['secure_url'])

# import utils to help with making transformations
# from cloudinary.utils import cloudinary_url
# create transformation url using public from git
# url, options = cloudinary_url(
#         result['public_id'],
#         width=500,
#         crop="scale"
#     )
# print(url)

# To return only the URL, standard Python command - cloudinary.utils.cloudinary_url
# print(cloudinary.utils.cloudinary_url(puma ,resource_type="image"))
# print(cloudinary.utils.cloudinary_url(
#     "tortoise", resource_type="video"))


# # direct url building
# cloudinary.CloudinaryImage("sample.jpg").build_url(
#   width = 100, height = 150, crop = 'fill')

