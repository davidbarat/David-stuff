import json
import ssl
import requests
import base64


auth = ('user','passwd')
list_group = ['id']

for id_group in list_group:
    url = "https://api/v2/groups" + id_group + "/all_hosts/?page_size=1000"
    r = requests.get(url, auth=auth, verify=False)
    json_content = r.json()
    for item in json_content['results']:
        print(item['name'])
