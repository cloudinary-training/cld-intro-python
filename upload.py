# read from .env file
import json
from dotenv import load_dotenv
load_dotenv()

import cloudinary
from cloudinary import uploader

# get reference to config instance
config = cloudinary.config(secure=True)
print(config.cloud_name)
print(config.api_key)

# Basic Upload Method
# basic_upload = uploader.upload("./assets/llama.jpg")
# print("**** Basic upload ****\nDelivery URL: ", json.dumps(basic_upload,indent=2), "\n")

 
# # Upload Source Options 

# #HTTP or HTTPS URL - Wikimedia
# https = uploader.upload("https://upload.wikimedia.org/wikipedia/commons/9/99/Capivara%28Hydrochoerus_hydrochaeris%29.jpg")
# print("**** Wikimedia ****\nDelivery URL: ", json.dumps(https,indent=2), "\n")

# # #Base64 Data URI
# base64 = uploader.upload("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII=")
# print("**** Base 64 Data URI ****\nDelivery URL: ", json.dumps(base64,indent=2), "\n")

# #Private Storage URL - Amazon S3 or Google Cloud Storage - we have not set up an S3 bucket to demo this,
# but wanted to show the format to show it's possible to use these remote sources
# s3 = uploader.upload("s3://my-bucket/my-path/example.jpg")
# print("**** Amazon S3 ****\nDelivery URL: ", json.dumps(s3,indent=2), "\n")

# #FTP URL - we have not set up an FTP server to demo this,
# but wanted to show the format to show it's possible to use these remote sources
# ftp = uploader.upload("ftp:user1:mypass@ftp.example.com/sample.jpg")
# print("**** FTP URL ****\nDelivery URL: ", json.dumps(ftp,indent=2), "\n")


 
# # Resource Type
# resource_vid = uploader.upload("assets/glacier.mp4", resource_type = "video")
# print("**** Resource Type: video ****\nDelivery URL: ", json.dumps(resource_vid,indent=2), "\n")

# resource_auto = uploader.upload("assets/glacier.mp4", resource_type = "auto")
# print("**** Resource Type: auto ****\nDelivery URL: ", json.dumps(resource_auto,indent=2), "\n")

# resource_JSON = uploader.upload("assets/south-america.json", resource_type = "auto")
# print("**** Resource Type: raw ****\nDelivery URL: ", json.dumps(resource_JSON,indent=2), "\n")

# resource_raw = uploader.upload("assets/y2k_bug.ttf", resource_type = "raw")
# print("**** Resource Type: raw ****\nDelivery URL: ", json.dumps(resource_raw,indent=2), "\n")


# # Public ID - Naming Options

#default
# default_public_id = uploader.upload("assets/puma.jpg")
# print("**** Default - 20 random character Public ID - if nothing is specified upon upload ****\nDelivery URL: ", json.dumps(default_public_id,indent=2), "\n")


# # use filename as public ID, don't attempt to make unique
# file_name_not_unique = uploader.upload("assets/puma.jpg", 
#   use_filename = True, 
#   unique_filename = False)
# print("**** Use Filename as Public ID, don't make unique ****\nDelivery URL: ", json.dumps(file_name_not_unique,indent=2), "\n")

# # use filename as public ID, DO add randomized characters at the end to make public ID unique
# file_name_unique = uploader.upload("assets/puma.jpg", 
#   use_filename = True, 
#   unique_filename = True)
# print("**** Use Filename as Public ID, unique ****\nDelivery URL: ", json.dumps(file_name_unique,indent=2), "\n")

# # determine your own public ID
# specify_public_id = uploader.upload("assets/anteater.jpg", 
#   public_id = "i-love-ants")
# print("**** Determine Your Own Public ID ****\nDelivery URL: ", json.dumps(specify_public_ID,indent=2), "\n")


# # Foldering
# create_folder_by_public_ID = uploader.upload("assets/iguana.jpg", 
#   public_id = "galapagos/iguana")
# print("**** Create Folder called galapagos, and upload image to that folder with public ID of iguana within Public ID Parameter ****\nDelivery URL: ", json.dumps(create_folder_by_public_ID,indent=2), "\n")

# folder_within_folder = uploader.upload("assets/puma.jpg", 
#   use_filename = True, 
#   unique_filename = False,
#   folder = "argentina/animals")
# print("**** Create Folder called argentina, with a subfolder called animals inside it, and upload image to that folder without a specified public ID ****\nDelivery URL: ", json.dumps(folder_within_folder,indent=2), "\n")


