import requests
import json

date = {
	"username":"helili",
	"password":"111111"
}

class runRequest:
	def __init__(self):
		res = requests.post(url="http://www.baidu.com", data=None)

	def send_post(self,url,data):
		res = requests.post(url=url, data=data).json()
		return json.dumps(res, indent = 2, sort_keys = True)

	def send_get(self,url,data):
		res = requests.get(url=url, data=data).json()
		#return res
		return json.dumps(res, indent = 2, sort_keys = True)

if __name__ == '__main__':
	url = "http://127.0.0.1:8000/login/"
	data = {
		"username":"ssssss",
		"password":"123456"
	}
	run = runRequest()
	res= run.send_get(url,data)
	print(res)