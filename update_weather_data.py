import requests
import json
#url = "https://api.bom.gov.au/apikey/v1/forecasts/daily/553/144?timezone=Australia/Melbourne"
#url = "https://api.bom.gov.au/apikey/v1/forecasts/texts?aac=VIC_PT042&timezone=Australia/Melbourne"
url = "https://api.bom.gov.au/apikey/v1/forecasts/1hourly/553/144?timezone=Australia/Melbourne"
uv_url = "https://api.bom.gov.au/apikey/v1/forecasts/texts?aac=VIC_PT042&timezone=Australia%2FMelbourne"
response = requests.get(url, headers = {'User-agent': 'Mozilla/5.0'})

print(response.text)

with open("dump.json", "w") as f:
    json.dump(response.json(), f, indent=2)
