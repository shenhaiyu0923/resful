# -*- coding: utf-8 -*-
import pprint
import requests
import warnings
warnings.filterwarnings("ignore")
class HttpsClient:

    def __init__(self):
        pass

    @staticmethod
    def get(_url, _json):
        _resp = requests.get(_url, _json)
        return _resp.content

    @staticmethod
    def https_post(_url, _json_dict,_headers):
        _resp = requests.post(_url, _json_dict,_headers, verify=False)
        return _resp.text

    @staticmethod
    def https_post_with_header(_url, _json_dict, _headers):
        _resp = requests.post(_url, data=_json_dict, headers=_headers, verify=False)
        return _resp.text


if __name__ == '__main__':
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}
    url = "https://cms-t3.vova.com.hk/index.php?q=admin/main/blacklistManagement/outBlacklist"
    json_dict={
            "act":"out_blacklist",
            "email_str":"t01221@163.com",
            "out_reasion":"test",
    }
    result = HttpsClient.https_post(url, json_dict,headers)
    pprint.pprint(result.json())