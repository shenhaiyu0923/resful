# 导入Flask类
from flask import Flask
class DefaultConfig(object):
    """默认配置"""
    #从配置对象中加载
    SECRET_KEY1 = 'peizhiwenjian1'
    SECRET_KEY2 = 'peizhiwenjian22'#被覆盖


class Prodection(DefaultConfig):
    """默认配置"""
    SECRET_KEY4 = 'peizhiwenjian4'#继承
    DEBUG = True
    host = "0.0.0.0"
    port = 5001

def create_flask_app(config):
    """
    创建Flask应用
    :param config: 配置对象
    :return: Flask应用
    """

    app = Flask(__name__)
    app.config.from_object(config)  # 配置对象加载

    # 从环境变量指向的配置文件中读取的配置信息会覆盖掉从配置对象中加载的同名参数
    app.config.from_envvar('PROJECT_SETTING',silent=True)#从环境变量加载
    return app



app = create_flask_app(Prodection)
@app.route("/")
def index():
    print(app.config['SECRET_KEY1'])
    print(app.config['SECRET_KEY2'])
    print(app.config['SECRET_KEY3'])
    print(app.config['DEBUG'])
    print(app.config['SECRET_KEY4'])
    return "hello world"
#
if __name__=="__main__":
    app.run(host="0.0.0.0", port=5001)

# export FLASK_APP=flas_4.py
# PROJECT_SETTING=setting.py
# flask run -h 0.0.0.0 -p 8000