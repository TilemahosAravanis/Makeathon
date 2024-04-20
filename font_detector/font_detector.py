import requests
import base64
import os

URL="https://www.whatfontis.com/api2/"


PARAMETERS ={
    "API_KEY": "3953afb6d46d59c7409187ea2b6e6e950b46bad9b0c16d7fe65f709db86c360d",
    "IMAGEBASE64": 1,
    "NOTTEXTBOXDETECTION": 0,
    "urlimagebase64": "",
    "limit": 10
}


cur_file_path = os.path.abspath(__file__)
work_dir = os.path.dirname(cur_file_path)
print(work_dir)


image = open(work_dir+"/cropped_images/test.png", "rb").read()
base64_encoded = base64.b64encode(image).decode('utf-8')

PARAMETERS["urlimagebase64"] = base64_encoded

# Send POST request and get response
response = requests.post(
    URL,
    data = PARAMETERS
)

response = response.json()

# Manipulate JSON file
for possible_font in response:
    print(possible_font["title"])