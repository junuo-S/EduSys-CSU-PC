import sys

from PyQt5.QtCore import QThread, pyqtSignal
import requests
from bs4 import BeautifulSoup

class validThread(QThread):
    readyValid=pyqtSignal(list)
    def __init__(self):
        super(validThread, self).__init__()
        self.session=requests.session()
        self.data={}
        self.exitCode = 0

    def dealaskValid(self, session, data):
        self.session=session
        self.data=data

    def run(self) -> None:
        validScoreUrl = 'http://csujwc.its.csu.edu.cn/jsxsd/kscj/cjcx_list'
        resp = self.session.post(validScoreUrl, data=self.data)
        soup = BeautifulSoup(resp.text, 'html.parser')

        temp = soup.find('table', id="dataList")
        try:
            scores = temp.find_all('tr')[1:]
        except AttributeError:
            self.exitCode = -1
            return
        validScores = list()
        for score in scores[::2]:
            rets = score.find_all('td')
            score = list()
            for ret in rets[1:]:
                score.append(ret.text)
            validScores.append(score)

        self.readyValid.emit(validScores)
        resp.close()