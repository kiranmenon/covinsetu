import requests
from apiclient.headers import MyHeaders as myHeader
from requests.exceptions import HTTPError
import datetime
from notifyInStdOut import NotifyInStdOut
from notifyByPushbullet import NotifyByPushbullet
from apiclient.parseResponses import ParseCenters
import globals

class CalendarByPin:
    def __init__(self):
        self.url = myHeader.calendarByPinURL
        self.pincodes = globals.app.ConfigData["calendarByPin"]["pinCodes"]
        super().__init__()
    
    def exec(self):
        finalText = ""
        for pincode in self.pincodes:    
            params = {
                "pincode" : pincode,
                "date" : datetime.date.today().strftime("%d-%m-%y")
            }
            # print("Using qParams: pincode {0}, date {1}".format(params["pincode"], params["date"]))
            
            try:
                response = requests.request("GET", self.url, headers=myHeader.headers, params=params)
                response.raise_for_status()
            except HTTPError as http_err:
                print("HTTP error occured. {0}".format(http_err))
            except Exception as err:
                print("Unknown error. {0}".format(err))
            else:
            #     print(response.text)

                replyJson = response.json()
                textList = ParseCenters.parseCenters(replyJson)
                for text in textList:
                    if text is not None:
                        finalText += "\n" + text + "\n"
                   
        for channel in globals.app.ConfigData["notificationChannels"]:
            if channel["type"] == "pushbullet":  
                if channel["enable"] == "true":
                    token = channel["options"]["token"]                                
                    pushBulletApiClient = NotifyByPushbullet(token)    
                    if finalText != "" :                                                         
                        pushBulletApiClient.notify("COWIN alert calendar-by-pin", finalText)      
            elif channel["type"] == "stdout":
                if channel["enable"] == "true":
                    if finalText != "" :
                        NotifyInStdOut.notify("COWIN alert calendar-by-pin" + finalText)
    
                    
