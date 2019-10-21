#!/opt/rh/rh-python36/root/usr/bin/python3

# Faça um Programa que peça um número correspondente a um determinado ano 
# e em seguida informe se este ano é ou não bissexto.

ano=int(input("Digite o ano: "))
if (ano%4 == 0):
	bissexto=str("sim")
else:
	bissexto=str("não")
print("O ano",ano,"é Bissexto? "+bissexto) 
