sexom = 0
sexof = 0
count = 0
while count < 10:
    nome = input('Teu nome?\n').title()
    sexo = input('Digite teu sexo (M ou F)\n').upper()
    if sexo != 'F' and sexo != 'M':
        print('INVALIDO')
        continue
    elif sexo == 'F':
        sexof = sexof + 1
    elif sexo == 'M':
        sexom = sexom + 1
    count += 1

print(f'MOLIERES: {sexof}, HOMENS:; {sexom}')
