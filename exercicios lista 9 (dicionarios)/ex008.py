dict = {}
for x in range(2):
    nome = input('Nome: ')
    telefone = input('Tel: ')
    dict.update({nome: telefone})
print(f'Amigos cadastrados: {dict}')
add = input('Adicionar mais um amigo: ')
telefone = input('Tel: ')
dict.update({add: telefone})
print(dict)
