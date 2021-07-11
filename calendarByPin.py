import requests
from headers import MyHeaders as myHeader
from requests.exceptions import HTTPError
import datetime
from notifyInStdOut import NotifyInStdOut


class CalendarByPin:
    def __init__(self):
        self.url = myHeader.calendarByPinURL
        self.pincodes = ["680662", "680686", "680664", "680671", "680688", "680666", "680681", "680691"]
        super().__init__()
    
    def exec(self):
        for pincode in pincodes:    
            params = {
                "pincode" : pincode,
                "date" : datetime.date.today().strftime("%d-%m-%y")
            }
            # print("Using qParams: pincode {0}, date {1}".format(params["pincode"], params["date"]))
            
            try:
                response = requests.request("GET", url, headers=myHeader.headers, params=params)
                response.raise_for_status()
            except HTTPError as http_err:
                print("HTTP error occured. {1}".format(http_err))
            except Exception as err:
                print("Unknown error. {1}".format(err))
            # else:
            #     print(response.text)

            replyJson = response.json()
            for center in replyJson["centers"]:
                print(center["name"])
                for session in center["sessions"]:
                    text = "session date: {0}, Available: {1}, Dose1: {2} ".format(session["date"], session["available_capacity"], session["available_capacity_dose1"])
                    NotifyInStdOut.notify(text)
