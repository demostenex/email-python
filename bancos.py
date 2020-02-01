#!/usr/bin/python
import csv
import datetime

class Bancos:
	def __init__(self, mailing):
		self.mailing = mailing
		self.devolve=[]
	
	def cnab400itau(self):
		for l in self.mailing:
			for a in l:
				nome, end, bairro, cidade = a[234:][:30], a[274:][:40], a[314:][:12], a[334:][:15]
				uf, agencia, conta_cor, dac_conta = a[349:][:2], a[17:][:4], a[23:][:5], a[28:][:1]
				nosso_num, carteira, data_mora, venc = a[62:][:8], a[83:][:3], a[385:][:6], a[120:][:6]
				valor_titulo, num_doc, cpf_cnpj, mora = a[129:][:10], a[110:][:10], a[220:][:14], a[161:][:12]
				if nome.strip() != '':
					self.devolve.append(
						{
						'nome': nome,  'end': end, 'bairro': bairro, 'cidade': cidade,
						'uf':uf, 'agencia': agencia, 'conta_cor': conta_cor, 'dac_conta': dac_conta,
						'nosso_num': nosso_num, 'carteira': carteira, 'data_mora': data_mora, 'venc': venc,
						'valor_titulo': valor_titulo, 'num_doc': num_doc, 'cpf_cnpj': cpf_cnpj, 'mora':mora
						})
		self.fatorVenc()
		self.dacNossoNum()
		self.barcodeItau()
		print(self.devolve)

	def barcodeItau(self):
		cod_banco = '341'
		cod_moeda = '9'
		result = []
		fator_mult = '4329876543298765432987654329876543298765432';
		for l in self.devolve:
			cod_bar = cod_banco+cod_moeda+l['fator_venc']+l['valor_titulo']+l['carteira']+l['nosso_num']+l['dac']+l['agencia']+l['conta_cor']+l['dac_conta']+'000'
			for x in range(43):
				result.append(int(cod_bar[x])*int(fator_mult[x]))
			Sum = sum(result)%11
			if Sum == 0:
				dac = 1
			elif Sum == 1:
				dac = 1
			elif Sum == 10:
				dac = 1
			elif Sum == 11:
				dac = 1
			else:
				dac = 11-Sum	
			l['dac_geral'] = dac
			dac_geral = str(dac)
			l['cod_barras'] = cod_banco+cod_moeda+dac_geral+l['fator_venc']+l['valor_titulo']+l['carteira']+l['nosso_num']+l['dac']+l['agencia']+l['conta_cor']+l['dac_conta']+'000'
		return self.devolve
	
	def fatorVenc(self):		
		for l in self.devolve:	
			ano, mes, dia = '20' + l['venc'][4:][:2], l['venc'][2:][:2], l['venc'][:2]
			if mes == '  ':
				dF = 0
			else: 
				d1, d2 = datetime.datetime.strptime('1997-10-07', '%Y-%m-%d'), datetime.datetime.strptime("{}-{}-{}".format(ano,dia,mes), '%Y-%m-%d') 
				dF = abs((d2 - d1).days)			
			l['fator_venc'] = str(dF)
		return self.devolve

	def dacNossoNum(self):
		fator = '12121212121212121212'
		result = []
		
		for l in self.devolve:
			cod = l['agencia']+l['conta_cor']+l['carteira']+l['nosso_num']
			for x in range(20):
				res = int(cod[x]) * int(fator[x])
				if len(str(res)) == 2:
					a = str(res)
					result.append(int(a[0]))
					result.append(int(a[1]))
				else:
					result.append(res)
			Sum = sum(result)%10
			if Sum == 0:
				dac  = 0
			else:	
				dac = 10-Sum

			l['dac'] = str(dac)
		return self.devolve
			
	def limpaBanco(self):
		self.devolve.clear()