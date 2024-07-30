dict = {}
for x in range(5):
    nome = input('Nome: ')
    preco = float(input('Preço: '))
    dict.update({nome: preco})
print(dict)