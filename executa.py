#!/usr/bin/python
import os.path
import estudo

_dir = os.path.dirname(os.path.abspath(__file__))

#print(_dir)

host = '192.168.2.250'
user = 'root'
passwd = 'dgdg4194'
db = 'dg_print'

arquivo = _dir + '/SINTR05@A.rem'
caminho = ''
ameplan = estudo.ameplan(host, user, passwd, db)
texto = ameplan.mailing(arquivo)
