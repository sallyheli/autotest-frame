
from report.HTMLTestRunner import *
from case_manage.caseUnittest import *

if __name__ == "__main__":
	suit = unittest.TestSuite()
	
	suit.addTest(testCaseManager("test_case4"))
	suit.addTest(testCaseManager("test_case5"))
	suit.addTest(testCaseManager("test_case6"))
	with open("../report/testResult.html", mode='w') as fp:
		HTMLTestRunner(fp).run(suit)
	#unittest.TextTestRunner().run(suit)