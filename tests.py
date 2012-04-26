import unittest
import convert

class numberToLetterTests(unittest.TestCase):
	def test_0(self):
		self.assertTrue('A'== convert.numberToLetter(0))
	def test_1(self):
		self.assertTrue('B'== convert.numberToLetter(1))
	def test_24(self):
		self.assertTrue('Y'== convert.numberToLetter(24))
	def test_25(self):
		self.assertTrue('Z'== convert.numberToLetter(25))
	def test_26(self):
		self.assertTrue('AA'== convert.numberToLetter(26))
	def test_1381(self):
		self.assertTrue('BAD'== convert.numberToLetter(1381))

if __name__ == '__main__':
	unittest.main()
