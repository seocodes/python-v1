nome = str(input('Nome > '))
idade = int(input('\nIdade > '))

if idade < 16:
    print(f'{nome} é não votante.')
if 18 <= idade <= 65:
    print(f'{nome} possui voto obrigatório!')
if 16 <= idade <= 17 or idade > 65:
    print(f'{nome} possui voto facultativo.')