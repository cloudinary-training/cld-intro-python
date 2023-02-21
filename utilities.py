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

# # To create only a URL
# url, options = cloudinary_url(
#     "anteater"
# )
# print("**** Return only the URL --> " + url, "\n")

# To create only a URL (video)
# url, options = cloudinary_url(
#     "tortoise",
#     resource_type = "video"
# )
# print("**** Return only the URL --> " + url, "\n")

# To create an image tag
# print(cloudinary.CloudinaryImage("puma").image())

# To create an video tag
print(cloudinary.CloudinaryVideo("tortoise").video())

# Build URL using build_url method (image)
# print(cloudinary.CloudinaryImage("puma").build_url()) 

# Build URL using build_url method (video)
# print(cloudinary.CloudinaryVideo("tortoise").build_url())