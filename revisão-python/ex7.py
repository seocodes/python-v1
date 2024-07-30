peso = float(input('Peso > '))
altura = float(input('Altura em metros: '))

imc = peso/(altura**2)

if imc < 18.5:
    print('Abaixo do peso\n')
elif 18.5 <= imc <= 25:
    print('Peso normal\n')
elif 25 < imc <= 30:
    print('Acima do peso\n')
elif imc > 30:
    print('Obeso')