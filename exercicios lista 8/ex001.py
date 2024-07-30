nomes = []
saldo = []

while True:
    nome = input('Digite seu nome: \n').lower().title()
    sal = float(input('Digite seu saldo em conta: \n'))
    nomes.append(nome)
    saldo.append(sal) 
    op = input('Quer sair? Digite S para sair.\n').upper()
    if op == 'S':
        break

print('''    ----------------------------
    CLIENTE   |   SALDO (em R$)''')
for x in range (0, len(nomes)):
    print(f'''    {nomes[x]}             {saldo[x]} ''')
print('    ----------------------------')
print(f'A conta com maior saldo tem {max(saldo)}R$, e já a menor: {min(saldo)}R$.')


