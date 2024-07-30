valor = float(input('Qual o valor da sua compra?'))
parcelas = int(input('Quantas parcelas serão feitas?'))
valorparcela = valor/parcelas

print(f'O valor de cada parcela de sua compra será de: {valorparcela}')

if valor <= 0 or parcelas <= 0: 
    print('Operação inválida.')