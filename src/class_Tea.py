import requests
import re
from bs4 import BeautifulSoup

class class_Tea:
    def __init__(self, term: str):
        url = self.makeUrl(term)
        self.tea_data = self.getallTeaInfo(url)
        self.user = ''
        self.jgId = ''

    def makeUrl(self, term:str) -> str:
        return f'http://csujwc.its.csu.edu.cn/jiaowu/pkgl/llsykb/llsykb_find_jg0101.jsp?xnxq01id={term}'

    def getallTeaInfo(self, url) -> list:
        resp = requests.post(url)
        resp.encoding = 'utf-8'
        searchTea = re.compile(r'var js="\[(.*?)]"')
        teachers = searchTea.findall(resp.text)[0].replace('jg0101id', "'jg0101id'")\
            .replace('jgh', "'jgh'").replace('xm', "'xm'")
        teacherData = eval(teachers)
        # print(teacherData)
        resp.close()
        return teacherData

    def getNames(self) -> set:
        names = set()
        for each in self.tea_data:
            names.add(each['xm'])
        return names

    def findallTea(self, keyword:str) -> list:
        userList = []
        for each in self.tea_data:
            name = each['xm']
            if name == keyword or each['jgh'] == keyword:
                user = self.getTeaInfo(each['jgh'], name)
                userList.append(user)
        return userList

    def getTeaInfo(self, jgId: str, xm = '') -> tuple:
        baseUrl = 'https://app.its.csu.edu.cn/csu-app/cgi-bin/privateadbook?method=queryUser'
        url = f'{baseUrl}&userName={xm}'
        resp = requests.get(url)
        data = resp.json()
        if len(data['data']) == 0:
            resp.close()
            url = f'{baseUrl}&userName={jgId}'
            resp = requests.get(url)
            data = resp.json()
        # print(data)
        resp.close()
        name=''
        if xm != '':
            name = xm
        dept=''
        for i in range(len(data['data'])):
            if data['data'][i]['realUserId'] == jgId:
                dept = data['data'][i]['dept']
        jg0101id = ''
        for each in self.tea_data:
            if each['jgh'] == jgId:
                jg0101id = each['jg0101id']
        # print((1, name, jgId, dept, ' ', jg0101id))
        return (1, name, jgId, dept, ' ', jg0101id)

    def downloadData(self, param) -> list:
        classData = []
        url = 'http://csujwc.its.csu.edu.cn/jiaowu/pkgl/llsykb/llsykb_kb.jsp'
        resp = requests.post(url, data=param)
        resp.encoding = 'utf-8'
        # print(resp.text)
        soup = BeautifulSoup(resp.text, 'html.parser')
        bzdiv = soup.find('div', id='bzdiv')
        kbtable = soup.find('table', id="kbtable")
        # print(kbtable)
        row = -1
        trs = kbtable.find_all('tr')
        for tr in trs:
            column = -1
            row += 1
            tds = tr.find_all('td')
            if len(tds) != 8:
                continue
            for info in tds[1:]:
                column += 1
                kbcontent = info.find_all('div', class_="kbcontent")[0]
                if 'javascript' in str(kbcontent):
                    # print(kbcontent)
                    kbList = str(kbcontent).split('------------------------------')
                    for kb in kbList:
                        kbsoup = BeautifulSoup(kb, 'html.parser')
                        className = kbsoup.find('font', title="课程名称").text
                        tem1 = kbsoup.find('font', title="周次").text
                        try:
                            tem2 = kbsoup.find('font', title="单双周").text
                        except:
                            tem2 = '周'
                        allWeek = f'{tem1}({tem2})'
                        eachWeek = f'星期{column}'
                        dayTime = f'{row * 2 - 1}-{row * 2}节'
                        try:
                            location = kbsoup.find('font', title="上课地点教室").text
                        except:
                            location = ' '
                        allWeek_pop = allWeek.replace('(', '').replace(')', '')
                        data = {'className': className, 'allWeek': allWeek, 'eachWeek': eachWeek,
                                'dayTime': dayTime, 'location': location}
                        classData.append(data)
        data = {'bztext': bzdiv.text}
        classData.append(data)
        resp.close()
        return classData