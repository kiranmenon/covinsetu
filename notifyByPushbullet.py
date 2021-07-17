import requests
from requests.exceptions import HTTPError
import json

"""pushbulletConfigDict = {}
        for channels in globals.app.ConfigData["notificationChannels"]:
            if "pushbullet" == channels["type"] and channels["enabled"] == "true" :
                """


class NotifyByPushbullet:
    url = "https://api.pushbullet.com/v2/pushes"
    def __init__(self, token):
        self.payloadDict = {"type": "note"}        
        self.headers = {
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json',
            'User-Agent': "com.qlabs.http.client",
            "Content-Type": "application/json"
            }
    
    def notify(self, title, body):
        self.payloadDict["title"] = title
        self.payloadDict["body"] = body

        try:
            resp = requests.request("POST", url=self.url, headers=self.headers, data=json.dumps(self.payloadDict))
            resp.raise_for_status()
        except HTTPError as http_err:
            print("HTTP error occured. {0}".format(http_err))
        except Exception as err:
            print("Unknown error. {0}".format(err))
        else:
            print("Pushbullet response OK.")  


        
        
        