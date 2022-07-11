import sys

from PyQt5.QtCore import QThread, pyqtSignal
from bs4 import BeautifulSoup
import requests


class Init2Thread(QThread):
    readyInit=pyqtSignal()
    readyInitValid=pyqtSignal(list, list)
    readyInitRank = pyqtSignal(list, list)
    readyInitOrigin = pyqtSignal(list, list)
    def __init__(self):
        super(Init2Thread, self).__init__()
        self.session=requests.session()
        self.exitCode = 0

    def recFromMain(self, session):
        self.session=session

    def run(self) -> None:
        validScoreUrl = 'http://csujwc.its.csu.edu.cn/jsxsd/kscj/cjcx_list'
        resp = self.session.get(validScoreUrl)
        soup = BeautifulSoup(resp.text, 'html.parser')
        ret = soup.find('table', id="dataList")
        try:
            temp = ret.find_all('th')
        except AttributeError:
            self.exitCode = -1
            return
        heads = []
        for head in temp[1:]:
            heads.append(head.text)
        ret = soup.find_all('option')
        options = []
        for option in ret:
            options.append(option)
        self.readyInitValid.emit(heads, options)

        rankUrl = 'http://csujwc.its.csu.edu.cn/jsxsd/kscj/zybm_cx'
        resp = self.session.get(rankUrl)
        soup = BeautifulSoup(resp.text, 'html.parser')
        rets = soup.find_all('option')
        options = []
        for ret in rets:
            options.append(ret.text)
        ret = soup.find('table', id="dataList")
        temp = ret.find_all('th')
        heads = []
        for head in temp:
            heads.append(head.text)
        self.readyInitRank.emit(heads, options)

        originUrl='http://csujwc.its.csu.edu.cn/jsxsd/kscj/yscjcx_list'
        resp=self.session.get(originUrl)
        soup=BeautifulSoup(resp.text,'html.parser')
        rets = soup.find_all('option')
        options = []
        for ret in rets:
            options.append(ret.text)
        ret = soup.find('table', id="dataList")
        temp = ret.find_all('th')
        heads = []
        for head in temp:
            heads.append(head.text)
        self.readyInitOrigin.emit(heads, options)

        self.readyInit.emit()
        resp.close()