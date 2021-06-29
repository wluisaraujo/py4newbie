#!/usr/bin/python3

produtos = [
    {'nome': 'produto1', 'valor':1.0},
    {'nome': 'produto2', 'valor':2.0},
    {'nome': 'produto3', 'valor':3.0},
    {'nome': 'produto4', 'valor':4.0},
]

try:
    for produto in produtos:
        produto['valor'] += produto['valor'] * 0.1
        print(produto)
        print()
except KeyError as e:
    print('Chave não pertence ao produto: {}'.format(e))
    print('Erro: {}'.format(e))
except Exception:
    pass
finally:
    print(produtos)
