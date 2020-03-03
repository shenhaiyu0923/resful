import re  #导入正则表达式模块
pat='yue'#定义一个表达式
string='dgdfsgfshfghdfgianyuehfghd'
res=re.search(pat,string)  #从某个字符串中寻找符合规则的字符
print(res)
print("======================1========================")
pat1='\n'#定义一个表达式
string1='''dgdfsgfshfg
       hdfgianyuehfghd'''
res1=re.search(pat1,string1)  #从某个字符串中寻找符合规则的非打印字符
print(res1)
print("======================2========================")
'''
\w  字母，数字，下划线
\d  十进制数
\s 空白字符
\W  非\w以外的
\S  出了空白字符以外的任意字符
'''
pat2="\wbc\w"#定义一个表达式
string2="dgdfsfshaabcfgianyuehfghd"
res2=re.search(pat2,string2)  #从某个字符串中寻找符合规则的字符
print(res2)
print("======================3========================")
#原子表  [jian]   查找含有jian中任意一个字母的
pat3='pyth[jian]n'
string3='ffffffffpythjnffffff'
res3=re.search(pat3,string3)  #从某个字符串中寻找符合规则的字符
print(res3)
print("======================4========================")
#元字符
#具有特殊含义
#  .   可以匹配任意字符
#  ^   可以匹配字符串的开始位置
#   $   可以匹配字符串的结束位置
#   *  可以匹配  0次1次多次   前一个位置的字符
#   ？  可以匹配  0次或者一次   前一个位置的字符
#    +   可以匹配  一次或多次   前一个位置的字符
#   t{3}   前面的的原子t出现了三次
#   t{6，}前面的的原子t至少出现6次
#   t{6，7}前面的的原子t至少出现6次，至多7次
#   a|b  竖线  或， a或者b
#  （）  提取某一个内容
pat4='aab|sss'
string4='fffffaabfpythjnsssfff'
res4=re.search(pat4,string4)  #从某个字符串中寻找符合规则的字符
print(res4)
print("======================6========================")
#  模式修正符
'''
I   忽略大小写
M  多行匹配
L本地化识别匹配
U   unick字符
S   让.匹配
'''
pat5='sdsd'
string5='fffffSdsdfffffffff'
res5=re.search(pat5,string5,re.I)  #从某个字符串中寻找符合规则的字符
print(res5)
print("======================7========================")
#贪婪模式，懒惰模式

pat6='f.*f'  #贪婪模式
pat7='f.*?f'#懒惰模式
string6='dagfsdfgsfd'
res6=re.search(pat6,string6)  #从某个字符串中寻找符合规则的字符
res7=re.search(pat7,string6)
print(res6)
print(res7)


'''
#函数
re.search()  只能搜索到一个结果
re.match()   从字符串开始的地方开始搜索，开头处必须有

全局搜索函数：
re.compile().findall()

'''
pat8='py'
string8='pyfdsdfpydsfdpyfdspy'
res8=re.compile(pat8).findall(string8)
print(res8)


#实例

a="[a-zA-Z]+://[^\s]*[.com|.cn]"
b="<a href='http://www.baidu.com'>ssdsafa</a>"
c=re.compile(a).findall(b)
print(c)