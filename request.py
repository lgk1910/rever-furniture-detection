import requests
import string
import json
import re

BASE = "http://127.0.0.1:5000/"

input_urls = input("URLs (seperated by comma): ")

url_list = []
for i in re.split(",\s*", input_urls):
    url_list.append(i)

# print('URL list: ' + str(url_list))
try:
    res = requests.post(BASE + 'predict/', json={"urls":url_list})
    parsed_json_res = res.json()
    print(json.dumps(parsed_json_res, indent=4, sort_keys=True))
except:
    print("Failed to send request")
    
