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
# backup = uploader.upload("assets/sealion.jpg", 
#   public_id = "sealion00",
#   overwrite = True,
#   backup = True)

# print("**** Upload and ensure asset is backed up ****\n Response:\n", json.dumps(backup,indent=2), "\n")

# Example to show a restore when a mistake is made
mistake = uploader.upload("assets/puma.jpg", 
  public_id = "sealion00",
  overwrite = True,
  backup = True)

print("**** Upload another asset by mistake with the same public ID ****\n Response:\n", json.dumps(mistake,indent=2), "\n")
