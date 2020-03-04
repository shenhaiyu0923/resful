#coding:utf-8
import jsonpath
import json
import requests
from pprint import pprint

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
}
url="https://www.lagou.com/lbs/getAllCitySearchLabels.json"

response = requests.get(url,headers=headers)

dict_data = json.loads(response.content)
#pprint(dict_data)

city=jsonpath.jsonpath(dict_data,'$..A..name')#层级输出
city1=jsonpath.jsonpath(dict_data,'$..B..name')#层级输出

print(city)
print(city1)