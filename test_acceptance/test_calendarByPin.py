from apiclient import calendarByPin
import unittest

class TestCalendarByPin(unittest.TestCase):
    def test_acceptance_basic(self):
        resource = calendarByPin.CalendarByPin()
        resource.exec()

if __name__ == '__main__':
    unittest.main()       