nome = str(input('Digite seu nome: \n'))
idade = int(input('Digite sua idade: \n'))

if idade >= 0 and idade <= 2:
    nivel = 'Berçário'
elif idade>= 3 and idade <= 6:
    nivel = 'Ed. Infantil'
elif idade >= 7 and idade <= 10:
    nivel = 'Fundamental I'
elif idade >= 11 and idade <= 15:
    nivel = 'Fundamental II'
elif idade >= 16 and idade <= 18:
    nivel = 'Ensino Médio'
else:
    print('Inválido, tente inserir outra idade.\n')

print(f'{nome}, de {idade} ano(s) está no nível: {nivel}')