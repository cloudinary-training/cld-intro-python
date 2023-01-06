# Introduction to Cloudinary Using Python

## Environment Setup

## Install Python3 and Pip

You will need to install Python on your machine, version 3.8 or higher.

Important - Installing Python will also install pip, the package manager for Python.

#### Mac

[Install Python3 and Pip3 on Mac Using Brew](https://docs.python-guide.org/starting/install3/osx/)

[Install Python on Mac - 3.11.0 is here!](https://www.python.org/downloads/)

#### Windows

[Install Python on Windows](https://docs.python.org/3/using/windows.html)

#### Mac Users
Using Homebrew:

```
brew install python3
```

#### Verify Python install

```bash
# verify versions
$ python3 --version
Python 3.10.8 #Python 3.8 or above is ideal!

$ pip3 --version
pip 22.3
```


### Choose an IDE or Use Text Editor

- [Visual Studio Code](https://code.visualstudio.com/download) (we use VSCode!)
- [WebStorm](https://www.jetbrains.com/webstorm/) 
- [Sublime](https://www.sublimetext.com/) 
- [Atom](https://atom.io/) 
- [iTerm](https://iterm2.com/) 

### Download Repository

[Introduction to Cloudinary for API Users and Python Developers](https://github.com/cloudinary-training/cld-intro-python)

- Assets are located in `/assets` directory
- Run code from root directory 


## Credentials

1. Create a free account on Cloudinary at [cloudinary.com/signup](https://www.cloudinary.com/signup)

2. Navigate to the [Dashboard](https://console.cloudinary.com/console/). Copy your `CLOUDINARY_URL` into your clipboard.

![Dashboard](/assets/env_variable.png)

- Key: CLOUDINARY_URL
- Value: cloudinary://API_KEY:API_SECRET@CLOUD_NAME


3. Create a `.env` file in the root of the project. Paste your CLOUDINARY_URL environment variable into your `.env` file. OR, you can use the `env.example` file we've created for you, which already exists in this repository. You can paste in your CLOUDINARY_URL where there is currently a placeholder for you which looks like this:

```bash
CLOUDINARY_URL=cloudinary://API_KEY:API_SECRET@CLOUD_NAME
```

### We store credentials in a .env file (or a .env.sample file!), but this isn't the only way.

[3 ways for credentials](https://www.realpythonproject.com/3-ways-to-store-and-read-credentials-locally-in-python/)


## Use Pip3 to Install Cloudinary and dotenv

Get the latest Pip

```
pip3 install --upgrade pip
```

### Install Cloudinary

```
pip3 install cloudinary
```

### Install dotenv

```
pip3 install python-dotenv 
```
In python script

```
from dotenv import load_dotenv
import os 

load_dotenv()
```

## Run Code: Test Credentials

Make sure to npm install the Python libraries. You will be using the `cloudinary` and the `dotenv` libraries.

```bash
python3 test_config.py
```
You should see your Cloud Name and API Key output in this format:

```bash
****Set up and configure the SDK:****
 cloud_name | api_key 
```
PS- Always keep your API_Secret private!


## Run Code

```
python3 upload.py
```

# Credits 

## assets/images  


anteater.jpg - [Photo by Sean P. Twomey from Pexels](https://www.pexels.com/photo/photo-of-giant-anteater-7561663/)

glacier.mp4 - [Photo by Jan Zakelj from Pexels](https://www.pexels.com/video/cold-glacier-iceberg-melting-9358281/)

iguana.jpg - [Photo by Simon Berger from Pexels](https://www.pexels.com/photo/orange-iguana-standing-on-rocks-1190690/)

puma.jpg - [Photo by Pixabay from Pexels](https://www.pexels.com/photo/nature-animal-wilderness-head-53001/)

llama.jpg - [Photo by Jen Brissman, Machu Picchu, Cusco, Peru](https://res.cloudinary.com/jen-brissman/image/upload/v1667611308/llama.jpg)

sealion.jpg - [Photo by Jen Brissman, San Cristobal Island, Galapagos](https://res.cloudinary.com/jen-brissman/image/upload/v1667611309/sealion.jpg)

tortoise.mp4 - [Photo by Jen Brissman, Santa Cruz Island, Galapagos](https://res.cloudinary.com/jen-brissman/video/upload/v1667611643/tortoise.mp4)

y2kbug.ttf - [Public TrueType Font File, Y2K Bug, from All-free-download.com](https://all-free-download.com/font/download/y2k_bug_6919020.html)