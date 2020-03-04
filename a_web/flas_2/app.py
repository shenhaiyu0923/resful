
# 导入Flask类
from flask import Flask
import json
#Flask类接收一个参数__name__
#app = Flask(__name__)
app = Flask(__name__, static_url_path='/s')
#app = Flask(__name__, static_url_path='/s', static_folder='ss')
# 装饰器的作用是将路由映射到视图函数index
@app.route('/')
def route_map():
    """
    主视图，返回所有视图网址
    """
    rules_iterator = app.url_map.iter_rules()
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})

# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run(host="192.168.199.210", port=3000, debug = True)
