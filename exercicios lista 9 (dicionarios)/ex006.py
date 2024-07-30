dict = {}
for x in range(5):
    nome = input('Nome: ')
    preco = input('Preço: ')
    dict.update({nome: preco})
print(f'Produtos cadastrados: {dict}')