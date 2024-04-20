import requests

HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
# Retrieve these from https://htmlcsstoimage.com/dashboard
HCTI_API_USER_ID = '2ac8ecb4-29c3-4f46-ae16-f0864180cca8'
HCTI_API_KEY = '7fd24cdb-4544-4bae-890d-47a2f49fb141'

data = {
    'url': "www.hellenicbank.com",
    "ms_delay": 500
}

image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

print("Your image URL is: %s"%image.json()['url'])
# https://hcti.io/v1/image/7ed741b8-f012-431e-8282-7eedb9910b32
