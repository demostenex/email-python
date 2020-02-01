#!/usr/bin/python
from mydb import *
from bancos import *
import csv
class ameplan(DataConn):
	def __init__(self, host, user, passwd, db):
		DataConn.__init__(self, host, user, passwd, db) 
		 

	def mailing(self, txt):
		arquivo = open (txt, 'r')
		f = csv.reader(arquivo)
		bancos = Bancos(f)
		lala = bancos.cnab400itau()
		#lala = bancos.fatorVenc()
		bancos.limpaBanco()

		#print(lala)
'''
db = DataConn('192.168.2.250', 'root', 'dgdg4194','dg_print')

	#cursor=db.cursor()
result = db.conn("SELECT name, email FROM dg_print.users")
	#print (result)
for (name, email) in result:
	print("{}, {}".format(name, email))
'''