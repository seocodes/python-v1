cri = 0
tub = 0
flor = 0

for x in range (0, 50):
    nome = input('Digite seu nome:\n').title()
    cidade = input('''Digite sua cidade:
                   C - Criciúma
                   T - Tubarão
                   F - Florianópolis:\n ''').upper()
    if cidade != 'T' and cidade != 'C' and cidade != 'F':
        print('INVÁLIDO')
        continue
    elif cidade == 'C':
        cri = cri + 1
    elif cidade == 'F':
        flor = flor + 1
    elif cidade == 'T':
        tub = tub + 1

print(f'Criciúma: {cri}, Tubarão: {tub}, Florianópolis: {flor}')