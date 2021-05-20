#!/usr/bin/python3

while True:
    try:
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))
        print ( x + y )
    except Exception as e:
        print ("Digite apenas números")
