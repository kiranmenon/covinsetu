import requests
from apiclient.headers import MyHeaders as myHeader

url = myHeader.calendarByCenterURL
params = {
    "center_id" : "710088",
    "date" : "10-07-2021"
}


response = requests.request("GET", url, headers=myHeader.headers, params=params)

print(response.text)
