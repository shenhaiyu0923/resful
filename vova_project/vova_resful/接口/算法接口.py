import requests
import pprint
from time import sleep,ctime
import threading

def ft310225():
    headers={
        "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001) [,1b8ba1836067773c,1571715392822-1921536911056350291] lq-App Vova 2.48.1 android",
         "Content-Type":"application/json",
         "charset":"utf-8"
             }
    # params={
    #     "device_id":"ZWE2MzI3NWJjMGUwNWE3OGFiYmM4ZGJkZjdlMmQwYmRfY2FjZTg4NzM0YTdkZDk3OWJiMTlkMmI5ODU2MGFhMTU=",#########
    #
    # }
    data={
        "device_id": "1b8ba1836067773c",
        "ip_country_code": "FR",
        "timezone": "Europe/Tirane",
        "network_country_code": "FR",
        "order_country_code": "FR",
        "sys_country_code": "FR",
        "sys_lang": "fr"
    }
    r=requests.post('http://api-p.vova.com/rec-region/region-predict',headers=headers,
                   data=data)
    pprint.pprint(r.json())

if __name__=='__main__':
    ft310225()


