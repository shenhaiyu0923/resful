import requests

url = "http://www.baidu.com/"

proxies = {
    'http': 'http://58.220.95.54:9400',
}
response = requests.get(url,proxies=proxies)

print(response.text)