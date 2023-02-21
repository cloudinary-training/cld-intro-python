import json
# read from .env file
from dotenv import load_dotenv
load_dotenv()

# import cloudinary
from cloudinary import api, config
from cloudinary.utils import cloudinary_url

# get reference to config instance
config = config(secure=True)
print(config.cloud_name)
print(config.api_key)

# Create a named transformation called "small_profile_thumbnail"
create_named = api.create_transformation("small_profile_thumbnail",
  dict(width = 150, height = 150, crop = "thumb", gravity = "auto"))
print(json.dumps(create_named, indent=2))

# Apply named transformation to an image
url, options = cloudinary_url("cld-sample", transformation=["small_profile_thumbnail"])
print("**** Apply Named Transformation to an image ****\nTransformation URL --> " + url, "\n")