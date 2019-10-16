#!/opt/rh/rh-python36/root/usr/bin/python3
#coding: utf-8
intA=int(input("Digite o valor do primeiro número inteiro: "))
intB=int(input("Digite o valor do segundo número inteiro: "))
floatA=float(input("Digite o valor do primeiro número real: "))

a=float((intA*2)+(intB/2))
print("O produto do dobro do primeiro com metade do segundo é: ",a)

b=float((intA*3)+floatA)
print("A soma do triplo do primeiro com o terceiro é: ",b)

c=float(floatA**3)
print("O terceiro elevado ao cubo: ",c)
