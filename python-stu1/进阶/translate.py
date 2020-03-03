
# 导入标准库
from tkinter import *
import requests
import json
import pyttsx3
def translate():
    # 获取到输入的内容
    content = input_entry.get()
#   根据内容去翻译
#   爬虫的本质  ->  就是模拟浏览器去抓取互联网的信息结果
#   你伪装成一个人,去别人那里借东西
# 大量的伪装手段
# 第一:你要找谁借 url 统一资源定位符 确定目标   隔壁老王借锤子 地址
# 第二:去借到东西 所有的相应结果       工具箱
# 第三:把你想要的东西弄到手 选取你想要的信息  取出你的锤子
# 第四:加以利用               加一利用

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 准备发送的数据
    data = {
        'i':content,
        'doctype':'json'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    # 发送请求,获取结果
    response = requests.post(url,data=data,headers=headers)
    # 转码
    # response.text()
    # 得到请求结果
    ret = response.content.decode()
    # print(ret)
    # 转成python能看懂的
    result = json.loads(ret)
    print(result)
    result_data  = result['translateResult'][0][0]['tgt']#获取翻译后的内容
    print(result_data)
    # 在输入框当中显示
    res.set(result_data)
    engine = pyttsx3.init()
    engine.say(result_data)
    engine.runAndWait()
# 反爬措施- header头  加
# 看你爬取频率 ->反爬  频率
# 666
# 创建了可视化的界面
root = Tk()
# 让界面显示在中间 此处有坑,前方绕行
root.geometry('300x100+500+200')
# 来个标题
root.title('桌面智能翻译')
# 设值禁止调整大小
root.resizable(False,False)
# 创建一个标签
input_data = Label(root,text='输入内容',font=('黑体',18),fg='blue')
# 让标签显示  网格状布局
input_data.grid()
# 创建一个输入框
input_entry = Entry(root)
# 让标签显示  网格状布局
# 0 12
input_entry.grid(row=0,column=1)

# 创建一个标签
res_data = Label(root,text='输出结果',font=('黑体',18),fg='blue')
# 让标签显示  网格状布局
res_data.grid(row=1,column=0)
res = StringVar()
# 创建一个输入框
res_entry = Entry(root,textvariable=res)
# 让标签显示  网格状布局
# 0 12
res_entry.grid(row=1,column=1)
button = Button(root,text='翻译',width=10,command=translate)
# 点击按钮的时候,就自动调用函数
button.grid(row=2,column=0)
# 让界面显示  事件主循环
root.mainloop()
