#!/usr/bin/python3

cont = 0
# while cont < 10:
while True:
    print('Execução {}'.format(cont))
    if cont == 50:
        print('interrompendo o loop com break')
        break
    cont += 1
