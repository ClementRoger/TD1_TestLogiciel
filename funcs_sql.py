import math
import sqlite3

def add_user( cursor , username , password , spublickey , sprivatekey , epublickey , eprivatekey ):
	cursor.execute( "INSERT INTO users(username , password , spublickey , sprivatekey , epublickey , eprivatekey) VALUES(?,?,?,?,?,?)""" , (username , password , spublickey , sprivatekey , epublickey , eprivatekey) )

def check_password( cursor , username , password ):
	return ( cursor.execute( """SELECT password FROM users WHERE username=?""" , (username,) ).fetchone() == (password,) )

def get_password( cursor , username ):
	return cursor.execute( """SELECT password FROM users WHERE username=?""" , (username,) ).fetchone()[0]

def get_spublickey( cursor , username ):
	return cursor.execute( """SELECT spublickey FROM users WHERE username=?""" , (username,) ).fetchone()[0]

def get_sprivatekey( cursor , username ):
	return cursor.execute( """SELECT sprivatekey FROM users WHERE username=?""" , (username,) ).fetchone()[0]

def get_epublickey( cursor , username ):
	return cursor.execute( """SELECT epublickey FROM users WHERE username=?""" , (username,) ).fetchone()[0]

def get_eprivatekey( cursor , username ):
	return cursor.execute( """SELECT eprivatekey FROM users WHERE username=?""" , (username,) ).fetchone()[0]

def is_database_corrupted( cursor , username ):

	if( len(username) < 4 ):
		return True

	for letter in username:
		if letter.isdecimal() or letter.isalpha():
			pass
		else:
			return True

	password = get_password( cursor , username )

	if( len(password) < 8 ):
		return True

	bool_maj = False
	bool_special_char = False
	bool_digit = False
	bool_std_char = False	

	for letter in password:
		if letter.isupper():
			bool_maj = True
		elif letter.isdecimal():
			bool_digit = True
		elif letter.islower():
			bool_std_char = True
		else:
			bool_special_char = True

	if	bool_special_char and bool_maj and bool_digit and bool_std_char:
		pass
	else:
		return True

	keyepu = get_epublickey( cursor , username )
	keyepr = get_eprivatekey( cursor , username )
	keyspu = get_spublickey( cursor , username )
	keyspr = get_sprivatekey( cursor , username )

	if len(keyepu) != 128 or len(keyepr) != 128 or len(keyspu) != 128 or len(keyspr) != 128:
		return True

	return False	 
								


