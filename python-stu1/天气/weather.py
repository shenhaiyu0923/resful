import sys
from PyQt5.QtWidgets import QWidget, QApplication, qApp
from PyQt5.QtCore import Qt
sys.path.append('F:/baidu/天气预报/天气预报/Ui_weather')
#from Ui_weather import Ui_Form
from query import *
import json#引用json模块













from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(599, 468)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(160, 140, 261, 141))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 70, 121, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(157, 314, 271, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close)
        self.pushButton.clicked.connect(Form.queryWeather)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Python高效编程-天气情况"))
        self.label.setText(_translate("Form", "城市天气查询"))
        self.label_2.setText(_translate("Form", "城市"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton_2.setText(_translate("Form", "退出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())











import requests
from json import JSONDecodeError

FILENAME = 'city_code.txt'


def read_code(filename=FILENAME):
    with open(filename, 'r') as f:
        city_code = json.load(f)
    return city_code


def query_code(table, city):
    '''
    table:字典
    city:字符串
    '''
    try:
        code = table[city]
    except KeyError:
        raise
    return code


def query_weather(code):
    html = f'http://wthrcdn.etouch.cn/weather_mini?citykey={code}'

    try:
        info = requests.get(html)
        info.encoding = 'utf-8'
    except requests.ConnectionError:
        raise

    try:
        info_json = info.json()
    except JSONDecodeError:
        return '无法查询'
    # 天气情况
    data = info_json['data']
    city = f"城市：{data['city']}\n"
    today = data['forecast'][0]
    date = f"日期：{today['date']}\n"
    now = f"实时温度：{data['wendu']}度\n"
    temperature = f"温度：{today['high']} {today['low']}\n"
    fengxiang = f"风向：{today['fengxiang']}\n"
    type = f"天气：{today['type']}\n"
    tips = f"贴士：{data['ganmao']}\n"

    return city + date + now + temperature + fengxiang + type + tips













class Weather(QWidget, Ui_Form):
    def __init__(self, parent=None):
        # 继承主窗口类
        super(Weather, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
 
    def initUi(self):
        # 维护一个城市代码字典
        self.table = read_code()
        # 将 textEdit 设置为只读模式
        self.textEdit.setReadOnly(True)
        # 将鼠标焦点放在 lineEdit 编辑栏里
        self.lineEdit.setFocus()

        
    def queryWeather(self):
        # 获取 lineEdit 中的文本
        city = self.lineEdit.text()
        err_msg = ''
        try:
            code = query_code(self.table,  city)
        except KeyError:
            err_msg = '请输入正确的城市名称'
        
        if not err_msg:
            try:
                info = query_weather(code)
            except requests.ConnectionError:
                err_msg = '请检查网络是否连接正确'
        
        if not err_msg:
            self.lineEdit.setFocus()
            # 设置文本
            self.textEdit.setText(info)
            # 清空文本
            self.lineEdit.clear()
            
        else:
            self.lineEdit.setFocus()
            self.textEdit.setText(err_msg)
            self.lineEdit.clear()
            
            
    def keyPressEvent(self, e):
        # 设置快捷键
        if e.key() == Qt.Key_Return:
                self.queryWeather()
 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather = Weather()
    weather.show()
    sys.exit(app.exec_())        
        
        
        
