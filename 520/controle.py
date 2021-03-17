#!/usr/bin/python

cont = 0
while cont < 10:
    print('Execução {}'.format(cont))
    if cont == 5:
        print('interrompendo o loop com break')
        break
    cont += 1
