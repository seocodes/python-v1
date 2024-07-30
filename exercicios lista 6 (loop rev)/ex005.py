bosta = 0
foda = 0
mediano = 0

for x in range (100):
    salario = int(input('Digite seu salario:\n'))
    if salario < 1500:
        bosta += 1
    elif salario >= 1500 and salario <= 3500:
        mediano += 1
    elif salario > 3500:
        foda += 1
print(f'Os salários bosta tem: {bosta}, os mediano tem {mediano} e os foda tem {foda}')
