import requests


def yuan():
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0.1; VIVO X20 Build/V417IR) [,340fee311994e386,1584001783790-5090209472900175219] lq-App Vova 2.65.0 android",
    }
    params = {
        "timezone": "Asia/Shanghai",
        "access_token": "",
        "s": "2",
        "uid": "0",
        "imei": "540000000045036",
        "imsi": "46007",
        "uuid": "340fee311994e386",
        "other": ";;0;46007;;;1;GMT+08:00;1;0",
        "version": "2.65.0",
        "currency": "EUR",
        "is_new_user": "0",
        "brand_country_code": "CN",
        "country_code": "FR",
        "req_time": "1584084992",
        "sign": "b4a3aa750973b8a1b203c54f68a0be93"
    }
    data = {
        "from_page": "homepage_category",
        "goods_number": "1",
        "req_time": "1584084992",
        "sign": "865c1768b79eb488b6a103f654be87bb",
        "sku_id": "72284803",
        "source": "goods_detail",
        "virtual_goods_id": "10252889"
    }

    url = "http://api.vova.com/en/v1/cart/"
    response = requests.post(url, headers=headers, params=params, data=data)
    retDict = response.json()
    print(retDict)
yuan()