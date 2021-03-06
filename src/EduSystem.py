import sys
import threading

from src.ui.EduSystemWindow import Ui_eduSys
from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QMessageBox, QFileDialog
from PyQt5.QtWidgets import QCompleter, QPushButton, QComboBox
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtCore import Qt, pyqtSignal, QStringListModel
from bs4 import BeautifulSoup
import requests
import re
from src.calendar.MyCalendar_ICS import *
from src.threads.Init2Thread import Init2Thread
from src.threads.validThread import validThread
from src.threads.originThread import originThread
from src.MyEveryClass import MyEveryClass
from src.TeaEvaluation import Evaluation
import uuid
import datetime
from concurrent.futures import ThreadPoolExecutor


class MyEduSystem(QWidget, Ui_eduSys):
    tabChange = pyqtSignal(int)
    initial = pyqtSignal(requests.sessions.Session)
    exitLogin = pyqtSignal()
    askValid = pyqtSignal(requests.sessions.Session, dict)
    askOrigin = pyqtSignal(requests.sessions.Session, dict)

    def __init__(self):
        super(MyEduSystem, self).__init__()
        self.setupUi(self)
        self.init2Thread = Init2Thread()
        self.validThread = validThread()
        self.originThread = originThread()
        self.tableClass.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableTeaScore.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableTeaScore.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableEvalCose.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableEvalCose.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.initSignalConnectSlot()
        self.tableClass.setSpan(6, 0, 6, 7)
        self.session = requests.session()
        self.name = ''
        self.user = ''
        self.num = 0
        self.stack = 0
        self.classPage = 0
        self.isFirstTab = True
        self.TeaEval = Evaluation()
        self.isable = [1, 0, 0]
        self.tabWidget.setCurrentIndex(0)
        self.radioValid.setChecked(True)
        self.classStack.setCurrentIndex(0)
        self.everyClass = MyEveryClass()
        self.classTerm = list()
        macAddrs = ('3c:2c:30:fa:03:5f', '8c:ec:db:28:6a:7c')
        if self.get_mac_address() in macAddrs:
            self.prompt()

    def initSignalConnectSlot(self) -> None:
        self.askValid.connect(self.validThread.dealaskValid)
        self.askOrigin.connect(self.originThread.dealaskOrigin)
        self.initial.connect(self.init2Thread.recFromMain)
        self.tabChange.connect(self.dealTabChange)
        self.init2Thread.readyInitValid.connect(self.dealValid)
        self.init2Thread.readyInitRank.connect(self.dealRank)
        self.init2Thread.readyInitOrigin.connect(self.dealOrigin)
        self.tabWidget.currentChanged.connect(self.dealtabWidgetChange)
        self.tableClass.itemClicked.connect(self.showDetail)
        self.tableClass.itemChanged.connect(self.tableClass.resizeRowsToContents)
        self.keyEdit.returnPressed.connect(self.on_classSearch_released)

    def get_mac_address(self):
        mac = uuid.uuid1(uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

    #?????????????????????????????????????????????????????????
    def prompt(self) -> None:
        completer=QCompleter()
        completer.setFilterMode(Qt.MatchContains)
        model = QStringListModel(self.everyClass.getNames())
        completer.setModel(model)
        self.keyEdit.setCompleter(completer)

    def MyInitClass(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        terms = soup.find('select', onchange="getKbxx();")
        options = terms.find_all('option')
        for option in options:
            self.classTerm.append(option.text)
        self.searchTerm.addItems(self.classTerm)
        self.setSearchTerm()
        self.on_buttonFind_released()

    def setSearchTerm(self) -> None:
        term = self.getCurrentTerm()
        if term in self.classTerm:
            self.searchTerm.setCurrentText(term)

    def getCurrentTerm(self) -> str:
        today = datetime.date.today()
        year = today.year
        month = today.month
        if 2<=month<9:
            return f'{year - 1}-{year}-2'
        else:
            return f'{year}-{year + 1}-1'

    def dealReadyValid(self, validScores) -> None:
        self.tableValid.setRowCount(len(validScores))
        row = -1
        for score in validScores:
            row += 1
            column = -1
            for data in score:
                column += 1
                self.tableValid.setItem(row, column, QTableWidgetItem(data))
                self.tableValid.item(row, column).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        w = 275
        for i in range(self.tableValid.columnCount()):
            w += self.tableValid.columnWidth(i)
        self.resize(w, self.height())

    def dealReadyOrigin(self, originScores) -> None:
        self.tableOrigin.setRowCount(len(originScores))
        row = -1
        for score in originScores:
            row += 1
            column = -1
            for data in score:
                column += 1
                self.tableOrigin.setItem(row, column, QTableWidgetItem(data))
                self.tableOrigin.item(row, column).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        w = 275
        for i in range(self.tableOrigin.columnCount()):
            w += self.tableOrigin.columnWidth(i)
        self.resize(w, self.height())

    def dealValid(self, heads, options):
        self.combo1stTerm.blockSignals(True)
        self.tableValid.setColumnCount(len(heads))
        self.tableValid.setHorizontalHeaderLabels(heads)
        self.tableValid.itemChanged.connect(self.tableValid.resizeColumnsToContents)
        for option in options:
            self.combo1stTerm.addItem(option.text)
        self.validThread.readyValid.connect(self.dealReadyValid)
        self.combo1stTerm.blockSignals(False)

    def dealRank(self, heads, options):
        for option in options:
            self.combo2ndTerm.addItem(option)
        self.tableRank.setColumnCount(len(heads))
        self.tableRank.setHorizontalHeaderLabels(heads)
        self.tableRank.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def dealOrigin(self, heads, options):
        self.combo3rdTerm.blockSignals(True)
        self.tableOrigin.setColumnCount(len(heads))
        self.tableOrigin.setHorizontalHeaderLabels(heads)
        self.tableOrigin.itemChanged.connect(self.tableOrigin.resizeColumnsToContents)
        for option in options:
            self.combo3rdTerm.addItem(option)
        self.originThread.readyOrigin.connect(self.dealReadyOrigin)
        self.combo3rdTerm.blockSignals(False)

    def closeEvent(self, a0: QCloseEvent) -> None:
        if self.init2Thread.isRunning():
            self.init2Thread.quit()
            self.init2Thread.wait()
        if self.validThread.isRunning():
            self.validThread.quit()
            self.validThread.wait()
        if self.originThread.isRunning():
            self.originThread.quit()
            self.originThread.wait()
        a0.accept()
        sys.exit()

    def MyInit(self, session, name, resp, user):
        self.combo1stTerm.clear()
        self.combo2ndTerm.clear()
        self.combo3rdTerm.clear()
        self.radioValid.setChecked(True)
        self.tabChange.emit(0)
        self.session = session
        self.name = name
        self.user = user
        self.setWindowTitle(f'??????{name}?????????')
        self.MyInitClass(resp.text)
        resp.close()
        self.initial.emit(session)
        self.init2Thread.start()

    def display(self, classData):
        obj = re.compile(r'???????????????(?P<className>.*?)\n???????????????(?P<teacher>.*?)\n'
                         r'?????????(?P<allweek>.*?)\n?????????(?P<eachWeek>.*?)\n?????????(?P<time>.*?)\n'
                         r'???????????????(?P<location>.*?)\n')
        timeDic = {'???': 1, '???': 2, '???': 3, '???': 4, '???': 5, '???': 6, '???': 7}
        for each in classData:
            classIter = obj.finditer(each['title'])
            row = column = -1
            for it in classIter:
                temp = it['time'].rstrip('???')
                if len(temp) == 4:
                    temp = temp[2:]
                    row = int(temp) // 2 - 1
                elif len(temp) == 8:
                    row = []
                    tem = temp[:4][2:]
                    row.append(int(tem) // 2 - 1)
                    tem = temp[4:][2:]
                    row.append(int(tem) // 2 - 1)
                temp = it['eachWeek'][-1]
                column = timeDic[temp] - 1
                location=it['location']
                if location == '':
                    location = ' '
                try:
                    classString = it['className'] + '\n' + it['teacher'] + '\n' + it['allweek'] + '\n'
                    classString += it['eachWeek'] + '\n' + it['time'] + '\n' + location
                    if self.tableClass.item(row, column) == None:
                        current = ''
                    else:
                        current = '\n\n' + self.tableClass.item(row, column).text()
                    if current.lstrip('\n\n') != classString:
                        self.tableClass.setItem(row, column, QTableWidgetItem(classString + current))
                        self.tableClass.item(row, column).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                except:
                    pos = 0
                    for eachRow in row:
                        pos += 4
                        classString = it['className'] + '\n' + it['teacher'] + '\n' + it['allweek'] + '\n'
                        classString += it['eachWeek'] + '\n' + it['time'].rstrip('???')[pos - 4:pos] + '???\n' + location
                        if self.tableClass.item(eachRow, column) == None:
                            current = ''
                        else:
                            current = '\n\n' + self.tableClass.item(eachRow, column).text()
                        if current.lstrip('\n\n') != classString:
                            self.tableClass.setItem(eachRow, column, QTableWidgetItem(classString + current))
                            self.tableClass.item(eachRow, column).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        if obj.findall(classData[-1]['title']) == []:
            others = classData[-1]['title'].replace(';', '\n')
            self.tableClass.setItem(6, 0, QTableWidgetItem(others))

    def showDetail(self, item) -> None:
        if item == None:
            return
        info = item.text()
        QMessageBox.about(self, "????????????", info)

    def dealEventList(self, lis):
        # ???????????????????????????MyEvent??????????????? ??????????????????
        event = list()
        timeDic = {'???': 1, '???': 2, '???': 3, '???': 4, '???': 5, '???': 6, '???': 7}
        # ??????????????????????????????
        summary = f'{lis[0]}@{lis[-1]}'
        description = f'?????????{lis[1]}\\n{lis[2]}\\n??????????????????'
        location = lis[-1]

        # ??????????????????
        weeks = []
        parity = lis[2][lis[2].index('('):]
        content = lis[2][: lis[2].index('(')]
        ret1 = content.split(',')
        for each in ret1:
            if '-' not in each:
                weeks.append(int(each))
            else:
                ret2 = each.split('-')
                for i in range(int(ret2[0]), int(ret2[1]) + 1):
                    if parity == '(???)':
                        weeks.append(i)
                    elif parity == '(??????)':
                        if i % 2 == 0:
                            weeks.append(i)
                    elif parity == '(??????)':
                        if i % 2 == 1:
                            weeks.append(i)


        # ????????????????????????????????????
        # ???????????????????????? hour minu sec
        minu = sec = 0
        everyDay = {1: 8, 2: 10, 3: 14, 4: 16, 5: 19, 6:21}
        temp = lis[4].rstrip("???")
        temp = temp[2:]
        temp = int(temp) / 2
        hour = everyDay[temp]

        eventStart = MyDateTime()
        eventStart.setTime(hour, minu, sec)
        eventEnd = MyDateTime()
        eventEnd.setTime(hour + 1, 40, sec)

        # ?????????????????????????????????
        # ??????????????? year month day
        for i in weeks:
            obj = re.compile(f'???{i}??? (?P<weekStart>.*?)??????(?P<weekEnd>.*?)???')
            myIter = obj.finditer(self.textEdit.toPlainText())
            weekStart = myIter.__next__()['weekStart'].split('-')
            year = int(weekStart[0])
            month = int(weekStart[1])
            day = int(weekStart[2])
            eventStart.setDate(year, month, day)
            eventStart.addDate(days=timeDic[lis[3][-1]])
            eventEnd.date_ = eventStart.date_
            alar = MyAlarm(20)
            self.num += 1
            uid = self.user + '_' + self.searchTerm.currentText() + '_' + str(self.num)
            e = MyEvent(summary, eventStart, eventEnd, uid, description, location, alar)
            event.append(e)
        return event

    def dealTabChange(self, index):
        self.scoreStack.setCurrentIndex(index)

    def on_combo1stTerm_currentTextChanged(self, text):
        self.tableValid.clearContents()
        self.tableValid.setRowCount(0)
        term = {'xnxq01id': ''}
        if text != '---?????????---':
            term['xnxq01id'] = text
        self.askValid.emit(self.session, term)
        try:
            self.validThread.start()
        except AttributeError:
            sys.exit(0)

    def on_combo3rdTerm_currentTextChanged(self, text):
        self.tableOrigin.clearContents()
        self.tableOrigin.setRowCount(0)
        term = {'xnxq01id': ''}
        if text != '---?????????---':
            term['xnxq01id'] = text
        self.askOrigin.emit(self.session, term)
        try:
            self.originThread.start()
        except AttributeError:
            sys.exit(0)

    def on_rankSearch_released(self):
        self.tableRank.clearContents()
        self.tableRank.setRowCount(0)
        term = {'xqfw': self.combo2ndTerm.currentText()}
        rankUrl = 'http://csujwc.its.csu.edu.cn/jsxsd/kscj/zybm_cx'
        resp = self.session.post(rankUrl, data=term)
        soup = BeautifulSoup(resp.text, 'html.parser')
        ret = soup.find('table', id="dataList")
        temp = ret.find_all('tr')[1]
        ranks = temp.find_all('td')
        row = self.tableRank.rowCount()
        self.tableRank.insertRow(row)
        column = -1
        try:
            for rank in ranks:
                column += 1
                self.tableRank.setItem(row, column, QTableWidgetItem(rank.text))
                self.tableRank.item(row, column).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        except AttributeError:
            QMessageBox.about(self, '????????????', '????????????????????????')
        resp.close()

    def setTableClass(self, paramGet):
        self.tableClass.clearContents()
        classUrl = 'http://csujwc.its.csu.edu.cn/jsxsd/kbxx/getKbxx.do'
        resp = self.session.get(classUrl, params=paramGet)
        # print(resp.text)
        try:
            classData = tuple(eval(resp.text))
            self.display(classData)
        except SyntaxError:
            QMessageBox.about(self, '?????????', '??????????????????')
        resp.close()
        # ????????????????????????????????????????????????

    def setTermDate(self, paramGet):
        url = 'http://csujwc.its.csu.edu.cn/jsxsd/xskb/xskb_list.do?Ves632DSdyV=NEW_XSD_WDKB'
        ret = self.session.get(url, params=paramGet)
        soup = BeautifulSoup(ret.text, 'html.parser')
        temp = soup.find_all('table', class_="Nsb_r_list Nsb_table")[1]
        date = temp.find_all('td')
        self.textEdit.setText('???????????????????????????')
        if len(date) == 0:
            self.buttonIcs.setDisabled(True)
        else:
            self.buttonIcs.setDisabled(False)
        for td in date:
            self.textEdit.append(td.text)
        ret.close()

    def on_buttonFind_released(self):
        paramGet = {'xnxq01id': self.searchTerm.currentText(), 'zc': ''}
        self.setTableClass(paramGet)
        self.setTermDate(paramGet)

    def on_buttonDownload_released(self):
        downloadUrl = 'http://csujwc.its.csu.edu.cn/jsxsd/xskb/xskb_print.do'
        paramGet = {'xnxq01id': self.searchTerm.currentText(), 'zc': ''}
        resp = self.session.post(downloadUrl, data=paramGet)
        name = self.user + '_' + self.searchTerm.currentText() + '.xls'
        fileName = QFileDialog.getSaveFileName(self, '????????????', '../' + name, 'Excel?????????(*.xls *.xlsx)')
        if fileName[0] == '':
            return
        with open(fileName[0], 'wb') as file:
            file.write(resp.content)
        resp.close()
        QMessageBox.about(self, '????????????', '????????????')

    def on_buttonIcs_released(self):
        name = ''
        if self.classPage == 0:
            name = self.user + '_' + self.searchTerm.currentText() + '.ics'
        elif self.classPage == 1:
            name = self.everyClass.idNum + '_' + self.searchTerm.currentText() + '.ics'
        classCalendar = MyIcalendar(name)
        self.num = 0  # ??????UID
        for row in range(self.tableClass.rowCount() - 1):
            for column in range(self.tableClass.columnCount()):
                if self.tableClass.item(row, column) == None:
                    continue
                content = self.tableClass.item(row, column).text()
                ret = content.split('\n')
                while True:
                    if '' in ret:
                        ret.pop(ret.index(''))
                    else:
                        break
                # print(ret)
                # print(len(ret))
                if len(ret) == 6:
                    for e in self.dealEventList(ret):
                        classCalendar.addEvent(e)
                elif len(ret) == 12:
                    for e in self.dealEventList(ret[:6]):
                        classCalendar.addEvent(e)
                    for e in self.dealEventList(ret[6:]):
                        classCalendar.addEvent(e)
        fileName = QFileDialog.getSaveFileName(self, "??????ics??????", '../' + name, "????????????(*.ics)")
        if fileName[0] == "":
            return
        classCalendar.saveAsICS(fileName[0])
        QMessageBox.about(self, "??????????????????", "????????????")

    def on_buttonExit_clicked(self):
        self.exitLogin.emit()

    def on_radioValid_released(self):
        self.tabChange.emit(0)
        w = 275
        for i in range(self.tableValid.columnCount()):
            w += self.tableValid.columnWidth(i)
        self.resize(w, self.height())

    def on_radioRank_released(self):
        self.tabChange.emit(1)
        if self.tableRank.rowCount() == 0:
            self.on_rankSearch_released()
        w = 275
        for i in range(self.tableRank.columnCount()):
            w += self.tableRank.columnWidth(i)
        self.resize(w, self.height())

    def on_radioOrigin_released(self):
        self.tabChange.emit(2)
        if self.isFirstTab:
            self.isFirstTab = False
            self.combo3rdTerm.currentTextChanged.emit(self.combo3rdTerm.currentText())
        w = 275
        for i in range(self.tableOrigin.columnCount()):
            w += self.tableOrigin.columnWidth(i)
        self.resize(w, self.height())

    def on_buttonChange_released(self) -> None:
        self.tableClass.clearContents()
        self.textEdit.clear()
        self.classPage += 1
        self.classPage %= 2
        page = self.classPage
        self.searchTerm.clear()
        if page == 0:
            self.buttonIcs.setDisabled(False)
            self.searchTerm.addItems(self.classTerm)
            self.setSearchTerm()
            self.on_buttonFind_released()
        elif page == 1:
            self.searchTerm.addItems(self.everyClass.stu.terms)
            self.setSearchTerm()
            self.keyEdit.clear()
        self.classStack.setCurrentIndex(page)
        return None

    def on_classSearch_released(self):
        self.tableClass.clearContents()
        self.textEdit.clear()
        keyWord = self.keyEdit.text()
        term = self.searchTerm.currentText()
        if term == '---?????????---':
            QMessageBox.about(self, '????????????', '???????????????')
            return
        if keyWord == '':
            QMessageBox.about(self, '????????????', '???????????????')
            return
        classDict = self.everyClass.search(term, keyWord)
        if classDict == None:
            QMessageBox.about(self, '????????????', '????????????')
            return
        if len(classDict[0].keys()) == 6:
            self.buttonIcs.setDisabled(False)
        else:
            self.buttonIcs.setDisabled(True)
        self.displayDict(classDict)

    def displayDict(self, classData):
        timeDict = {'1': '???', '2': '???', '3': '???', '4': '???', '5': '???', '6': '???', '7': '???'}
        for class_ in classData[:-1]:
            # print(class_)
            temp = class_['dayTime'].rstrip('???')
            temp = temp[temp.index('-') + 1 : ]
            weekNum = class_['eachWeek'][-1]
            if weekNum == '0':
                class_['eachWeek'] = '??????7'
                weekNum = '7'
            row = int(temp) // 2 - 1
            column = int(class_['eachWeek'][-1]) - 1
            class_['eachWeek'] = class_['eachWeek'].replace(weekNum, timeDict[weekNum])
            classString = ''
            for value in class_.values():
                classString += value + '\n'
            try:
                current = self.tableClass.item(row, column).text() + '\n'
            except:
                current = ''
            # print(current)
            self.tableClass.setItem(row, column, QTableWidgetItem(current + classString))
            self.tableClass.item(row, column).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        bzdata = classData[-1]
        bzlist = bzdata['bztext'].split(';')
        bztext = ''
        for bz in bzlist:
            bztext += bz + '\n\n'
        self.tableClass.setItem(6, 0, QTableWidgetItem(bztext))
        self.tableClass.item(6, 0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        paramGet = {'xnxq01id': self.searchTerm.currentText(), 'zc': ''}
        self.setTermDate(paramGet)

    def EvalBtnDown(self):
        index = self.tableEvalCose.currentRow()
        # print(index)
        self.TeaEval.getDetail(index, self.session)
        self.displayEvaldetail()

    def displayEvaldetail(self):
        self.tableTeaScore.clearContents()
        length = len(self.TeaEval.teachers)
        self.tableTeaScore.setRowCount(length)
        combos = []
        row = -1
        for each in self.TeaEval.teachers:
            row += 1

            comboBox = QComboBox()
            comboBox.setEditable(False)
            scores = [str(num) for num in each[3]]
            comboBox.addItems(scores)
            combos.append(comboBox)

            self.tableTeaScore.setItem(row, 0, QTableWidgetItem(each[1]))
            self.tableTeaScore.item(row, 0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tableTeaScore.setItem(row, 1, QTableWidgetItem(each[0]))
            self.tableTeaScore.item(row, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tableTeaScore.setCellWidget(row, 2, combos[row])

    def displayEvalall(self) -> None:
        length = len(self.TeaEval.rows)
        self.tableEvalCose.setRowCount(length)
        btns = []
        for i in range(length):
            btn = QPushButton()
            btn.setText('??????')
            btn.clicked.connect(self.EvalBtnDown)
            btns.append(btn)
        row = -1
        for r in self.TeaEval.rows:
            row += 1
            column = -1
            for c in r[:-1]:
                column += 1
                self.tableEvalCose.setItem(row, column, QTableWidgetItem(c))
                self.tableEvalCose.item(row, column).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tableEvalCose.setCellWidget(row, 6, btns[row])

    def on_btnEval_released(self):
        if self.tableTeaScore.rowCount() == 0:
            QMessageBox.about(self, '????????????', '???????????????????????????')
            return
        else:
            threadPool = ThreadPoolExecutor(max_workers=10, thread_name_prefix="save_do")
            for index in range(self.tableTeaScore.rowCount()):
                score = float(self.tableTeaScore.cellWidget(index, 2).currentText())
                threadPool.submit(self.TeaEval.saveDo, self.session, index, score)
                # print(threading.current_thread().ident)
                # self.TeaEval.saveDo(self.session, index, score)
            threadPool.shutdown(wait=True)
            self.TeaEval.pltj_savedo(self.session)
            if self.TeaEval.isOk:
                QMessageBox.about(self, '????????????', '???????????????')
            else:
                QMessageBox.about(self, '????????????', '???????????????')

    # ?????????????????????????????? ????????? ?????????????????????
    def dealtabWidgetChange(self, index: int) -> None:
        # print(index)
        if index == 1 and self.isable[index] == 0:
            self.isable[index] = 1
            self.combo1stTerm.currentTextChanged.emit(self.combo1stTerm.currentText())
        elif index == 2 and self.isable[index] == 0:
            if self.TeaEval.getInfo(self.session) == 0:
                QMessageBox.about(self, '????????????', '??????????????????')
                self.tabWidget.setCurrentIndex(0)
            else:
                self.displayEvalall()
        # self.tabWidget.currentChanged.disconnect(self.dealtabWidgetChange)