from apiclient import calendarByPin
from apiclient import calendarByCenter

class Tasks:
    @staticmethod
    def do_calendarByPin():
            resource = calendarByPin.CalendarByPin()
            resource.exec()
    
    @staticmethod
    def do_calendarByCenter():
        rsrc = calendarByCenter.CalendarByCenter()
        rsrc.exec()

if __name__ == "__main__":
    Tasks.do_calendarByPin()
    Tasks.do_calendarByCenter()

    
    