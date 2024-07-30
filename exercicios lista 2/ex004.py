nome = str(input('Type your name:\n'))
med = float(input('Digite sua média final:\n'))
if med < 5:
    print('Reprovado newba.')
elif med >= 5 and med < 7:
    print('Em recuperação')
else:
    print('Aprovado.')