from PyQt5.QtCore import QThread, pyqtSignal
import requests
from bs4 import BeautifulSoup

class originThread(QThread):
    readyOrigin=pyqtSignal(list)
    def __init__(self):
        super(originThread, self).__init__()
        self.session=requests.session()
        self.data={}
        self.exitCode = 0

    def dealaskOrigin(self, session, data):
        self.session=session
        self.data=data

    def run(self) -> None:
        originUrl='http://csujwc.its.csu.edu.cn/jsxsd/kscj/yscjcx_list'
        resp = self.session.post(originUrl, data=self.data)
        soup = BeautifulSoup(resp.text, 'html.parser')

        temp = soup.find('table', id="dataList")
        try:
            scores = temp.find_all('tr')[1:]
        except AttributeError:
            self.exitCode = -1
            return
        originScores = list()
        for score in scores:
            rets = score.find_all('td')
            score = list()
            for ret in rets:
                score.append(ret.text)
            originScores.append(score)

        self.readyOrigin.emit(originScores)
        resp.close()