import json
# read from .env file
from dotenv import load_dotenv
load_dotenv()

import cloudinary
from cloudinary import uploader, api

from cloudinary.api import delete_resources_by_tag, resources_by_tag
from cloudinary.utils import cloudinary_url

# get reference to config instance
config = cloudinary.config(secure=True)
print(config.cloud_name)
print(config.api_key)


# DOCS: https://cloudinary.com/documentation/managing_assets

# List all assets
# list_all = api.resources()
# print(json.dumps(list_all, indent=2))
# print(json.dumps(len(list_all['resources'])))

# result = api.resources(max_results = 30)
# print(json.dumps(result, indent=2))
# print(json.dumps(len(result['resources'])))

# List all images with a given prefix - we are hoping to find the image of a llama that we previously uploaded
list_by_prefix = api.resources(
        type="upload",
        prefix="iguan")

print(json.dumps(list_by_prefix, indent=2))


# Rename an asset
# rename_asset = uploader.rename("sealion4", "sealion5")
# print(json.dumps(rename_asset, indent=2))

#Destroy with Upload API
# destroy = uploader.destroy("sample", invalidate = True)
# print(json.dumps(destroy, indent=2))

# Delete multiple with Admin API
# delete_multiple = api.delete_resources(["rnqhdhg1bkao8slxmney", "nrzichmiv8f2krw8s91n"])
# print(json.dumps(delete_multiple, indent=2))

#Upload and tag a single asset
# upload_and_tag = uploader.upload("assets/llama.jpg", tags = ["peru", "not an alpaca"])
# print(json.dumps(upload_and_tag, indent=2))

# Tag an existing asset
# tag_existing = uploader.add_tag(["galapagos", "ocean"], "owajuca2hssyorljfxvv")
# print(json.dumps(tag_existing, indent=2))

# Remove all tags from an asset
# remove_all_tags = uploader.remove_all_tags("owajuca2hssyorljfxvv")
# print(json.dumps(remove_all_tags, indent=2))

# Rename an asset and invalidate
# rename_and_invalidate = uploader.rename("sealion4", "sealion5", invalidate = True)
# print(json.dumps(rename_and_invalidate, indent=2))
