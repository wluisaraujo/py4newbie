#!/usr/bin/python3

num = input('Digite um numero: ')

try:
    print(int(num) + 2)
except Exception:
    print('num não é um numero')
