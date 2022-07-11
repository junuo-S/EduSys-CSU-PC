import datetime
import uuid
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QWidget
from src.MyRepeatWindow import MyRepeatWindow
from src.class_Stu import class_Stu
from src.class_Tea import class_Tea


class MyEveryClass():
    def __init__(self):
        self.term = self.checkTerm()
        self.stu = class_Stu(self.term)
        self.teac = class_Tea(self.term)
        self.repeatWindow = MyRepeatWindow()
        self.idNum = ''
        self.userName = ''

    def checkTerm(self) -> str:
        today = datetime.date.today()
        if 2 <= today.month < 9:
            term = f'{today.year - 1}-{today.year}-2'
        elif 1<=today.month<2:
            term = f'{today.year-1}-{today.year}-1'
        else:
            term = f'{today.year}-{today.year + 1}-1'
        return term

    def makeParam(self, user:tuple, term:str) -> dict:
        param={}
        if user[0]==0:
            param = {'type': 'xs0101',
                     'xnxq01id': term,
                     'xs0101id': user[2],
                     'xs': user[1]}
        elif user[0]==1:
            param = {'type': 'jg0101',
                    'xnxq01id': term,
                    'teacherID': user[1],
                    'jg0101id': user[5]}
        return param

    def search(self, term, keyWord):
        userList = self.stu.findallStu(keyWord) + self.teac.findallTea(keyWord)
        if len(userList) == 0:
            return None
        # print(userList)
        if len(userList) == 1:
            # print(list(userList[0].keys())[0])
            user = userList[0]
            param = self.makeParam(user, term)
        else:
            self.repeatWindow.load_display(userList)
            choice = self.repeatWindow.getRow()
            user = userList[choice]
            param = self.makeParam(user, term)
        title=''
        self.idNum = user[2]
        self.userName = user[1]
        infoString = f'姓名：{self.userName}\n学院：{user[3]}'
        macAddrs = ('3c:2c:30:fa:03:5f', '8c:ec:db:28:6a:7c')
        if user[0] == 0:
            infoString += f'\n专业班级：{user[4]}'
            if self.get_mac_address() in macAddrs:
                infoString += f'\n学号：{self.idNum}'
            title = '学生信息'
        elif user[0] == 1:
            if self.get_mac_address() in macAddrs:
                infoString += f'\n教工号：{self.idNum}'
            title = '教工信息'

        tempWidget = QWidget()
        tempWidget.setWindowIcon(QIcon(":/:/Image/中南大学校徽.jpg"))
        QMessageBox.about(tempWidget, title, infoString)
        if param != {}:
            return self.downloadData(param)

    def downloadData(self, param):
        if param['type'] == 'xs0101':
            return self.stu.downloadData(param)
        elif param['type'] == 'jg0101':
            return self.teac.downloadData(param)

    def get_mac_address(self):
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

    def getNames(self) -> set:
        names = self.stu.getStuNames() | self.teac.getNames()
        return names