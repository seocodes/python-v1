totalvogais = 0
totalconsoantes = 0
espacos = 0
lista = []
frase = input("Digite uma frase: ").lower()

for i in range(len(frase)):
    lista.append(frase[i])
    valor = lista[i]
    if valor in ['a', 'e', 'i', 'o', 'u']:
        totalvogais = totalvogais + 1
    elif valor == ' ':
        espacos = espacos + 1
    else:
        totalconsoantes = totalconsoantes + 1

print(totalconsoantes, totalvogais, espacos)
