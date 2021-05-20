#!/usr/bin/python3

nomes = ['daniel', 'maria', 'joao', 'pedro']
busca = input('Digite nome de uma pessoa: ')

for nome in nomes:
    if busca.lower().strip() == nome:
        print("Convidado está na lista")
        break
else:
    print("Não está na lista")
