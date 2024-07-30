votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

total_votantes = int(input("Informe o número total de votantes: "))

for i in range(total_votantes):
    voto = int(input(f"Informe o voto do votante {i+1} (1, 2 ou 3): "))
    if voto < 1 or voto > 3:
        voto = int(input("Voto inválido. Informe novamente (1, 2 ou 3): "))
        continue
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    else:
        votos_candidato3 += 1

print("\nResultado da eleição:")
print(f"Candidato 1: {votos_candidato1} votos")
print(f"Candidato 2: {votos_candidato2} votos")
print(f"Candidato 3: {votos_candidato3} votos")