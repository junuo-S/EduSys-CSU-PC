from src.ui.RepeatWindow import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem


class MyRepeatWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MyRepeatWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.SubWindow)
        self.setWindowModality(Qt.ApplicationModal)
        # self.setModal(True)
        self.__row=-1
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.itemChanged.connect(self.tableWidget.resizeRowsToContents)
        self.tableWidget.itemChanged.connect(self.tableWidget.resizeColumnsToContents)
        # self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

    def load_display(self, userList: list) -> None:
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        # self.setParent()
        for user in userList:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            if user[0] == 0:
                self.tableWidget.setItem(row, 0, QTableWidgetItem('学生'))
                self.tableWidget.item(row, 0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            elif user[0] == 1:
                self.tableWidget.setItem(row, 0, QTableWidgetItem('教工'))
                self.tableWidget.item(row, 0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tableWidget.setItem(row, 1, QTableWidgetItem(user[1]))
            self.tableWidget.item(row, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tableWidget.setItem(row, 2, QTableWidgetItem(user[3]))
            self.tableWidget.item(row, 2).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tableWidget.setItem(row, 3, QTableWidgetItem(user[4]))
            self.tableWidget.item(row, 3).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.show()
        self.exec_()

    def on_pushButton_released(self):
        row = self.tableWidget.currentRow()
        self.__row=row
        self.close()

    def getRow(self):
        return self.__row