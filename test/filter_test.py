import sys
import unittest
sys.path.append('..')
import filter_perms

class TestPatternFilter(unittest.TestCase):

	def test_sample(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_filter_exact1(self):
		perms = filter_perms.filter_perms(1, 0, 'AABB')
		self.assertTrue('ACCC' in perms)

	def test_filter_exact2(self):
		perms = filter_perms.filter_perms(2, 0, 'AABB')
		self.assertTrue('ACBC' in perms)

	def test_filter_exact3(self):
		perms = filter_perms.filter_perms(3, 0, 'AABB')
		self.assertTrue('ACBB' in perms)

	def test_filter_exact4(self):
		perms = filter_perms.filter_perms(4, 0, 'AABB')
		self.assertTrue('AABB' in perms)

	def test_filter_inexact1(self):
		perms = filter_perms.filter_perms(0, 1, 'BAAC')
		self.assertTrue('DBED' in perms)

	def test_filter_inexact2(self):
		perms = filter_perms.filter_perms(0, 2, 'BAAC')
		self.assertTrue('ABDD' in perms)

	def test_filter_inexact3(self):
		perms = filter_perms.filter_perms(0, 3, 'BAAC')
		self.assertTrue('ABDA' in perms)

	def test_filter_inexact4(self):
		perms = filter_perms.filter_perms(0, 4, 'BAAC')
		self.assertTrue('ABCA' in perms)

	def test_filter_mix1(self):
		perms = filter_perms.filter_perms(1, 1, 'BAAC')
		self.assertTrue('AADD' in perms)

	def test_filter_mix2(self):
		perms = filter_perms.filter_perms(2, 1, 'BAAC')
		self.assertTrue('BACD' in perms)

	def test_filter_mix3(self):
		perms = filter_perms.filter_perms(2, 2, 'BAAC')
		self.assertTrue('BACA' in perms)

	def test_filter_mix4(self):
		perms = filter_perms.filter_perms(1, 3, 'BDAC')
		self.assertTrue('BACD' in perms)



if __name__ == '__main__':
	unittest.main()

