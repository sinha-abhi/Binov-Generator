import json
import requests

base_url="https://random-word-api.herokuapp.com/word?"
api_key="D10Q0E04"
number="1"

url = base_url + "key=" + api_key + "&number=" + number

r= requests.get(url)
response = r.json()

print(response[0] + "binov")
