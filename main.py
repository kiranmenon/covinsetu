from apiclient import calendarByPin

class Tasks:
    @staticmethod
    def do_calendarByPin():
            resource = calendarByPin.CalendarByPin()
            resource.exec()

if __name__ == "__main__":
    Tasks.do_calendarByPin()
    
    