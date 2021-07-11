
class Headers:
    def __init__(self):
        self.headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJmYTAyNjY3NS1kOGE4LTQ2Y2UtOTE3OS01Y2VhN2I2MGVmMjEiLCJ1c2VyX3R5cGUiOiJCRU5FRklDSUFSWSIsInVzZXJfaWQiOiJmYTAyNjY3NS1kOGE4LTQ2Y2UtOTE3OS01Y2VhN2I2MGVmMjEiLCJtb2JpbGVfbnVtYmVyIjo5NDQ2Mzc5OTUwLCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjczNzc3NjAxMjg3MjcwLCJ0eG5JZCI6IjMxZjQ3YjdhLTJkZWYtNDI3MS1hMzliLWRjMjI3MmU5MzAxYiIsImlhdCI6MTYyNDg1NzUxOCwiZXhwIjoxNjI0ODU4NDE4fQ.krfL3tBmBPpOTkuCmgHyaVYT6uf57c_M0f2FqDV7Emc',
            'Accept': 'application/json',
            'Accept-Encoding': "gzip,deflate,br",
            'User-Agent': "com.qlabs.http.client"
        }
        self.getAllDistrictsURL = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/17"
        self.calendarByCenterURL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByCenter"
        self.calendarByPinURL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
        super().__init__()

MyHeaders = Headers()
