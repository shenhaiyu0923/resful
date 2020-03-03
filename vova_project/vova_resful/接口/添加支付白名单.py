import requests
import pprint
import warnings
warnings.filterwarnings("ignore")

def pay_white():#支付白名单
    headers={
       # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400",
        "Cookie":"PHPSESSID=kpd04hfc6pispo5qqe26qvepa7; OKSID=f05b516b94b60f23393f4be90d3baaeb",
        "Authorization":"Basic bGViYmF5OnBhc3N3MHJk",
            }
    data={
            'act':'out_blacklist',
            'email_str':'t01221@163.com',
            'out_reason':'test'
    }
    url='https://cms-t3.vova.com.hk/index.php?q=admin/main/blacklistManagement/outBlacklist'
    r = requests.post(data=data, url=url,headers=headers, verify=False)
    pprint.pprint(r.json())

def pay_black():  # 支付白名单
    headers = {
        "Host":"cms-t3.vova.com.hk",
        "Content-Length":"124",
        "Cache-Control":"max-age=0",
        "Authorization": "Basic bGViYmF5OnBhc3N3MHJk",
        "Upgrade-Insecure-Requests":"1",
        "Content-Type":"application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer":"https://cms-t3.vova.com.hk/index.php?q=admin/main/blacklistManagement/addBlacklist",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie": "PHPSESSID=kpd04hfc6pispo5qqe26qvepa7; OKSID=f05b516b94b60f23393f4be90d3baaeb",
        "Connection":"keep-alive"
    }
    cookies={
        "PHPSESSID":"kpd04hfc6pispo5qqe26qvepa7",
        "OKSID":"f05b516b94b60f23393f4be90d3baaeb"
    }
    data = {
        'q':'admin/main/blacklistManagement/addBlacklist',
        'rule_type_id': '1',
        'black_type':'email',
        'add_black_data': 't01221@163.com',
        'comment': ''
    }
    url = 'https://cms-t3.vova.com.hk/index.php?q=admin/main/blacklistManagement/outBlacklist'
    r = requests.post(data=data, url=url, headers=headers,cookies=cookies, verify=False)
    pprint.pprint(r.text)



pay_white()
pay_black()








