#!/opt/rh/rh-python36/root/usr/bin/python3
#Faça um Programa que peça os 3 lados de um triângulo. 
#O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
triangulo=int(0)

while triangulo==0:
	ladoA=float(input("Digite o primeiro lado do Triângulo: "))
	ladoB=float(input("Digite o segundo lado do Triangulo: "))
	ladoC=float(input("Digite o terceiro lado do Triângulo: "))
#    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
	if ((ladoA+ladoB)>ladoC) and ((ladoB+ladoC)>ladoA) and ((ladoC+ladoA)>ladoB):
		triangulo=1
#    Triângulo Equilátero: três lados iguais;
		if (ladoA==ladoB) and (ladoB==ladoC):
			print("Triangulo Equilátero")
#    Triângulo Isósceles: quaisquer dois lados iguais;
		elif (ladoA==ladoB) or (ladoB==ladoC) or (ladoA==ladoC):
			print("Triângulo Isóceles")
#    Triângulo Escaleno: três lados diferentes; 
		elif (ladoA!=ladoB) and (ladoB!=ladoC) and (ladoC!=ladoA):
			print("Triângulo Escaleno")
	else:
		print("Não é triângulo")
