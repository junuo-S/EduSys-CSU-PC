from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIcon
import sys1
from src.Login import MyLogin
from src.EduSystem import MyEduSystem
from src.MyIntroduce import MyIntroduce


class MyEduManager:
    def __init__(self):
        self.loginWindow = MyLogin()
        self.eduSys = MyEduSystem()
        self.loginWindow.readyLogin.connect(self.dealReadyLogin)
        self.eduSys.exitLogin.connect(self.dealExitLogin)
        self.isFirst = True

    def dealReadyLogin(self, session, name, resp, user):
        self.eduSys.MyInit(session, name, resp, user)
        self.loginWindow.hide()
        self.eduSys.show()
        if self.isFirst:
            self.isFirst = False
            ui_Intro = MyIntroduce()
            ui_Intro.show()
            ui_Intro.exec_()

    def dealExitLogin(self):
        self.__init__()
        self.eduSys.hide()
        self.loginWindow.show()

    def Mymain(self):
        self.loginWindow.show()


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        manager = MyEduManager()
        manager.Mymain()
        sys.exit(app.exec_())
    except:
        tempWidget = QWidget()
        tempWidget.setWindowIcon(QIcon(":/:/Image/中南大学校徽.jpg"))
        QMessageBox.about(tempWidget, '错误', '这里出现了亿点点错误\n请联系开发者QQ：3236877923进行反馈')
        sys.exit(0)