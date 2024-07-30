nome = input("Digite o nome do funcionário: ")
idade = int(input("Digite a idade do funcionário: "))
valor_plano = float(input("Digite o valor do plano de saúde: "))

if idade <= 18:
    aumento = 0.05
elif 19 <= idade <= 35:
    aumento = 0.10
elif 36 <= idade <= 60:
    aumento = 0.15
else:
    aumento = 0.20

novo_valor = valor_plano * (1 + aumento)

print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Valor do plano de saúde: R$ {valor_plano:.2f}")
print(f"Aumento: {aumento*100:.2f}%")
print(f"Novo valor a ser pago: R$ {novo_valor:.2f}")