#!/usr/bin/python3

aux = True
x = 1
while aux:
    print('Executando {}'.format(x))
    if x == 100:
        aux = False
    x += 1

print('fim do bloco while')
