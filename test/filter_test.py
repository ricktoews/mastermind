import sys
import unittest
sys.path.append('..')
import filter_perms

class TestPatternFilter(unittest.TestCase):

	def test_sample(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_filter_aabb(self):
		perms = filter_perms.filter_perms(1, 1, 'AABB')
		self.assertTrue('AABB' in perms)

	def test_filter_abba(self):
		perms = filter_perms.filter_perms(0, 3, 'BAAC')
		print perms
		self.assertTrue('ABBA' in perms)



if __name__ == '__main__':
	unittest.main()

