#coding:utf-8
import unittest
from reauestdemo import runRequest
from case1 import testStr
import HTMLTestRunner
import mockDemo

class TestMain(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		print("全部用例执行前执行")

	@classmethod
	def tearDownClass(self):
		print("全部用例执行完毕执行")

	def setUp(self):
		print("每个用例执行前执行")
		self.url = "http://127.0.0.1:8000/login/"
		self.data = {
		"username":"ssssss",
		"password":"123456"
		}
		self.run = runRequest()


	def tearDown(self):
		print('例执行完执行')

	
	def test_01(self):
		#test post
		res = self.run.send_post(self.url, self.data)
		#self.assertEqual(res['errorCode'],1001,"测试失败")
		#全局变量，可在多个case间共享，但注意case的执行顺序是按照字母排序的
		globals()['globalVar'] = 1009
		print("test_01")
		print(type(res))

	#@unittest.skip("test_02")
	def test_02(self):
		#test get
		#res = self.run.send_get(self.url,self.data)
		response_data ={
			"username":"test",
			"password":"123"
		}
		res = mockDemo.mockTest(self.url, self.data,response_data)
		print("test_02")
		print(res)
		print(globalVar)



if __name__ == '__main__':
	#unittest.main()
	#case 管理
	suit = unittest.TestSuite()
	suit.addTest(TestMain("test_01"))
	suit.addTest(TestMain("test_02"))
	suit.addTest(testStr("test_isUpper"))
	fp = open("./testResult.html","wb")
	runner = HTMLTestRunner.HTMLTestRunner(fp)
	runner.run(suit)
	#unittest.TextTestRunner().run(suit)
