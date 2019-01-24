#coding:utf-8
import sys
sys.path.append("./base")
from request_method import *
from data_manager.data_access import *

caseList = []
def geneteCase():
	header='''
#coding:utf-8
import sys
sys.path.append("./base")
from request_method import *
import time
import unittest
from data_manager.data_access import *

class testCaseManager(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		print("全部用例执行前执行")
		self.request = runRequest()
		self.data = dataAccess()

	@classmethod
	def tearDownClass(self):
		print("全部用例执行完毕执行")

	def setUp(self):
		print("每个用例执行前执行")


	def tearDown(self):
		print('例执行完执行')
'''
	data = dataAccess()
	row = data.get_row()
	with open("./caseUnittest.py",mode='w') as fp:
		fp.write(header)
		for i in range(1,row):
			is_run = data.get_is_run(i)
			if is_run == "Y":
				caseList.append("test_case%d" %i)
				caseContent = '''
	def test_case%d(self):
		case_id = self.data.get_case_id(%d)
		url = self.data.get_case_url(%d)
		url_data = self.data.get_case_data(%d)
		expectData = self.data.get_expect_data(%d)
		request_method = self.data.get_run_method(%d)
		res = self.request.run_main(url, url_data, request_method)
		self.assertEqual(expectData,res.status_code, "测试成功")
		print(case_id.encode("ascii") + ":" + str(res))\n''' %(i,i,i,i,i,i)
				fp.write(caseContent)

def generateCaseSuit():
	content =""
	header = '''
from report.HTMLTestRunner import *
from case_manage.caseUnittest import *

if __name__ == "__main__":
	suit = unittest.TestSuite()
	'''
	for item in caseList:
		content += '''
	suit.addTest(testCaseManager("%s"))'''%item

	tail = '''
	with open("../report/testResult.html", mode='w') as fp:
		HTMLTestRunner(fp).run(suit)
	#unittest.TextTestRunner().run(suit)'''

	with open("./run_case1.py", mode='w') as fp:
		fp.write(header)
		fp.write(content)
		fp.write(tail)

if __name__ == "__main__":
	geneteCase()
	generateCaseSuit()
