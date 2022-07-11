class MyDateTime:
    def __init__(self, year, month, day, hour, minute, sec):
        self.daysDic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = sec
        self.setdaysDic()

    def setdaysDic(self):
        if (self.year % 100 != 0 and self.year % 4 == 0) or (self.year % 100 == 0):
            self.daysDic[2] = 29
        else:
            return

    def __sub__(self, aheadMin):
        h = minu = 0
        if self.minute >= aheadMin:
            minu = self.minute - aheadMin
        elif self.minute < aheadMin:
            h = self.hour - 1
            minu = self.minute + 60 - aheadMin
        return MyDateTime(self.year, self.month, self.day, h, minu, self.second)

    def __add__(self, addDay):
        y = self.year
        m = self.month
        d = self.day
        temp = self.day + addDay
        if temp > self.daysDic[self.month]:
            d = temp - self.daysDic[self.month]
            m = self.month + 1
            if m > 12:
                m = self.month - 12
                y = self.year + 1
        else:
            d = temp
        return MyDateTime(y, m, d, self.hour, self.minute, self.second)

    def toString(self):
        theString = str(self.year) + str(self.month).zfill(2) + str(self.day).zfill(2) + 'T' + \
                    str(self.hour).zfill(2) + str(self.minute).zfill(2) + str(self.second).zfill(2)
        return theString


class MyAlarm:
    def __init__(self, dateTime):
        self.ACTION = 'DISPLAY'
        self.TRIGGER = f';VALUE=DATE-TIME:{dateTime.toString()}'

    def toString(self):
        theString = 'BEGIN:VALARM\n' + f'ACTION:{self.ACTION}\n' + \
                    f'TRIGGER{self.TRIGGER}\n' + 'END:VALARM\n'
        return theString


class MyEvent:
    def __init__(self, SUMMARY, DTSTART, DTEND, UID, DESCRIPTION, LOCATION, ALARM):
        self.STATUS = 'CONFIRMED'
        self.SUMMARY = SUMMARY  # 字符串类型
        self.DTSTART = DTSTART  # MyDateTime类型
        self.DTEND = DTEND  # MyDateTime类型
        self.UID = UID  # 字符串类型
        self.DESCRIPTION = DESCRIPTION  # 字符串类型
        self.LOCATION = LOCATION  # 字符串类型
        self.ALARM = ALARM

    def toString(self):
        theString = 'BEGIN:VEVENT\n' + f'SUMMARY:{self.SUMMARY}\n' + \
                    f'DTSTART;TZID=Asia/Shanghai:{self.DTSTART.toString()}\n' + \
                    f'DTEND;TZID=Asia/Shanghai:{self.DTEND.toString()}\n' + \
                    f'UID:{self.UID}\n' + f'DESCRIPTION:{self.DESCRIPTION}\n' + \
                    f'LOCATION:{self.LOCATION}\n' + f'STATUS:{self.STATUS}\n' + \
                    self.ALARM.toString() + 'END:VEVENT\n'
        return theString


class MyIcalendar:
    def __init__(self, icalendarName='MyIcalendar'):
        self.eventDict = dict()
        self.begin = f"BEGIN:VCALENDAR\n" \
                     f"PRODID:-//ZHONG_BAI_REN//APPGENIX-SOFTWARE//\n" \
                     f"VERSION:2.0\n" \
                     f"CALSCALE:GREGORIAN\n" \
                     f"METHOD:PUBLISH\n" \
                     f"X-WR-CALNAME:{icalendarName}\n" \
                     f"X-WR-TIMEZONE:null\n"
        self.end = 'END:VCALENDAR\n'

    def removeEvent(self, UID):
        self.eventDict.pop(UID)

    def addEvent(self, event):
        if event.UID in self.eventDict.keys():
            print("已存在")
            return
        self.eventDict[event.UID] = event

    def toString(self):
        theString = self.begin
        for key, value in self.eventDict.items():
            theString += value.toString()
        theString += self.end
        return theString

    def saveAsICS(self, filename='Icalendar.ics'):
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(self.toString())
