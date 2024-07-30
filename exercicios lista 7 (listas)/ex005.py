nums = []
pares = []
impar = []


for y in range(0,10):
    x = int(input('Digite um número:\n'))
    nums.append(x)
    if x % 2 == 0:
        pares.append(x)
    else:
        impar.append(x)
pares.sort(reverse=False)
impar.sort(reverse=False)
nums.sort(reverse=False)
print(f'A sua lista de números foi de: {nums}, a lista de pares foi de {pares}, e de ímpares, {impar}')
