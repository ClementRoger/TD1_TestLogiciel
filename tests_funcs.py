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

	def test_geometric_list(self):	
		self.assertEqual( funcs.is_geometric( (1 , 2 , 4 , 8 , 16) ) , True )
		self.assertEqual( funcs.is_geometric( (10 , 5 , 2.5 , 1.25) ) , True )
		self.assertEqual( funcs.is_geometric( (10 , -20 , 40 , -80, 160) ) , True )
		self.assertEqual( funcs.is_geometric( (10 , 3 , 7 , 2, -1 ) ) , False )
		self.assertEqual( funcs.is_geometric( (0 , 0 , 0 , 0 , 1 ) ) , False )
		self.assertEqual( funcs.is_geometric( (2 , 4 , 8 , 16 , 256 ) ) , False )
		self.assertEqual( funcs.is_geometric( (2 , 2 , 2 , 2 , 2 ) ) , True )	
		self.assertEqual( funcs.is_geometric( () ) , None )

	def test_arithmetic_list(self):	
		self.assertEqual( funcs.is_arithmetic( (1 , 2 , 3 , 4 , 5) ) , True )
		self.assertEqual( funcs.is_arithmetic( (10 , 5 , 2.5 , 1.25) ) , False )
		self.assertEqual( funcs.is_arithmetic( (10 , 7 , 4 , 1, -2) ) , True )
		self.assertEqual( funcs.is_arithmetic( (5 , 5 , 5 , 5, 5 ) ) , True )
		self.assertEqual( funcs.is_arithmetic( (0 , 0 , 0 , 0 , 1 ) ) , False )
		self.assertEqual( funcs.is_arithmetic( (1 , 2 , 3 , 5 , 8 ) ) , False )	
		self.assertEqual( funcs.is_arithmetic( () ) , None )

	def test_geometric_following(self):
		self.assertEqual( funcs.return_next_geometric_progression( (1 , 2 , 3 , 4 , 5) , 5) , False)
		self.assertEqual( funcs.return_next_geometric_progression( (1 , 2 , 4 , 8 , 16) , 3 ) , (True , [ 32 , 64 , 128 ] ))
		self.assertEqual( funcs.return_next_geometric_progression( (0 , 0 , 0 , 0 , 0) , 6 ) , (True , [ 0 , 0 , 0 , 0 , 0 , 0 ] ))
		self.assertEqual( funcs.return_next_geometric_progression( (243 , 81 , 27 , 9 , 3) , 0 ) , (True , [] ))
		self.assertEqual( funcs.return_next_geometric_progression( (243 , 81 , 27 , 9 , 3) , 3 ) , (True , [1 , 1/3 , 1/9] ))
		self.assertEqual( funcs.return_next_geometric_progression( (2 , -4 , 8 , -16 , 32) , 1 ) , (True , [-64] ))

	def test_arithmetic_following(self):
		self.assertEqual( funcs.return_next_arithmetic_progression( (1 , 2 , 3 , 4 , 5) , 5) , (True , [6 , 7 , 8 , 9 , 10] ))
		self.assertEqual( funcs.return_next_arithmetic_progression( (1 , 2 , 4 , 8 , 16) , 3 ) , False )
		self.assertEqual( funcs.return_next_arithmetic_progression( (0 , 0 , 0 , 0 , 0) , 6 ) , (True , [ 0 , 0 , 0 , 0 , 0 , 0 ] ))
		self.assertEqual( funcs.return_next_arithmetic_progression( (243 , 230 , 217 , 204 , 191) , 0 ) , (True , [] ))
		self.assertEqual( funcs.return_next_arithmetic_progression( (243 , 230 , 217 , 204 , 191) , 3 ) , (True , [178 , 165 , 152] ))
		self.assertEqual( funcs.return_next_arithmetic_progression( (2 , -4 , -10 , -16 , -22) , 1 ) , (True , [-28] ))
			
if __name__ == '__main__':
	unittest.main()