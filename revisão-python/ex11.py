
cidades = [
    {"codigo": 1, "veiculos": 1500, "acidentes": 50},
    {"codigo": 2, "veiculos": 2500, "acidentes": 70},
    {"codigo": 3, "veiculos": 1800, "acidentes": 40},
    {"codigo": 4, "veiculos": 1200, "acidentes": 30},
    {"codigo": 5, "veiculos": 3000, "acidentes": 90}
]

maior_acidente = cidades[0]
menor_acidente = cidades[0]
#a. maior e menor indice
for cidade in cidades:
    if cidade["acidentes"] > maior_acidente["acidentes"]:
        maior_acidente = cidade
    if cidade["acidentes"] < menor_acidente["acidentes"]:
        menor_acidente = cidade

print(f"Maior índice de acidentes: {maior_acidente['acidentes']} na cidade {maior_acidente['codigo']}")
print(f"Menor índice de acidentes: {menor_acidente['acidentes']} na cidade {menor_acidente['codigo']}")

#média de veiculos nas cinco cidades
soma_veiculos = 0
for cidade in cidades:
    soma_veiculos += cidade["veiculos"]
media_veiculos = soma_veiculos / len(cidades)
print(f"Média de veículos: {media_veiculos:.2f}")

#média de acidentes nas cidades com menos de 2k veiculos
cidades_pequenas = []
soma_acidentes_pequenas = 0

for cidade in cidades:
    if cidade["veiculos"] < 2000:
        cidades_pequenas.append(cidade)
        soma_acidentes_pequenas += cidade["acidentes"]

if len(cidades_pequenas) > 0:
    media_acidentes_pequenas = soma_acidentes_pequenas / len(cidades_pequenas)
    print(f"Média de acidentes nas cidades com menos de 2.000 veículos: {media_acidentes_pequenas:.2f}")
else:
    print("Não há cidades com menos de 2.000 veículos")