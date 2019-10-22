#!/opt/rh/rh-python36/root/usr/bin/python3
#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. 

#Verifica se o número é maior que 0 e menor que 1000
cond=int(0)
while cond==0:
numero=int(input("Digite um número inteiro menor que 1000: "))
	if (numero>0) and (numero<=1000):
		print("Número inválido. Tente novamente.")
	else:
		cond=1


