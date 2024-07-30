celsius = float(input('Temp. em celsius > '))

print('''TABELA DE CONVERSÕES
      1 - Fahrenheit
      2 - Kelvin
      3 -  Réaumur''')
op = int(input('Digite a opção escolhida > '))

if op == 1:
    print(f'A temperatura em Fahrenheit é de: {celsius*1.8+32}')
if op == 2:
    print(f'A temperatura em Kelvin é de: {celsius+273.15}')
if op == 3: 
    print(f'A temperatura em Réaumur é de: {celsius*0.8}')