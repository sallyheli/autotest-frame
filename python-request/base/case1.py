import unittest

class testStr(unittest.TestCase):
	"""docstring for ClassName"""
	# def __init__(self):
	# 	pass
	# 	#self.arg = arg

	def test_isUpper(self):
		str = "Abc"
		self.assertTrue(str.isupper())
