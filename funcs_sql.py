import math
import sqlite3

def add_user( cursor , username , password , spublickey , sprivatekey , epublickey , eprivatekey ):

	cursor.execute( "INSERT INTO users(username , password , spublickey , sprivatekey , epublickey , eprivatekey) VALUES(?,?,?,?,?,?)""" , (username , password , spublickey , sprivatekey , epublickey , eprivatekey) )
