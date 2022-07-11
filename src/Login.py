# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QWidget, QMessageBox, QCompleter
from src.ui.LoginWindow import Ui_LoginWindow
import base64
from PyQt5.QtCore import pyqtSignal, Qt, QStringListModel, pyqtSlot
from PyQt5.QtGui import QCloseEvent
import requests
import re
import ddddocr
import os


class MyLogin(QWidget, Ui_LoginWindow):
    readyLogin=pyqtSignal(requests.sessions.Session, str, requests.models.Response, str)
    def __init__(self):
        super(MyLogin, self).__init__()
        self.setupUi(self)
        self.userEdit.returnPressed.connect(self.enterPressed)
        self.pwdEdit.returnPressed.connect(self.enterPressed)
        lines=[]
        try:
            with open('users.ini', 'r') as file:
                lines=file.readlines()
        except:
            file = open('users.ini', 'w')
            file.close()
        self.users={}
        for line in lines:
            line=line.strip('\n')
            temp=line.split(' ')
            decodeUser=base64.b64decode(temp[0].encode()).decode()
            decodePwd=base64.b64decode(temp[1].encode()).decode()
            self.users[decodeUser]=decodePwd
        # http://csujwc.its.csu.edu.cn/jsxsd/xk/LoginToXk
        self.loginUrl = 'http://csujwc.its.csu.edu.cn/jsxsd/xk/LoginToXk'
        self.randCodeUrl = 'http://csujwc.its.csu.edu.cn/jsxsd/verifycode.servlet'
        completer=QCompleter()
        completer.setFilterMode(Qt.MatchContains)
        model=QStringListModel(self.users.keys())
        completer.setModel(model)
        self.userEdit.setCompleter(completer)

    def on_userEdit_changed(self,text):
        if text in self.users.keys():
            self.pwdEdit.setText(self.users[text])

    def on_Login_Clicked(self):
        user=self.userEdit.text()
        pwd=self.pwdEdit.text()
        if pwd == '' or user == '':
            QMessageBox.about(self, "用户登录", "用户名或密码不能为空")
            return
        encoded = base64.b64encode(user.encode()).decode() + \
                  '%%%' + base64.b64encode(pwd.encode()).decode()
        if user in self.users.keys():
            if self.users[user]!=pwd:
                self.users[user]=pwd
        else:
            self.users[user]=pwd
        paramPost = {'encoded': encoded}
        session=requests.session()
        session.get(self.loginUrl)
        captcha = session.get(self.randCodeUrl)
        ocr = ddddocr.DdddOcr(show_ad=False)
        res = ocr.classification(captcha.content)
        captcha.close()
        paramPost['RANDOMCODE'] = res
        resp = session.post(self.loginUrl, data=paramPost)
        if '用户名或密码错误' in resp.text:
            QMessageBox.about(self,"用户登录","用户名或密码错误")
            self.pwdEdit.clear()
            resp.close()
            session.close()
            return None
        objUser = re.compile('<font size="4">(?P<userName>.*?)</font><br />')
        name = objUser.findall(resp.text)
        if self.checkRemember.isChecked():
            if list(self.users.keys())!=[]:
                with open('users.ini', 'w') as file:
                    for key,value in self.users.items():
                        encodeKey=base64.b64encode(key.encode()).decode()
                        encodeValue=base64.b64encode(value.encode()).decode()
                        file.write(f'{encodeKey} {encodeValue}\n')
        try:
            QMessageBox.about(self,"登录成功",f"欢迎{name[0]}登录")
        except:
            # print(resp.text)
            QMessageBox.about(self,"登录失败",f"登录失败，请重试！")
            pass
        self.readyLogin.emit(session, name[0], resp, user)
        resp.close()
        return session

    def on_Cancel_Clicked(self):
        self.close()

    @pyqtSlot()
    def on_buttonClear_clicked(self):
        file = open('users.ini', 'w')
        file.close()
        self.users={}
        completer = QCompleter()
        completer.setFilterMode(Qt.MatchContains)
        model = QStringListModel(self.users.keys())
        completer.setModel(model)
        self.userEdit.setCompleter(completer)
        QMessageBox.about(self,'清空记录','记录已清空')

    def closeEvent(self, a0: QCloseEvent) -> None:
        sys.exit()

    def enterPressed(self):
        self.on_Login_Clicked()