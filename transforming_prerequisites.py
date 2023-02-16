import json
# read from .env file
from dotenv import load_dotenv
load_dotenv()

from cloudinary import uploader

uploader.upload("./assets/anteater.jpg", public_id= "anteater")
print("✓ anteater")
    
uploader.upload("./assets/puma.jpg", public_id= "puma")
print("✓ puma")

uploader.upload("./assets/cld-training-logo.png", public_id= "cld-training-logo")
print("✓ cloudinary training logo")

uploader.upload("./assets/llama.jpg", public_id= "llama")
print("✓ llama")

uploader.upload("./assets/sealion.jpg", public_id= "sealion")
print("✓ sealion")
    
uploader.upload("./assets/glacier.mp4", public_id= "glacier", resource_type = "video")
print("✓ glacier")
    
uploader.upload("./assets/iguana.jpg", public_id= "iguana")
print("✓ iguana")
    
uploader.upload("./assets/y2kbug.ttf", public_id= "y2kbug", resource_type = "raw")
print("✓ y2k bug font")
    
uploader.upload("./assets/cld-sample.jpg", public_id= "cld-sample")
print("✓ cld-sample")

uploader.upload("./assets/tortoise.mp4", public_id= "tortoise", resource_type="video")
print("✓ tortoise")

uploader.upload("./assets/south-america.json", public_id= "south-america", resource_type="raw")
print("✓ south america")

uploader.upload('https://res.cloudinary.com/cloudinary-training/image/upload/logo-big.png')
print("✓ cloudinary logo")
