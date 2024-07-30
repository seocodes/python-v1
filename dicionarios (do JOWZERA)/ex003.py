dic = {}

for i in range(4):
    produto = input('nome do produto> ')
    preco = int(input('preco> '))
    dic[produto] = preco

for i, o in dic.items():
    print(f'{i} - R${o}')

