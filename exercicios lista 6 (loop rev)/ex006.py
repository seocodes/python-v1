alunor = 0
alunoa = 0
count = 0
while count < 50:
    nome = input('Teu nome?\n').title()
    media = int(input('Digite tua media\n'))
    if media <= 0 or media >= 10:
        print('INVALIDO')
        continue
    elif media >= 7:
        alunoa = alunoa + 1
    elif media < 7:
        alunor = alunor + 1
    count += 1

print(f'APROVADOS: {alunoa}, REPROVADOS: {alunor}')