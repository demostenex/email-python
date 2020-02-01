#!/usr/bin/python
# -*- coding: latin-1 -*-
# Importa o modulo de conexao com o mysql
from pprint import pprint
import MySQLdb

class DataConn:
	def __init__(self, host, user, passwd, db):
		
		self.host=host
		self.user=user
		self.passwd=passwd
		self.db=db

	def conn(self,query):
		conn=MySQLdb.connect(
			host=self.host, 
			user=self.user, 
			password=self.passwd, 
			db=self.db
			)
		cursor = conn.cursor()
		result = cursor.execute(query)
		return cursor
		#for (name, email) in cursor:
		#	print("{}, {}".format(name, email))
#cursor=conn.cursor()
#cursor.execute("SELECT * FROM dg_print.users")

#for (name, email, created_at) in cursor:
#	print("{}, {} was hired on {:%d %b %Y}".format(
#    name, email, created_at))

#cursor.close()
#conn.close()
if __name__ == '__main__':
	db = DataConn('192.168.2.250', 'root', 'dgdg4194','dg_print')

	#cursor=db.cursor()
	result = db.conn("SELECT name, email FROM dg_print.users")
	#print (result)
	for (name, email) in result:
		print("{}, {}".format(name, email))