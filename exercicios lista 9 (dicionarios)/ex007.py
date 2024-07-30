dict = {}
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    media = (n1+n2+n3)/3
    if media >=7:
        dict.update({nome: 'Aprovado'})
    if media < 7 and media >= 5:
        dict.update({nome: 'Recuperação'})
    if media < 5:
        dict.update({nome: 'Reprovado'})
    op = input('Tu vai sair?\n').lower()
    if op == 's':
        break
print(dict)

