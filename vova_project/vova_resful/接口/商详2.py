'''

http://api-t2.vova.com/tw/v2/surface/detail?virtual_goods_id=1632818&from_page=&timezone=Asia%2FShanghai&access_token=Y2RhNDVjYjY4NmM0YjU0MTk1NWVhNDNlZTIyNjQ1NTdfMzRhYWQxMDMyNDhiMjViYmRlMGI5MjRjNTQzODRjMDY%3D&s=2&uid=16805551&imei=540000000045036&imsi=46007&uuid=340fee311994e386&other=zh%3BCN%3B0%3B46007%3B%3B%3B1%3BGMT%2B08%3A00%3B2%3B0&version=2.59.0&currency=EUR&is_new_user=0&brand_country_code=CN&country_code=FR&req_time=1578887424&sign=0818b97744c03335544a213d94b1508d
'''
import requests
from pprint import pprint
url='http://api-t2.vova.com/tw/v2/surface/detail?virtual_goods_id=1632818&from_page=&timezone=Asia%2FShanghai&access_token=Y2RhNDVjYjY4NmM0YjU0MTk1NWVhNDNlZTIyNjQ1NTdfMzRhYWQxMDMyNDhiMjViYmRlMGI5MjRjNTQzODRjMDY%3D&s=2&uid=16805551&imei=540000000045036&imsi=46007&uuid=340fee311994e386&other=zh%3BCN%3B0%3B46007%3B%3B%3B1%3BGMT%2B08%3A00%3B2%3B0&version=2.59.0&currency=EUR&is_new_user=0&brand_country_code=CN&country_code=FR&req_time=1578887424&sign=0818b97744c03335544a213d94b1508d'
def shangxaing():
    r=requests.get(url)
   # pprint(r.json())
    pprint(r.json()['code'])
    pprint(r.json()['data']['coupon_info']['coupon_config_list'])
shangxaing()