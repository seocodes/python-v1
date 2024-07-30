litros = float(input("Informe o número de litros vendidos: "))
tipo_combustivel = input("Informe o tipo de combustível (A - álcool, G - gasolina): ").upper()

if tipo_combustivel == "A":  #alcool
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor_total = litros * 4.22
    valor_pago = valor_total - (valor_total*desconto)
elif tipo_combustivel == "G":  #gasosa
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor_total = litros * 5.65
    valor_pago = valor_total - (valor_total*desconto)
else:
    print("Tipo de combustível inválido!")

print(f"Valor a ser pago: R$ {valor_pago:.2f}")