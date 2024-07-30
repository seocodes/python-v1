nome = str(input('Nome: '))
idade = int(input('\n Idade: '))
peso = float(input('\n Peso: '))

if idade >= 0 and idade < 16:
    print(f'{nome} não pode ser doador pois está abaixo da idade permitida.\n')
elif 16 <= idade < 18 and peso > 55:
    print(f'{nome} pode ser doador com autorização dos responsáveis.\n')
elif 18 <= idade <= 69 and peso > 60:
    print(f'{nome} pode ser doador.\n')
else:
    print(f'{nome} não pode ser doador por não atingir a idade permitida e/ou não ter o peso necessário.\n')
