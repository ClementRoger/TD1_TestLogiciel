import funcs
import unittest
import math

class TestFuncs(unittest.TestCase):

	def test_max_int(self):
		self.assertEqual( funcs.max_int(0 , 2) , 2 )
		self.assertEqual( funcs.max_int(-1 , -5) , -1 )
		self.assertEqual( funcs.max_int(-1 , 2) , 2 )
		self.assertEqual( funcs.max_int(0 , 0) , 0 )

	def test_min_int(self):
		self.assertEqual( funcs.min_int(0 , 2) , 0 )
		self.assertEqual( funcs.min_int(-1 , -5) , -5 )
		self.assertEqual( funcs.min_int(-1 , 2) , -1 )
		self.assertEqual( funcs.min_int(0 , 0) , 0 )

	def test_mean_list(self):
		self.assertEqual( funcs.mean_list( (2 , 2 , 2 , 2) ) , 2 )
		self.assertEqual( funcs.mean_list( (-1 , -5 , 5 , 1) ) , 0 )
		self.assertEqual( funcs.mean_list( (13 , 15 , 11 , 13 , 12 , 17) ) , 13.5 )
		self.assertEqual( funcs.mean_list( (50 , 45 , 55 , 43 , 46) ) , 47.8 )

	def test_median_list(self):
		self.assertEqual( funcs.median_list( (2 , 3 , 4 , 5 , 6) ) , 4 )
		self.assertEqual( funcs.median_list( (-1 , -5 , 5 , 1) ) , 0 )
		self.assertEqual( funcs.median_list( (13 , 15 , 11 , 13 , 12 , 17) ) , 13 )
		self.assertEqual( funcs.median_list( () ) , None )

	def test_std_list(self):	
		self.assertEqual( funcs.std_list( (1 , 1 , 1 , 1 , 1) ) , 0 )
		self.assertEqual( funcs.std_list( (6 , 2 , 3 , 1) ) , math.sqrt(3.5) )
		self.assertEqual( funcs.std_list( (12 , 14 , 9 , 12 , 11 , 14 , 8 , 16) ) , 2.5 )
		self.assertEqual( funcs.std_list( () ) , None )
			
if __name__ == '__main__':
	unittest.main()