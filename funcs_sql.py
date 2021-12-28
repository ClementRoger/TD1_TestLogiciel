import math
import sqlite3

def add_user( cursor , username , password , spublickey , sprivatekey , epublickey , eprivatekey ):
	cursor.execute( "INSERT INTO users(username , password , spublickey , sprivatekey , epublickey , eprivatekey) VALUES(?,?,?,?,?,?)""" , (username , password , spublickey , sprivatekey , epublickey , eprivatekey) )

def check_password( cursor , username , password ):
	return ( cursor.execute( """SELECT password FROM users WHERE username=?""" , (username,) ).fetchone() == (password,) )

def get_spublickey( cursor , username ):
	return cursor.execute( """SELECT spublickey FROM users WHERE username=?""" , (username,) ).fetchone()[0]

def get_sprivatekey( cursor , username ):
	return cursor.execute( """SELECT sprivatekey FROM users WHERE username=?""" , (username,) ).fetchone()[0]

def get_epublickey( cursor , username ):
	return cursor.execute( """SELECT epublickey FROM users WHERE username=?""" , (username,) ).fetchone()[0]

def get_eprivatekey( cursor , username ):
	return cursor.execute( """SELECT eprivatekey FROM users WHERE username=?""" , (username,) ).fetchone()[0]			