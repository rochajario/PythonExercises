#!/opt/rh/rh-python36/root/usr/bin/python3
#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
#(1-Domingo, 2- Segunda, etc.), 
#se digitar outro valor deve aparecer valor inválido. 
validador=int(0)
while validador ==0:
	num=int(input("Digite um número pelo dia da semana desejado: "))
	if num>0 and num<8:
		if num == 1:
			print("Domingo")
			validador=(1)
		elif num ==2:
			print("Segunda-Feira")
			validador=(1)
		elif num ==3:
			print("Terça-Feira")
			validador=(1)
		elif num ==4:
			print("Quarta-Feira")
			validador=(1)
		elif num ==5:
			print("Quinta-Feira")
			validador=(1)
		elif num ==6:
			print("Sexta-Feira")
			validador=(1)
		elif num ==7:
			print("Sábado")
			validador=(1)
	else:
		print ("Não reconheci o dígito, pode tentar novamente?")
