import json

from dotenv import load_dotenv
load_dotenv()

from cloudinary import uploader, config

# get reference to config instance
config = config(secure=True)
print(config.cloud_name)
print(config.api_key)

# DOCS: https://cloudinary.com/documentation/backups_and_version_management

# Upload and ensure asset is backed up
backup = uploader.upload("assets/sealion.jpg", 
  public_id="sealion0",
  overwrite="True",
  backup = True)

print("**** Upload and ensure asset is backed up ****\n Response:\n", json.dumps(backup,indent=2), "\n")

