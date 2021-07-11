import globals

class Headers:
    def __init__(self):
        self.headers = {
            'Authorization': 'Bearer ' + globals.app.ConfigData["apiToken"],
            'Accept': 'application/json',
            'Accept-Encoding': "gzip,deflate,br",
            'User-Agent': "com.qlabs.http.client"
        }
        self.getAllDistrictsURL = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/17"
        self.calendarByCenterURL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByCenter"
        self.calendarByPinURL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
        super().__init__()

MyHeaders = Headers()
