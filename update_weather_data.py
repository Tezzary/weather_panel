import requests
import json
import time

url = "https://api.bom.gov.au/apikey/v1/observations/latest/86338/atm/surf_air?include_qc_results=false"

sleep_time = 5 * 60

while True:
    try:
        response = requests.get(url, headers = {'User-agent': 'Mozilla/5.0'})

        with open("static/weatherInformation.json", "w") as f:
            json.dump(response.json(), f, indent=2)

    except Exception as e:
        print(e)
    
    time.sleep(sleep_time)
