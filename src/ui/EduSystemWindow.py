# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EduSystemWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_eduSys(object):
    def setupUi(self, eduSys):
        eduSys.setObjectName("eduSys")
        eduSys.setWindowModality(QtCore.Qt.NonModal)
        eduSys.resize(1252, 843)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/:/Image/中南大学校徽.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        eduSys.setWindowIcon(icon)
        eduSys.setAutoFillBackground(True)
        eduSys.setStyleSheet("*{ \n"
"    font: 9pt \"宋体\";\n"
"    font-size:18px;\n"
"}\n"
"QPushButton:hover { color: green;\n"
"font-size:22px;\n"
"border:1px solid #1d649c;\n"
" }\n"
"QTextEdit { background-color: rgb(216, 255, 221) }")
        self.gridLayout = QtWidgets.QGridLayout(eduSys)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(eduSys)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.MyClass = QtWidgets.QWidget()
        self.MyClass.setObjectName("MyClass")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.MyClass)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.MyClass)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.searchTerm = QtWidgets.QComboBox(self.MyClass)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.searchTerm.setFont(font)
        self.searchTerm.setObjectName("searchTerm")
        self.horizontalLayout_7.addWidget(self.searchTerm)
        self.classStack = QtWidgets.QStackedWidget(self.MyClass)
        self.classStack.setObjectName("classStack")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonFind = QtWidgets.QPushButton(self.page)
        self.buttonFind.setObjectName("buttonFind")
        self.horizontalLayout.addWidget(self.buttonFind)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonDownload = QtWidgets.QPushButton(self.page)
        self.buttonDownload.setObjectName("buttonDownload")
        self.horizontalLayout.addWidget(self.buttonDownload)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.classStack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.keyEdit = QtWidgets.QLineEdit(self.page_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.keyEdit.setFont(font)
        self.keyEdit.setObjectName("keyEdit")
        self.horizontalLayout_6.addWidget(self.keyEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.classSearch = QtWidgets.QPushButton(self.page_2)
        self.classSearch.setObjectName("classSearch")
        self.horizontalLayout_6.addWidget(self.classSearch)
        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.classStack.addWidget(self.page_2)
        self.horizontalLayout_7.addWidget(self.classStack)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.buttonIcs = QtWidgets.QPushButton(self.MyClass)
        self.buttonIcs.setObjectName("buttonIcs")
        self.horizontalLayout_7.addWidget(self.buttonIcs)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.buttonChange = QtWidgets.QPushButton(self.MyClass)
        self.buttonChange.setObjectName("buttonChange")
        self.horizontalLayout_7.addWidget(self.buttonChange)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.buttonExit = QtWidgets.QPushButton(self.MyClass)
        self.buttonExit.setObjectName("buttonExit")
        self.horizontalLayout_7.addWidget(self.buttonExit)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.horizontalLayout_7.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableClass = QtWidgets.QTableWidget(self.MyClass)
        self.tableClass.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableClass.setAcceptDrops(False)
        self.tableClass.setToolTipDuration(-1)
        self.tableClass.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableClass.setAutoFillBackground(True)
        self.tableClass.setLineWidth(1)
        self.tableClass.setMidLineWidth(1)
        self.tableClass.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableClass.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableClass.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableClass.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableClass.setShowGrid(True)
        self.tableClass.setGridStyle(QtCore.Qt.SolidLine)
        self.tableClass.setObjectName("tableClass")
        self.tableClass.setColumnCount(7)
        self.tableClass.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClass.setHorizontalHeaderItem(6, item)
        self.tableClass.horizontalHeader().setVisible(True)
        self.tableClass.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClass.horizontalHeader().setSortIndicatorShown(False)
        self.tableClass.horizontalHeader().setStretchLastSection(False)
        self.tableClass.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableClass)
        self.textEdit = QtWidgets.QTextEdit(self.MyClass)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 15)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.MyClass, "")
        self.MyScore = QtWidgets.QWidget()
        self.MyScore.setObjectName("MyScore")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MyScore)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(25)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioValid = QtWidgets.QRadioButton(self.MyScore)
        self.radioValid.setObjectName("radioValid")
        self.verticalLayout_4.addWidget(self.radioValid)
        self.radioRank = QtWidgets.QRadioButton(self.MyScore)
        self.radioRank.setObjectName("radioRank")
        self.verticalLayout_4.addWidget(self.radioRank)
        self.radioOrigin = QtWidgets.QRadioButton(self.MyScore)
        self.radioOrigin.setObjectName("radioOrigin")
        self.verticalLayout_4.addWidget(self.radioOrigin)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.scoreStack = QtWidgets.QStackedWidget(self.MyScore)
        self.scoreStack.setObjectName("scoreStack")
        self.validScore = QtWidgets.QWidget()
        self.validScore.setObjectName("validScore")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.validScore)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.validScore)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.combo1stTerm = QtWidgets.QComboBox(self.validScore)
        self.combo1stTerm.setObjectName("combo1stTerm")
        self.horizontalLayout_3.addWidget(self.combo1stTerm)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.tableValid = QtWidgets.QTableWidget(self.validScore)
        self.tableValid.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableValid.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableValid.setObjectName("tableValid")
        self.tableValid.setColumnCount(0)
        self.tableValid.setRowCount(0)
        self.verticalLayout_5.addWidget(self.tableValid)
        self.scoreStack.addWidget(self.validScore)
        self.proRank = QtWidgets.QWidget()
        self.proRank.setObjectName("proRank")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.proRank)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.label_2 = QtWidgets.QLabel(self.proRank)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.combo2ndTerm = QtWidgets.QComboBox(self.proRank)
        self.combo2ndTerm.setObjectName("combo2ndTerm")
        self.horizontalLayout_4.addWidget(self.combo2ndTerm)
        self.rankSearch = QtWidgets.QPushButton(self.proRank)
        self.rankSearch.setObjectName("rankSearch")
        self.horizontalLayout_4.addWidget(self.rankSearch)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 3)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.tableRank = QtWidgets.QTableWidget(self.proRank)
        self.tableRank.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableRank.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableRank.setObjectName("tableRank")
        self.tableRank.setColumnCount(0)
        self.tableRank.setRowCount(0)
        self.verticalLayout_6.addWidget(self.tableRank)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem13)
        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 50)
        self.scoreStack.addWidget(self.proRank)
        self.originalScore = QtWidgets.QWidget()
        self.originalScore.setObjectName("originalScore")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.originalScore)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.originalScore)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.combo3rdTerm = QtWidgets.QComboBox(self.originalScore)
        self.combo3rdTerm.setObjectName("combo3rdTerm")
        self.horizontalLayout_5.addWidget(self.combo3rdTerm)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.tableOrigin = QtWidgets.QTableWidget(self.originalScore)
        self.tableOrigin.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableOrigin.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableOrigin.setObjectName("tableOrigin")
        self.tableOrigin.setColumnCount(0)
        self.tableOrigin.setRowCount(0)
        self.verticalLayout_7.addWidget(self.tableOrigin)
        self.scoreStack.addWidget(self.originalScore)
        self.horizontalLayout_2.addWidget(self.scoreStack)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.MyScore, "")
        self.evaluation = QtWidgets.QWidget()
        self.evaluation.setObjectName("evaluation")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.evaluation)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableEvalCose = QtWidgets.QTableWidget(self.evaluation)
        self.tableEvalCose.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableEvalCose.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableEvalCose.setObjectName("tableEvalCose")
        self.tableEvalCose.setColumnCount(7)
        self.tableEvalCose.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableEvalCose.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEvalCose.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEvalCose.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEvalCose.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEvalCose.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEvalCose.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEvalCose.setHorizontalHeaderItem(6, item)
        self.verticalLayout_3.addWidget(self.tableEvalCose)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.tableTeaScore = QtWidgets.QTableWidget(self.evaluation)
        self.tableTeaScore.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableTeaScore.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableTeaScore.setObjectName("tableTeaScore")
        self.tableTeaScore.setColumnCount(3)
        self.tableTeaScore.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableTeaScore.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTeaScore.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTeaScore.setHorizontalHeaderItem(2, item)
        self.tableTeaScore.horizontalHeader().setCascadingSectionResizes(False)
        self.tableTeaScore.horizontalHeader().setStretchLastSection(False)
        self.horizontalLayout_9.addWidget(self.tableTeaScore)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.btnEval = QtWidgets.QPushButton(self.evaluation)
        self.btnEval.setObjectName("btnEval")
        self.horizontalLayout_9.addWidget(self.btnEval)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem17)
        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 8)
        self.horizontalLayout_9.setStretch(2, 1)
        self.horizontalLayout_9.setStretch(3, 1)
        self.horizontalLayout_9.setStretch(4, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 5)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.evaluation, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(eduSys)
        self.tabWidget.setCurrentIndex(0)
        self.classStack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(eduSys)

    def retranslateUi(self, eduSys):
        _translate = QtCore.QCoreApplication.translate
        eduSys.setWindowTitle(_translate("eduSys", "中南大学教务管理系统"))
        self.label_4.setText(_translate("eduSys", "学  期："))
        self.buttonFind.setText(_translate("eduSys", "查看课表"))
        self.buttonDownload.setText(_translate("eduSys", "导出课表"))
        self.keyEdit.setPlaceholderText(_translate("eduSys", "输入姓名/学号"))
        self.classSearch.setText(_translate("eduSys", "查询课表"))
        self.buttonIcs.setText(_translate("eduSys", "生成日程文件"))
        self.buttonChange.setText(_translate("eduSys", "切换"))
        self.buttonExit.setText(_translate("eduSys", "退出登录"))
        item = self.tableClass.verticalHeaderItem(0)
        item.setText(_translate("eduSys", "1~2节"))
        item = self.tableClass.verticalHeaderItem(1)
        item.setText(_translate("eduSys", "3~4节"))
        item = self.tableClass.verticalHeaderItem(2)
        item.setText(_translate("eduSys", "5~6节"))
        item = self.tableClass.verticalHeaderItem(3)
        item.setText(_translate("eduSys", "7~8节"))
        item = self.tableClass.verticalHeaderItem(4)
        item.setText(_translate("eduSys", "9~10节"))
        item = self.tableClass.verticalHeaderItem(5)
        item.setText(_translate("eduSys", "11-12节"))
        item = self.tableClass.verticalHeaderItem(6)
        item.setText(_translate("eduSys", "备注"))
        item = self.tableClass.horizontalHeaderItem(0)
        item.setText(_translate("eduSys", "星期一"))
        item = self.tableClass.horizontalHeaderItem(1)
        item.setText(_translate("eduSys", "星期二"))
        item = self.tableClass.horizontalHeaderItem(2)
        item.setText(_translate("eduSys", "星期三"))
        item = self.tableClass.horizontalHeaderItem(3)
        item.setText(_translate("eduSys", "星期四"))
        item = self.tableClass.horizontalHeaderItem(4)
        item.setText(_translate("eduSys", "星期五"))
        item = self.tableClass.horizontalHeaderItem(5)
        item.setText(_translate("eduSys", "星期六"))
        item = self.tableClass.horizontalHeaderItem(6)
        item.setText(_translate("eduSys", "星期日"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MyClass), _translate("eduSys", "我的课表"))
        self.radioValid.setText(_translate("eduSys", "有效成绩查询"))
        self.radioRank.setText(_translate("eduSys", "专业排名查询"))
        self.radioOrigin.setText(_translate("eduSys", "原始成绩查询"))
        self.label.setText(_translate("eduSys", "初修学期："))
        self.label_2.setText(_translate("eduSys", "选择学期:"))
        self.rankSearch.setText(_translate("eduSys", "查询"))
        self.label_3.setText(_translate("eduSys", "获得学期："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MyScore), _translate("eduSys", "我的成绩"))
        item = self.tableEvalCose.horizontalHeaderItem(0)
        item.setText(_translate("eduSys", "序号"))
        item = self.tableEvalCose.horizontalHeaderItem(1)
        item.setText(_translate("eduSys", "学年学期"))
        item = self.tableEvalCose.horizontalHeaderItem(2)
        item.setText(_translate("eduSys", "评价分类"))
        item = self.tableEvalCose.horizontalHeaderItem(3)
        item.setText(_translate("eduSys", "评价批次"))
        item = self.tableEvalCose.horizontalHeaderItem(4)
        item.setText(_translate("eduSys", "开始时间"))
        item = self.tableEvalCose.horizontalHeaderItem(5)
        item.setText(_translate("eduSys", "结束时间"))
        item = self.tableEvalCose.horizontalHeaderItem(6)
        item.setText(_translate("eduSys", "操作"))
        item = self.tableTeaScore.horizontalHeaderItem(0)
        item.setText(_translate("eduSys", "课程名称"))
        item = self.tableTeaScore.horizontalHeaderItem(1)
        item.setText(_translate("eduSys", "教师"))
        item = self.tableTeaScore.horizontalHeaderItem(2)
        item.setText(_translate("eduSys", "分数"))
        self.btnEval.setText(_translate("eduSys", "一键评教"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.evaluation), _translate("eduSys", "教学评价"))
import src.resource.image_rc
