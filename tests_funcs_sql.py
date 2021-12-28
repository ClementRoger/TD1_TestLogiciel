import funcs_sql
import unittest
import math
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users( username TEXT UNIQUE, password TEXT , spublickey TEXT , sprivatekey TEXT , epublickey TEXT , eprivatekey TEXT ) """)
conn.commit()

funcs_sql.add_user( cursor , "Bobby" , "motdepasse" , "abcde" , "fghij" , "klmno" , "pqrst" )
funcs_sql.add_user( cursor , "Bob" , "motdepasseresistant" , "key1" , "key2" , "key3" , "key4" )

class TestFuncs(unittest.TestCase):

	def test_add_user(self):
		self.assertEqual( cursor.execute("""SELECT * FROM users WHERE username="Bobby" """).fetchone() , ("Bobby" , "motdepasse" , "abcde" , "fghij" , "klmno" , "pqrst") )
		self.assertEqual( cursor.execute("""SELECT * FROM users WHERE password="motdepasse" """).fetchone() , ("Bobby" , "motdepasse" , "abcde" , "fghij" , "klmno" , "pqrst") )
		self.assertEqual( cursor.execute("""SELECT * FROM users WHERE spublickey="abcde" """).fetchone() , ("Bobby" , "motdepasse" , "abcde" , "fghij" , "klmno" , "pqrst") )
		self.assertEqual( cursor.execute("""SELECT * FROM users WHERE sprivatekey="fghij" """).fetchone() , ("Bobby" , "motdepasse" , "abcde" , "fghij" , "klmno" , "pqrst") )
		self.assertEqual( cursor.execute("""SELECT * FROM users WHERE epublickey="klmno" """).fetchone() , ("Bobby" , "motdepasse" , "abcde" , "fghij" , "klmno" , "pqrst") )
		self.assertEqual( cursor.execute("""SELECT * FROM users WHERE eprivatekey="pqrst" """).fetchone() , ("Bobby" , "motdepasse" , "abcde" , "fghij" , "klmno" , "pqrst") )
		self.assertEqual( cursor.execute("""SELECT * FROM users WHERE username="Bob" """).fetchone() , ("Bob" , "motdepasseresistant" , "key1" , "key2" , "key3" , "key4" ) )

	def test_check_password(self):
		self.assertEqual( funcs_sql.check_password( cursor , "Bobby" , "motdepasse" ) , True )
		self.assertEqual( funcs_sql.check_password( cursor , "Bobby" , "azertyuiop" ) , False )
		self.assertEqual( funcs_sql.check_password( cursor , "Bob" , "motdepasseresistant" ) , True )
		self.assertEqual( funcs_sql.check_password( cursor , "Bob" , "motdepassepasresistant" ) , False )

	def test_get_spublickey(self):
		self.assertEqual( funcs_sql.get_spublickey( cursor , "Bobby" ) , "abcde" )
		self.assertEqual( funcs_sql.get_spublickey( cursor , "Bob" ) , "key1" )

	def test_get_epublickey(self):
		self.assertEqual( funcs_sql.get_epublickey( cursor , "Bobby" ) , "klmno" )
		self.assertEqual( funcs_sql.get_epublickey( cursor , "Bob" ) , "key3" )

	def test_get_epublickey(self):
		self.assertEqual( funcs_sql.get_sprivatekey( cursor , "Bobby" ) , "fghij" )
		self.assertEqual( funcs_sql.get_sprivatekey( cursor , "Bob" ) , "key2" )

	def test_get_epprivatekey(self):
		self.assertEqual( funcs_sql.get_eprivatekey( cursor , "Bobby" ) , "pqrst" )
		self.assertEqual( funcs_sql.get_eprivatekey( cursor , "Bob" ) , "key4" )	


if __name__ == '__main__':
	unittest.main()
	db.close()
