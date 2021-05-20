#!/usr/bin/python3

while True:
    try:
        x = int(input("Digite o primeiro numero: "))
        y = int(input("Digite o segundo numero: "))
        print (x + y)
    except Exception as e:
        print ("Digite apenas numeros")
    
