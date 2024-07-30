a = 0
f = 0
m = 0
o = 0
for x in range (0, 100):
    nome = input('Digite seu nome:\n').title()
    cu = input('''Digite seu curso:
                   A - ARQUITETURA
                   F - FARMÁCIA
                   M - MEDICINA
                   O - ODONTOLOGIA:\n ''').upper()
    if cu != 'A' and cu != 'F' and cu != 'M' and cu != 'O':
        print('invalido')
        continue
    elif cu == 'A':
        a += 1
    elif cu == 'F':
        f += 1
    elif cu == 'M':
        m += 1
    elif cu == 'O':
        o += 1

print(f'Arquitetura: {a}, Farmácia: {f}, Odontologia: {o}, Medicina: {m}')
