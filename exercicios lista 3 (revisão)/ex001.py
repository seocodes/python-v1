conversao = str(input('Você converterá para dólar ou para real?\n'))
dinheiro = float(input("Digite o valor que será convertido:\n"))
cotacao = 4.97

if conversao == 'dólar' or 'dolar':
    print(f'O valor recebido em real será de: {dinheiro/cotacao}')
elif conversao == 'real' or 'reais':
    print(f'O valor recebido em dólar será de: {dinheiro*cotacao}')

