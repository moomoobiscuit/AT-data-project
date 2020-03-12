import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import os, sys
from dotenv import load_dotenv

# import json_work module from the script directory
sys.path.insert(1, './script')
from json_work import save_json, json_to_csv

# get AT dev API key using the .env file
load_dotenv()
API_KEY = os.getenv('AT_API_KEY')

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': API_KEY,
}

# download static data from AT APIs
static_api_namelist = ['stops', 'trips', 'routes', 'calendar', 'agency']

for api_name in static_api_namelist:

    try:
        # connect to the API service
        conn = http.client.HTTPSConnection('api.at.govt.nz')

        # request specific API
        conn.request("GET", "/v2/gtfs/%s?" % api_name, "{body}", headers)

        # save response
        response = conn.getresponse()
        data = response.read()
        conn.close() # close connection
        
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # save the json to file
    save_json(data, 'data/json/{0}.json'.format(api_name))
    json_to_csv(
        'data/json/{0}.json'.format(api_name), 
        'data/csv/{0}.csv'.format(api_name)
    )
