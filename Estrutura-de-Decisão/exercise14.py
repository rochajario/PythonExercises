#!/opt/rh/rh-python36/root/usr/bin/python3

#Faça um programa que lê as duas notas parciais obtidas por um aluno 
#numa disciplina ao longo de um semestre, e calcule a sua média. 
#A atribuição de conceitos obedece à tabela abaixo:

notaA=float(input("Digite a primeira nota parcial: "))
notaB=float(input("Digite a segunda nota parcial: "))
media=float((notaA+notaB)/2)

# Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E

if media>=9 and media<=10:
	print("Primeira nota parcial:",notaA,"\nSegunda nota parcial:",notaB,"\nConceito A\nAPROVADO")
elif media>=7.5 and media<9:
	print("Primeira nota parcial:",notaA,"\nSegunda nota parcial:",notaB,"\nConceito B\nAPROVADO")
elif media>=6 and media<7.5:
	print("Primeira nota parcial:",notaA,"\nSegunda nota parcial:",notaB,"\nConceito C\nAPROVADO")
elif media>=4 and media<6:
	print("Primeira nota parcial:",notaA,"\nSegunda nota parcial:",notaB,"\nConceito D\nREPROVADO")
elif media>=0 and media<4:
	print("Primeira nota parcial:",notaA,"\nSegunda nota parcial:",notaB,"\nConceito E\nREPROVADO")

#O algoritmo deve mostrar na tela as notas, a média, 
#o conceito correspondente e a mensagem APROVADO se o conceito for A, B ou C 
#ou REPROVADO se o conceito for D ou E.  
