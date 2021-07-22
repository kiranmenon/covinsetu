import globals

class ParseCenters:
    @staticmethod
    def parseCenters(centersDict):
        textList = []
        try:
            for center in centersDict["centers"]:
                textList.append(ParseCenters.parseCenter(center))
        except KeyError as e:
            # print("Key not found." + str(e)) 
            pass
        return textList
    
    @staticmethod
    def parseCenter(centerDict):                
        try:
            for session in centerDict["sessions"]:
                if int(session["available_capacity"]) > 0 or int(session["available_capacity_dose1"]) > 0 \
                    or int(session["available_capacity_dose2"]) > 0:
                    text = "Center : {3}, session date: {0}, Available: {1}, Dose1: {2}, Dose2: {4} ".format(session["date"], \
                        session["available_capacity"], session["available_capacity_dose1"], centerDict["name"], session["available_capacity_dose1"])
                else:
                    if globals.app.ConfigData["NotifyEvenIfNone"] == "true" :
                        text = "No slots in center: {0} for session {1}".format(centerDict["name"], session["date"])     
                    else:
                        text = None           
        except KeyError as e:
            # print("Key not found in JSON." + str(e))
            pass
        else:
            return text