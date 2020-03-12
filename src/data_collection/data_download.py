import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import os
from dotenv import load_dotenv

# get AT dev API key using the .env file
load_dotenv()
API_KEY = os.getenv('AT_API_KEY')

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': API_KEY,
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.at.govt.nz')
    conn.request("GET", "/v2/gtfs/stops?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

# decode the response from bytes to json
data = json.loads(data.decode("utf-8"))

# save the json to file
with open('data/json/stops.json', 'w', encoding = 'utf-8') as f:
    json.dump(data, f, indent = 2)
