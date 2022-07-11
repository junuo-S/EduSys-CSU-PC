import requests
from bs4 import BeautifulSoup
import re
import threading


class Evaluation:
    def __init__(self):
        self.rows = []
        self.teachers = []
        self.current = -1
        self.isOk = False

    def getInfo(self, session: requests.Session) -> int:
        url = 'http://csujwc.its.csu.edu.cn/jsxsd/xspj/xspj_find.do?Ves632DSdyV=NEW_XSD_JXPJ'
        resp = session.get(url)
        # print(resp.text)
        soup = BeautifulSoup(resp.text, 'html.parser')
        temp = soup.find('div', class_="Nsb_layout_r")
        trs = temp.find_all('tr')[1:]
        self.rows.clear()
        for tr in trs:
            tds = tr.find_all('td')
            temp = []
            for td in tds[:-1]:
                temp.append(td.text)
            href = tds[-1].find('a').get('href')
            temp.append(href)
            self.rows.append(temp)
        resp.close()
        return len(self.rows)

    def getDetail(self, index, sesssion: requests.Session):
        self.current = index
        url = 'http://csujwc.its.csu.edu.cn' + self.rows[index][-1]
        resp = sesssion.get(url)
        # print(resp.text)
        soup = BeautifulSoup(resp.text, 'html.parser')
        trs = soup.find_all('div', class_="Nsb_pw")[2].find_all('tr')[1:-1]
        self.teachers.clear()
        for tr in trs:
            per = tr.find_all('td')
            name = per[3].text
            clasName = per[2].text
            hreftem = per[8].find('a').get('href')
            obj = re.compile(r"\'(.*?)\'")
            href = obj.findall(hreftem)[0]
            ret_scores, all_scores = self.getPerTeaScores(sesssion, href)
            temp = (name, clasName, href, ret_scores, all_scores)
            self.teachers.append(temp)
        # print(self.teachers)
        resp.close()

    def getPerTeaScores(self, session:requests.Session, url:str) -> list:
        perUrl = 'http://csujwc.its.csu.edu.cn' + url
        resp = session.get(perUrl)
        soup = BeautifulSoup(resp.text, 'html.parser')
        table = soup.find('table', id = 'table1')
        trs = table.find_all('tr')
        length = 0
        all_score = []
        for tr in trs[:-1]:
            pertds = tr.find_all('td')
            if len(pertds) == 2:
                length += 1
                inputs = pertds[1].find_all('input')
                if len(inputs) != 8 and len(inputs) != 10:
                    continue
                temp = []
                for input in inputs[1::2]:
                    value = input.get('value')
                    temp.append(value)
                temp = [float(num) for num in temp]
                all_score.append(temp)
        # print(all_score)
        ret_score=[]
        if len(all_score) == 7:
            ret_score = [98, 97, 96, 95.5, 95, 94, 93.5, 93, 92.5, 92, 91.5, 91, 90.5, 90, 89.5, 89, 88.5, 88, 87.5, 87, 86.5, 86, 85.5, 85, 84.5, 84, 83.5, 83, 82.5, 82, 81.5, 81, 80.5, 80, 79.5, 79, 78.5, 78, 77.5, 77, 76.5, 76, 75.5, 75, 74.5, 74, 73.5, 73, 72.5, 72, 71.5, 71, 70.5, 70, 69.5, 69, 68.5, 68, 67.5, 67, 66.5, 66, 65.5, 65, 64.5, 64, 63.5, 63, 62.5, 62, 61.5, 61]
        elif len(all_score) == 11:
            ret_score = [98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61]
        return [ret_score, all_score]

    def getIndexes(self, score: float, length = 7) -> tuple:
        if length == 7:
            s = [
                [15, 12, 10.5, 9],
                [15, 12, 10.5, 9],
                [15, 12, 10.5, 9],
                [10, 8, 7, 6],
                [15, 12, 10.5, 9],
                [15, 12, 10.5, 9],
                [15, 12, 10.5, 9]
            ]
            for i1 in range(4):
                for i2 in range(4):
                    for i3 in range(4):
                        for i4 in range(4):
                            for i5 in range(4):
                                for i6 in range(4):
                                    for i7 in range(4):
                                        if i1 == i2 == i3 == i4 == i5 == i6 == i7:
                                            continue
                                        else:
                                            temp = s[0][i1] + s[1][i2] + s[2][i3] + s[3][i4] + s[4][i5] + s[5][i6] + s[6][i7]
                                            if temp == score:
                                                return (i1, i2, i3, i4, i5, i6, i7)
        elif length == 11:
            s = [
                    [7.5, 6.0, 5.25, 4.5],
                    [7.5, 6.0, 5.25, 4.5],
                    [10.0, 8.0, 7.0, 6.0],
                    [10.0, 8.0, 7.0, 6.0],
                    [12.0, 9.6, 8.4, 7.2],
                    [9.0, 7.2, 6.3, 5.4],
                    [9.0, 7.2, 6.3, 5.4],
                    [7.5, 6.0, 5.25, 4.5],
                    [7.5, 6.0, 5.25, 4.5],
                    [10.0, 8.0, 7.0, 6.0],
                    [10.0, 8.0, 7.0, 6.0]
                ]
            index = [0 for i in range(11)]
            for index[0] in range(4):
                for index[1] in range(4):
                    for index[2] in range(4):
                        for index[3] in range(4):
                            for index[4] in range(4):
                                for index[5] in range(4):
                                    for index[6] in range(4):
                                        for index[7] in range(4):
                                            for index[8] in range(4):
                                                for index[9] in range(4):
                                                    for index[10] in range(4):
                                                        if index[0] == index[1] == index[2] == index[3] == index[4] == \
                                                                index[5] == index[6] == index[7] == index[8] == index[
                                                            9] == index[10]:
                                                            continue
                                                        else:
                                                            temp = s[0][index[0]] + s[1][index[1]] + s[2][index[2]] + \
                                                                   s[3][index[3]] + s[4][index[4]] + s[5][index[5]] + \
                                                                   s[6][index[6]] + s[7][index[7]] + s[8][index[8]] + \
                                                                   s[9][index[9]] + s[10][index[10]]
                                                            if temp == score:
                                                                return tuple(index)

    def saveDo(self, session: requests.Session, index:int, score: float):
        # print(threading.current_thread().ident)
        postUrl = 'http://csujwc.its.csu.edu.cn/jsxsd/xspj/xspj_save.do'
        form = {}
        url = 'http://csujwc.its.csu.edu.cn' + self.teachers[index][2]
        resp = session.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        ret = soup.find('form', method="post")
        inputs = ret.find_all('input')

        # 这里的13个是表单的开头 都一样的
        for index in range(13):
            key = inputs[index].get('name')
            value = inputs[index].get('value')
            form[key] = value

        step = -1
        len_item = -1
        # print(len(inputs))
        if len(inputs) == 76 or len(inputs) == 77:
            step = 9
            len_item = 7
        elif len(inputs) == 127 or len(inputs) == 125:
            len_item = 11
            step = 10

        # form['pj06xh'] = [4, 5, 7, 6, 3, 8, 2]
        form['pj06xh'] = []
        form['pj06id'] = []
        indexs = self.getIndexes(score, len_item)
        for index in range(len_item):
            begin = index * step
            end = begin + step
            pScore = inputs[13:-2][begin:end]
            # print(pScore)
            pindex = indexs[index] * 2 + 2
            key = pScore[0].get('name')
            value = pScore[0].get('value')
            if key  == 'pj06xh':
                form[key].append(value)
            key = pScore[1].get('name')
            value = pScore[1].get('value')
            if key == 'pj06id':
                form[key].append(value)

            temp = (pindex, 3, 5, 7, 9)
            for i in temp:
                try:
                    key = pScore[i].get('name')
                    value = pScore[i].get('value')
                    form[key] = value
                except:
                    pass
        key = inputs[-3].get('name')
        value = inputs[-3].get('value')
        form[key] = value
        form['jynr'] = ''
        # print(form)
        session.post(postUrl, data=form).close()
        resp.close()

    def pltj_savedo(self, session:requests.Session):
        posturl = 'http://csujwc.its.csu.edu.cn/jsxsd/xspj/pltj_save.do'
        infourl = 'http://csujwc.its.csu.edu.cn' + self.rows[self.current][-1]
        resp = session.get(infourl)
        soup = BeautifulSoup(resp.text, 'html.parser')
        form = soup.find('form', id="Form1")
        inputs = form.find_all('input')
        # print(len(inputs), inputs)
        params = {}
        params['isissub'] = []
        for input in inputs:
            key = input.get('name')
            value = input.get('value')
            if key == 'isissub':
                params[key].append(value)
            elif key == None:
                continue
            else:
                params[key] = value
        session.post(posturl, data=params).close()
        self.isOK(resp.text)
        resp.close()

    def isOK(self, html:str) -> bool:
        soup = BeautifulSoup(html, 'html.parser')
        form = soup.find('form', id="Form1")
        trs = form.find_all('tr')
        done_score = []
        for tr in trs[1:-1]:
            scoretd = tr.find_all('td')[5]
            obj = re.compile(r'<td>(.*?)<br/>')
            # print(str(scoretd))
            ret = obj.findall(str(scoretd).replace('\n', '').replace(' ', '').replace('\t', '').replace('\r', ''))
            done_score.append(float(ret[0]))

        if 0.0 not in done_score:
            self.isOk = True
        return self.isOk