
#coding:utf-8
import sys
sys.path.append("..")
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

	def test_case4(self):
		case_id = self.data.get_case_id(4)
		url = self.data.get_case_url(4)
		url_data = self.data.get_case_data(4)
		expectData = self.data.get_expect_data(4)
		request_method = self.data.get_run_method(4)
		res = self.request.run_main(url, url_data, request_method)
		self.assertEqual(expectData,res.status_code)
		print(case_id.encode("ascii") + ":" + str(res))

	def test_case5(self):
		case_id = self.data.get_case_id(5)
		url = self.data.get_case_url(5)
		url_data = self.data.get_case_data(5)
		expectData = self.data.get_expect_data(5)
		request_method = self.data.get_run_method(5)
		res = self.request.run_main(url, url_data, request_method)
		#self.assertEqual(expectData,res.status_code)
		print(case_id.encode("ascii") + ":" + str(res))

	def test_case6(self):
		case_id = self.data.get_case_id(6)
		url = self.data.get_case_url(6)
		url_data = self.data.get_case_data(6)
		expectData = self.data.get_expect_data(6)
		request_method = self.data.get_run_method(6)
		res = self.request.run_main(url, url_data, request_method)
		self.assertEqual(expectData,res.status_code)
		print(case_id.encode("ascii") + ":" + str(res))
