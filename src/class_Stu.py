import requests
import re
import ast
from bs4 import BeautifulSoup

class class_Stu:
    def __init__(self, term: str) -> None:
        url = self.makeUrl(term)
        self.stu_data, self.terms= self.getTerm_Stuinfo(url)
        self.user = ''
        self.stuId = ''

    def getTerm_Stuinfo(self, url) -> list:
        resp = requests.post(url)
        resp.encoding = 'utf-8'
        obj = re.compile(r'var bj=\"(.+)\"')
        ret = obj.findall(resp.text)[0].replace('x', "'x").replace(':', "':")
        stu_data = ast.literal_eval(ret)
        soup = BeautifulSoup(resp.text, 'html.parser')
        temp = soup.find('select', id="xnxq01id")
        options = temp.find_all('option')
        terms = []
        for option in options:
            terms.append(option.text)
        resp.close()
        return [stu_data, terms]

    def makeUrl(self, term:str) -> str:
        baseUrl = r'http://csujwc.its.csu.edu.cn/jiaowu/pkgl/llsykb/llsykb_find_xs0101.jsp'
        return baseUrl+f'?xnxq01id={term}'

    def findallStu(self, keyWords) -> list:
        stuList = []
        for item in reversed(self.stu_data):
            if item['xm'] == keyWords or item['xh'] == keyWords:
                user = self.getStuInfo(item['xh'])
                stuList.append(user)
        return stuList

    def getStuInfo(self, stuId:str) -> tuple:
        baseUrl = 'https://app.its.csu.edu.cn/csu-app/cgi-bin/privateadbook?method=queryUser'
        url = f'{baseUrl}&userName={stuId}'
        resp = requests.get(url)
        data = resp.json()
        name = data['data'][0]['userName']
        dept = data['data'][0]['dept']
        className = data['data'][0]['className']
        resp.close()
        #姓名 学号 学院 专业班级
        return (0, name, stuId, dept, className)

    def downloadData(self, param) -> list:
        classData = []
        url = 'http://csujwc.its.csu.edu.cn/jiaowu/pkgl/llsykb/llsykb_kb.jsp'
        resp = requests.post(url, data=param)
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')
        bzdiv = soup.find('div', id='bzdiv')
        kbtable = soup.find('table', id="kbtable")
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
                        teacher = kbsoup.find('font', title="老师").text
                        tem1 = kbsoup.find('font', title="周次").text
                        tem2 = kbsoup.find('font', title="单双周").text
                        allWeek = f'{tem1}({tem2})'
                        eachWeek = f'星期{column}'
                        dayTime = f'{row * 2 - 1}-{row * 2}节'
                        try:
                            location = kbsoup.find('font', title="上课地点教室").text
                        except:
                            location = ' '
                        allWeek_pop = allWeek.replace('(', '').replace(')', '')
                        className = kbsoup.find('a').text.replace(teacher, '').replace(allWeek_pop, '').replace(
                            location, '')
                        data = {'className': className, 'teacher': teacher, 'allWeek': allWeek, 'eachWeek': eachWeek,
                                'dayTime': dayTime, 'location': location}
                        classData.append(data)
                        # print(className, teacher, allWeek, eachWeek, dayTime, location, '\n')
        data = {'bztext': bzdiv.text}
        classData.append(data)
        resp.close()
        return classData

    def getStuNames(self) -> set:
        names = set()
        for each in self.stu_data:
            names.add(each['xm'])
        return names