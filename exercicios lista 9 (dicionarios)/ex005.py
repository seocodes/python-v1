dict = {}
for x in range(10):
    nome = input('Nome: ')
    telefone = input('Autor: ')
    dict.update({nome: telefone})
print(f'Amigões cadastrados: {dict}')