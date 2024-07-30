D = {}
while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    D.update({nome: idade})
    op = input('Deseja continuar?\n').lower()
    if op == 'n':
        break
print(D)