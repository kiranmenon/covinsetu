import requests
from apiclient.headers import MyHeaders as myHeader
import globals 
import datetime
from requests.exceptions import HTTPError
import notifyByPushbullet
from notifyInStdOut import NotifyInStdOut
from apiclient.parseResponses import ParseCenters

class CalendarByCenter:
    def __init__(self):
        self.url = myHeader.calendarByCenterURL
        self.centers = globals.app.ConfigData["calendarByCenter"]["centers"]
        super().__init__()
    def exec(self):
        for center in self.centers:
            params = {
                "center_id" : center,
                "date": datetime.date.today().strftime("%d-%m-%y")
            }        

            try:
                response = requests.request("GET", self.url, headers=myHeader.headers, params=params)
                response.raise_for_status()
            except HTTPError as e:
                print("HTTP error occured." + str(e))
            except Exception as e:
                print("Unknown error." + str(e))
            else:
                print(response.text)
                replyJson = response.json()
                try:
                    text = ParseCenters.parseCenter(replyJson["centers"])
                except KeyError as e:
                    print("Key not found." + str(e)) 
                else:
                    for channel in globals.app.ConfigData["notificationChannels"]:
                        if channel["type"] == "pushbullet":
                            if channel["enable"] == "true":
                                token = channel["options"]["token"]
                                pbClient = notifyByPushbullet.NotifyByPushbullet(token)
                                pbClient.notify("COWIN alert for calendar by center " + params["center_id"], text)
                        elif channel["type"] == "stdout":
                            if channel["enable"] == "true":
                                NotifyInStdOut.notify(text)                

