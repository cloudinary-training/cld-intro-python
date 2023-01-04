from dotenv import load_dotenv
load_dotenv() # reading variables from .env file

# load_dotenv() needs to be run before importing cloudinary
import cloudinary
config = cloudinary.config(secure=True)

# Log the configuration
print("**** Set up and configure the SDK:****\n",
      config.cloud_name, config.api_key, "\n")

