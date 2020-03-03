
import requests,pprint
headers={
    "analyst_api":"true",
    "Accept":"application/json",
    "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001) [,1b8ba1836067773c,1571715392822-1921536911056350291] lq-App Vova android",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length":"211",
    "Host":"analyst-t.vova.com.hk",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip"
}
data="login_0%7Cvova%7Chttps%3A%2F%2Fapi-t3.vova.com%7C2%7C2.48.1%7C%7B%22imei%22%3A%22%22%2C%22android_id%22%3A%221b8ba1836067773c%22%7D%7C16800818%7Cen%7CCN%7CUSD%7C%7Ccom.vova.android%7Cvivo%20X21A%7Cmanual%7C"
r=requests.post('http://analyst-t.vova.com.hk/collector/login?timezone=Asia%2FShanghai&access_token=YWQ0MmIzOGJhMTc2ZTEwYTAzOWI4NDBjZmRjNzljZGRfMzY4NjEzY2M3Y2Q5MDI2NjNiNTllN2Y5OWJlNTY5ZDQ%3D&s=2&uid=16800818&imei=&imsi=46001&uuid=1b8ba1836067773c&other=zh%3BCN%3B0%3B46001%3B%3B%3B0%3BGMT%2B08%3A00%3B2&version=2.48.1&currency=USD&is_new_user=0&brand_country_code=CN&country_code=CN',headers=headers)

pprint.pprint(r)