import requests
import pprint
from time import sleep,ctime
import threading

   
def ft212281():#过期信用卡支付
    headers={"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001) [,1b8ba1836067773c,1571715392822-1921536911056350291] lq-App Vova 2.48.1 android"}
    data={
        "bill_cardholder": "",
        "bill_cc": "4242424242424242",
        "bill_cvv": "100",
        "bill_expmonth": "06",
        "bill_expyear": "5df412e3b7799355bc0fc6aeba6c41c7",
        "installments": "1",
        "is_save_card": "1",
        "order_sn":"041f51e72c2be9cf",
        "payment_code":"checkout",
        "req_time":"1577760000",
        "sign":"d8016cd30be6a061e73f88f3107b59a4"
    }
    url='http://api-t2.vova.com/en/v1/payment?timezone=Asia%2FShanghai&access_token=MmE4ZDNhZDc0NTNmZmVlNWFjZGMzZWY5ZWQ3YjI3NDNfMDk0NmY4Yjc3YTAzMzJhOTIxNzlkNzNhNzIwM2M0MTk%3D&s=2&uid=16804705&imei=&imsi=&uuid=1b8ba1836067773c&other=zh%3BCN%3B0%3B%3B%3B%3B0%3BGMT%2B08%3A00%3B2&version=2.56.0&currency=USD&is_new_user=0&brand_country_code=CN&country_code=CN&req_time=1577523328&sign=865d74bf7c32326cb54a70582f9d56d8'
    r=requests.put(url,headers=headers,data=data)
    pprint.pprint(r.json())
ft212281()


#http://api-t.vova.com/en/v1/payment?timezone=Asia%2FShanghai&access_token=MmMzMWZhYWYxNzM4MDkwMDI0OWE0Y2NmMjAyY2E2YWJfOTAyMmM4YzIzN2U5NzgxNzQ0NWQ4MzkzYjhiNmExNWU%3D&s=2&uid=16804831&imei=&imsi=&uuid=1b8ba1836067773c&other=zh%3BCN%3B0%3B%3B%3B%3B0%3BGMT%2B08%3A00%3B2&version=2.57.0&currency=USD&is_new_user=0&brand_country_code=CN&country_code=CN&req_time=1577760000&sign=440e6fab7e33eac693e02b20d2dd3cb3