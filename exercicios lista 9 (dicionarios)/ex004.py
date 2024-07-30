dict = {}
for x in range(10):
    nome = input('Nome: ')
    autor = input('Autor: ')
    dict.update({nome: autor})
print(f'Livros cadastrados: {dict}')