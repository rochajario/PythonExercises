#!/opt/rh/rh-python36/root/usr/bin/python3
#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 

data=str(input("Digite uma data no seguinte formato dd/mm/aaaa: "))
if (data[2] == "/") and (data[5] == "/"):
	dia=int(data[0]+data[1])
	mes=int(data[3]+data[4])
	ano=int(data[6]+data[7]+data[8]+data[9])
	print("Formato de Data Validado")

#Valida Quantidade de Meses
	if mes > 0 and mes<=12:
		print("Mês Validado")
#Valida Ano-Bissexto
		if (ano%4==0) and mes==2:
			if dia > 0 and dia <=29:
				print("Dia Validado")
			else:
				print("Dia Inválido - Ano Bissexto")
		elif (mes==4) or (mes==6) or (mes==9) or (mes==11):
			if dia > 0 and dia <=30:
				print("Dia Validado")
			else:
				print("Dia Inválido - Mês com 30 dias")
		else:
			if dia > 0 and dia <=31:
				print("Dia Validado")
			else:
				print("Dia Inválido - Mês com 31 dias")
	else: 
		print("Mês Inválido")
else:
	print("Formato de Data Inválido")
