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
        "bill_expyear": "2025",
        "installments": "1",
        "is_save_card": "1",
        "order_sn":"04039bd796398975",
        "payment_code":"checkout",
        "req_time":"1577524864",
        "sign":"03b8010d85237e47aad43eaaa26d392a"
    }
    url='http://api-t2.vova.com/en/v1/payment?timezone=Asia%2FShanghai&access_token=MmE4ZDNhZDc0NTNmZmVlNWFjZGMzZWY5ZWQ3YjI3NDNfMDk0NmY4Yjc3YTAzMzJhOTIxNzlkNzNhNzIwM2M0MTk%3D&s=2&uid=16804705&imei=&imsi=&uuid=1b8ba1836067773c&other=zh%3BCN%3B0%3B%3B%3B%3B0%3BGMT%2B08%3A00%3B2&version=2.56.0&currency=USD&is_new_user=0&brand_country_code=CN&country_code=CN&req_time=1577523328&sign=865d74bf7c32326cb54a70582f9d56d8'
    r=requests.put(url,headers=headers,data=data)
    pprint.pprint(r.json())
ft212281()