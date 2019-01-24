import requests
import json

class runRequest:
    def __init__(self):
        res = requests.post(url="http://www.baidu.com", data=None)

    def send_post(self,url,data,header=None,cookies=None):
        res = requests.post(url=url, data=data,headers=header,cookies=cookies)
        return res
        #return json.dumps(res, indent = 2, sort_keys = True)

    def send_get(self,url,data,header=None,cookies=None):
        res = requests.get(url=url, data=data,headers=header,cookies=cookies)
        return res
        #return json.dumps(res, indent = 2, sort_keys = True)

    def run_main(self,url,data,method="GET"):
        res = None
        #print(method)
        if str(method).upper() == "GET":
            res = self.send_get(url,data)
        elif str(method).upper() == "POST":
            res = self.send_post(url, data)
        return res

import sys
sys.path.append("../data_manager")
from data_manager.parse_json import *

if __name__ == "__main__":
    url = "https://order.imooc.com/pay/buynow"
    data = {
        "type_id": "299",
        "type": "1"
    }
    userFeedback = {
        "fankuicont": "aa",
        "ptype": "hp",
        "qq": "",
        "email": "",
        "fr": "fb",
        "fbtype": "0",
        "refer": "https://cn.bing.com/",
        "localtime": "1547384681958",
        "mosmv": "2_1_1_1.491.444,_2.490.306,",
        "screen": "docu_1280_150,page_1280_765,screen_1280_800,avail_1280_731",
        "mosmv3": "2"
        }
    #jsonParam = parseJsonData()
    #name = "userFeback"
    #data = jsonParam.getData(name)
    loginurl = "http://m.imooc.com/passport/user/login"
    data = {
        "username":"18513199586",
        "pqssword":"111111",
        "verify":"",
        "referer":"https://m.imooc.com"
    }
    res = requests.post(url,data).json()
    #res = runRequest().run_main(url,data,"get")
    print(res)
