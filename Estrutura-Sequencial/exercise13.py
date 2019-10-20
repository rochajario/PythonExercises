#!/opt/rh/rh-python36/root/usr/bin/python3

#Tendo como dado de entrada a altura (h) de uma pessoa, 
#construa um algoritmo que calcule seu peso ideal, 
#utilizando as seguintes fórmulas:
h=float(input("Digite a sua altura: "))
flag=int(0)
while flag==0:
	sexo=str(input("Gênero: \nMasculino=M\nFeminido=F\n"))
	if(sexo=="M"):
		#  Para homens: (72.7*h) - 58
		homens=float((72.7*h)-58)
		print("O seu peso ideal é: ",homens)
		flag=1
	elif(sexo=="F"):
        	#  Para mulheres: (62.1*h) - 44.7
		mulheres=float((62.1*h)-44.7)
		print("O seu peso ideal é: ",mulheres)
		flag=1


