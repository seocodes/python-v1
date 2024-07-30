nts = []
for y in range(0,10):
    n1 = float(input('Digite sua primeira nota do bimestre:\n'))
    n2 = float(input('Digite sua segunda nota do bimestre:\n'))
    nts.append(n1)
    nts.append(n2)
    media = (n1+n2)/2
    print(f'Sua média foi de {media}')
print(f'Notas coletadas: {nts}')