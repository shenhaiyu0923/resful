import requests
import pprint
from time import sleep,ctime
import threading

   
def ft310227():
    headers={"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001) [,1b8ba1836067773c,1571715392822-1921536911056350291] lq-App Vova 2.48.1 android"}
    url1="http://api-t.vova.com/en/v2/activity/ranking_list/rankingPlist?ranking_id=411&cat_id=5907&ranking_type=top-rated&country_code=FR&is_open_notification=0&is_new_user=0&currency=EUR&version=2.52.0&other=zh%3BCN%3B0%3B%3B%3B%3B0%3BGMT%2B08%3A00%3B2&s=2&access_token=M2FjYTk5YTRiNDdhZThhNzE5ZjYzYTJhYmM1YTk2OWRfZTc0N2FjMzJmYzAyZWQ0NTZhZDJiMmVmZGFlZWI4NjA=&brand_country_code=FR&uuid=1b8ba1836067773c&lang=en&imsi=&uid=16804228&timezone=Asia%2FShanghai&rn_module_name=rankinglist&rn_module_version=1.0.0&req_time=1576553155&sign=99b0d31051bcb78c8d14193d3864548e"
    url2="http://api-t.vova.com/en/v2/activity/ranking_list/rankingPlist?ranking_id=411&cat_id=5907&ranking_type=top-rated&country_code=FR&is_open_notification=0&is_new_user=0&currency=EUR&version=2.52.0&other=zh%3BCN%3B0%3B%3B%3B%3B0%3BGMT%2B08%3A00%3B2&s=2&access_token=M2FjYTk5YTRiNDdhZThhNzE5ZjYzYTJhYmM1YTk2OWRfZTc0N2FjMzJmYzAyZWQ0NTZhZDJiMmVmZGFlZWI4NjA=&brand_country_code=FR&uuid=1b8ba1836067773c&lang=en&imsi=&uid=16804228&timezone=Asia%2FShanghai&rn_module_name=rankinglist&rn_module_version=1.0.0&req_time=1576553256&sign=159d3b18dddd46d3232bff0bd16a3a74"

    r=requests.get(url2,headers=headers,)
    pprint.pprint(r.json())
ft310227()