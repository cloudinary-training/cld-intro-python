import json
# read from .env file
from dotenv import load_dotenv
load_dotenv()

# import cloudinary
from cloudinary import config
from cloudinary.utils import cloudinary_url

# # get reference to config instance
# config = config(secure=True)
# # create a Cloudinary delivery URL using the CLOUDINARY_URL in the config / .env file.
# url, options = cloudinary_url("llama")
# print(url)

# Supply cloud_name explicitly in the config object, not using CLOUDINARY_URL in .env file, not requiring dotenv 
config.cloud_name="jen-brissman"
url, options = cloudinary_url("llama")
print(url)



