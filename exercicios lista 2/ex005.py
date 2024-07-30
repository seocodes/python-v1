idade = int(input('Qual sua idade?\n'))
if idade == 0 and idade <= 3:
    print('Bebê')
elif idade >= 4 and idade <= 11:
    print('Criança')
elif idade >= 12 and idade <= 17:
    print('AAdolescente')
elif idade >= 18 and idade <= 60:
    print('Adulto')
elif idade >= 61 and idade <= 100:
    print('Idoso')
else:
    print('Ou tu é velho pa caralho ou tu tá mentindo.')