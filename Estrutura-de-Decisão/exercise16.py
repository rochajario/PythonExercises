#!/opt/rh/rh-python36/root/usr/bin/python3
import math
# Faça um programa que calcule as raízes de uma equação do segundo grau, 
# na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, 
# informando ao usuário nas seguintes situações:
run=int(0)
# a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo   #	grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

while run==0:
	a=float(input("Digite o valor de A: "))
	if a==0:
		print("Valor inválido! Digite outro número.")
	else:
		b=float(input("Digite o valor de B: "))
		c=float(input("Digite o valorde C: "))
# b) Se o delta calculado for negativo, a equação não possui raizes reais.
#    Informe ao usuário e encerre o programa; 	
		delta=((b*b)-4*(a*c))
		if delta < 0:
			print("A equação não possui raizes reais.")
			run=1
# c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; 
#    informe-a ao usuário; 
		elif delta == 0:
			print("Apenas uma raiz real.")
			run=1
# d) Se o delta for positivo, a equação possui duas raiz reais; 
#    informe-as ao usuário; 
		elif delta > 0:
			print("Duas raizes reais.")
			xA=float((-b+(math.sqrt(delta)))/2*a)
                	print (xA)
                	xB=float((-b-(math.sqrt(delta)))/2*a)
                	print (xB)
			run=1
