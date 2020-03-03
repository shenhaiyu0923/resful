# 导入Flask类
from flask import Flask
class DefaultConfig(object):
    """默认配置"""
    #从配置对象中加载
    SECRET_KEY1 = 'peizhiwenjian1'

app = Flask(__name__)
app.config.from_object(DefaultConfig)#配置对象加载

#app.config.from_pyfile('setting.py')#配置文件加载

app.config.from_envvar('PROJECT_SETTING',silent=True)#从环境变量加载

@app.route("/")
def index():
    print(app.config['SECRET_KEY1'])
    print(app.config['SECRET_KEY2'])
    print(app.config['SECRET_KEY3'])
    return "hello world"