alturas = []
sexos = []
soma_alturas_mulheres = 0
contador_mulheres = 0
contador_homens = 0

for i in range(50):
    altura = float(input(f"Informe a altura da pessoa {i+1}: "))
    sexo = input(f"Informe o sexo da pessoa {i+1} (M - masculino, F - feminino): ")
    alturas.append(altura)
    sexos.append(sexo)

    if sexo.upper() == "F":
        soma_alturas_mulheres += altura
        contador_mulheres += 1
    else:
        contador_homens += 1

media_altura_mulheres = soma_alturas_mulheres / contador_mulheres

porcentagem_homens = (contador_homens / 50) * 100
porcentagem_mulheres = (contador_mulheres / 50) * 100

print(f"Maior altura: {max(alturas):.2f}m")
print(f"Menor altura: {min(alturas):.2f}m")
print(f"Média de altura das mulheres: {media_altura_mulheres:.2f} m")
print(f"Número de homens: {contador_homens}")
print(f"Porcentagem de homens: {porcentagem_homens:.2f}%")
print(f"Porcentagem de mulheres: {porcentagem_mulheres:.2f}%")