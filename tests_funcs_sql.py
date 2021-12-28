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

funcs_sql.add_user( cursor , "Alice" , "Motdepasse1!" , "a" * 128 , "b" * 128 , "c" * 128 , "d" * 128 )
funcs_sql.add_user( cursor , "Ali" , "Motdepasse1!" , "a" * 128 , "b" * 128 , "c" * 128 , "d" * 128 )
funcs_sql.add_user( cursor , "Ali3" , "Motdepasse1!" , "a" * 128 , "b" * 128 , "c" * 128 , "d" * 128 )
funcs_sql.add_user( cursor , "Ali!" , "Motdepasse1!" , "a" * 128 , "b" * 128 , "c" * 128 , "d" * 128 )
funcs_sql.add_user( cursor , "Charlie" , "Mot1!" , "a" * 128 , "b" * 128 , "c" * 128 , "d" * 128 )
funcs_sql.add_user( cursor , "Dennis" , "motdepasse1!" , "a" * 128 , "b" * 128 , "c" * 128 , "d" * 128 )
funcs_sql.add_user( cursor , "Emmy" , "Motdepasse!" , "a" * 128 , "b" * 128 , "c" * 128 , "d" * 128 )
funcs_sql.add_user( cursor , "Finn" , "Motdepasse1" , "a" * 128 , "b" * 128 , "c" * 128 , "d" * 128 )
funcs_sql.add_user( cursor , "George" , "M!!!!!1111111" , "a" * 128 , "b" * 128 , "c" * 128 , "d" * 128 )
funcs_sql.add_user( cursor , "Hal" , "Motdepasse1!" , "a" * 127 , "b" * 128 , "c" * 128 , "d" * 128 )
funcs_sql.add_user( cursor , "Isabel" , "Motdepasse1!" , "a" * 128 , "b" * 129 , "c" * 128 , "d" * 128 )
funcs_sql.add_user( cursor , "John" , "Motdepasse1!" , "a" * 128 , "b" * 128 , "c" , "d" * 128 )
funcs_sql.add_user( cursor , "Kelly" , "Motdepasse1!" , "a" * 128 , "b" * 128 , "c" * 128 , "key" )

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

	def test_is_database_corrupted(self):
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "Alice" ) , False ) #good
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "Ali" ) , True ) #Username length less than 4 characters
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "Ali3" ) , False ) #Good, digits accepted in username
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "Ali!" ) , True ) #Special characters not accepted in username
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "Charlie" ) , True ) #Password length less than 8 characters
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "Dennis" ) , True ) #Password contains no uppercase
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "Emmy" ) , True ) #Password contains no digit
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "Finn" ) , True ) #Password contains no special character
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "George" ) , True ) #Password contains no standard character
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "Hal" ) , True ) #Key1 isn't 128 characters long
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "Isabel" ) , True ) #Key2 isn't 128 characters long
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "John" ) , True ) #Key3 isn't 128 characters long
		self.assertEqual( funcs_sql.is_database_corrupted( cursor , "Kelly" ) , True ) #Key4 isn't 128 characters long

if __name__ == '__main__':
	unittest.main()
	db.close()
