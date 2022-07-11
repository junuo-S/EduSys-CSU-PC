import datetime


class MyDateTime:
    def __init__(self):
        self.date_ = datetime.date(1, 1, 1)
        self.time_ = datetime.time()

    def newOne(self):
        newone = MyDateTime()
        newone.date_ = self.date_
        newone.time_ = self.time_
        return newone

    def setDate(self, year, month, day):
        self.date_ = self.date_.replace(year, month, day)

    def setTime(self, hour, minute, second):
        self.time_ = datetime.time(hour, minute, second)

    def addDate(self, days=0):
        delta = datetime.timedelta(days=days)
        self.date_ += delta

    def toString(self):
        theString = self.date_.strftime("%Y%m%d") + 'T' + self.time_.strftime("%H%M%S")
        return theString


class MyAlarm:
    def __init__(self, aheadMin):
        self.ACTION = 'DISPLAY'
        self.TRIGGER = f';RELATED=START:-PT{aheadMin}M'

    def toString(self):
        theString = 'BEGIN:VALARM\n' + f'ACTION:{self.ACTION}\n' + \
                    f'TRIGGER{self.TRIGGER}\n' + 'END:VALARM\n'
        return theString


class MyEvent:
    def __init__(self, SUMMARY, DTSTART, DTEND, UID, DESCRIPTION, LOCATION, ALARM):
        self.SUMMARY = SUMMARY  # 字符串类型
        self.DTSTART = DTSTART.newOne()  # MyDateTime类型
        self.DTEND = DTEND.newOne()  # MyDateTime类型
        self.UID = UID  # 字符串类型
        self.DESCRIPTION = DESCRIPTION  # 字符串类型
        self.LOCATION = LOCATION  # 字符串类型
        self.ALARM = ALARM

    def toString(self):
        theString = 'BEGIN:VEVENT\n' + \
                    f'SUMMARY:{self.SUMMARY}\n' + \
                    f'DTSTART;TZID=Asia/Shanghai:{self.DTSTART.toString()}\n' + \
                    f'DTEND;TZID=Asia/Shanghai:{self.DTEND.toString()}\n' + \
                    f'UID:{self.UID}\n' + f'DESCRIPTION:{self.DESCRIPTION}\n' + \
                    f'LOCATION:{self.LOCATION}\n' + \
                    self.ALARM.toString() + 'END:VEVENT\n'
        return theString


class MyIcalendar:
    def __init__(self, icalendarName='MyIcalendar'):
        self.eventDict = dict()
        self.begin = f"BEGIN:VCALENDAR\n" \
                     f"PRODID:-//YZune//ZHENGYANGSchedule//EN\n" \
                     f"VERSION:2.0\n" \
                     f"X-WR-CALNAME:{icalendarName.rstrip('.ics')}\n"
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
        for value in self.eventDict.values():
            theString += value.toString()
        theString += self.end
        return theString

    def saveAsICS(self, filename='Icalendar.ics'):
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(self.toString())
