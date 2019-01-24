#coding:utf-8
import json

class parseJsonData:
    '''解析JSON配置的接口参数'''
    def __init__(self):
        self.data = self._LoadJson()

    def _LoadJson(self):
        fname = "../data_config/data.json"
        try:
            with open(fname) as fp:
                data = json.load(fp)
            return data
        except Exception,e:
            raise e

    def getData(self, name):
        return self.data[name]

if __name__ == "__main__":
    jsonParam = parseJsonData()
    #jsonData = data.LoadJson()#
    name = "feedback"
    print(jsonParam.getData(name))