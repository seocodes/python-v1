cb = 0
cp = 0
cv = 0
for x in range(200):
    nome = input('Nome:\n').title()
    idade = int(input('Digite sua idade:\n'))
    if idade < 13 or idade > 100:
        print('inválido')
        continue
    elif idade >= 13 and idade <= 17:
        cb+=1
    elif idade >= 18 and idade <= 40:
        cp+=1
    elif idade > 40:
        cv+=1
print(f'Base: {cb}, Profissional: {cp}, Veteranos: {cv}')
