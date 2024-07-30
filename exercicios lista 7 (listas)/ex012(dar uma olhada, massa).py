v1 = []
v2 = []
v3 = []

for x in range(0,5):
    y = int(input('Digite um numero:\n'))
    v1.append(y)
    f = int(input('Digite números para outra lista:\n'))
    v2.append(f)
    v3.append(v1[x])
    v3.append(v2[x])
print(f'Lista 1 = {v1}\n')
print(f'Lista 2: {v2}\n')
print(f'Lista 3: {v3}\n')
