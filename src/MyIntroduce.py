from src.ui.introduce import Ui_Introduce
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt


class MyIntroduce(QDialog, Ui_Introduce):
    def __init__(self):
        super(MyIntroduce, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        html = "<h2 align='center'>用户须知</h2>" \
               "<h3 align='center'>本程序兼具查看自己课表和成绩、查询他人课表功能</h3>" \
               "<h3 align='center'>首次登录勾选记住密码之后 下次登录会有账号密码自动补全功能</h3>" \
               "<h3 align='center'>登录成功后首先是自己的课表界面</h3>" \
               "<h3 align='center'>此时可以导出课表为Excel表格</h3>" \
               "<h3 align='center'>也可以生成日程文件导入日历</h3>" \
               "<h3 align='center'>点击切换按键可以切换到查询他人课表的界面</h3>" \
               "<h3 align='center'>点击生成日程文件可以生成一个ics文件</h3>" \
               "<h3 align='center'>把此文件发送到手机用日历打开即可导入</h3>" \
               "<h3 align='center'>目前可完整无误导入的系统有</h3>" \
               "<h3 align='center'>小米的MIUI系统</h3>" \
               "<h3 align='center'>华为的EMUI系统、MagicUI系统、HarmonyOS</h3>" \
               "<h3 align='center'>IOS系统</h3>" \
               "<h3 align='center'>其它系统若出现导入的日程时间不对  或提醒时间不是提前20分钟</h3>" \
               "<h3 align='center'>或其它非正常情况  或程序异常崩溃" \
               "<h3 align='center'>请及时反馈至开发者QQ：3236877923</h3></h3>" \
               "<h3 align='center'>谢谢使用！</h3>"
        self.setContent(html)

    def setContent(self, html: str) -> None:
        self.introduce.setHtml(html)

    def on_buttonOK_released(self):
        self.close()