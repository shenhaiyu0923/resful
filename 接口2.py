import requests
import pprint
from time import sleep, ctime
import threading


def ztest_reg():  #
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001) [,1b8ba1836067773c,1578710372871-2164943907535087689] lq-App Vova 2.48.1 android"}
    params = {
        "uuid": "340fee311994e386",
        "sign": "70ce8258f4872cf7acee1e8d80aec1f6"
    }
    data = {

        "password": "96e79218965eb72c92a549dd5a330112",
        "sign": "f3f9b1d293415d1d2f1a9fd840f3ac04",
        "username": "t000003@163.com"
    }
    url = "http://api-t4.vova.com/en/v2/authentications"
    r = requests.post(url=url,
                      headers=headers,
                      params=params,
                      data=data,
                      )
    pprint.pprint(r.json())

if __name__ == '__main__':
    ztest_reg()