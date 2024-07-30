prodName = str(input('Nome do produto: \n'))
qtd = int(input('Quantidade: \n'))
price = float(input('Preço: \n'))
total = qtd*price

print('''TIPO DE PAGAMENTO
      1 - DINHEIRO (10% DESC)
      2 - À VISTO CARTÃO DE CRÉDITO (5% DE DESC)
      3 - EM 2X (PREÇO NORMAL SEM JUROS)
      4 - EM 3X (PREÇO + 5%)''')

payType = int(input('\nTipo de pagamento:'))

if payType == 1:
    print(f'O total é de: {total-(total*0.1)}')
if payType == 2:
    print(f'O total será: {total-(total*0.05)}')
if payType == 3:
    print(f'O total será de: {total}, com 2 parcelas de {total/2:.2f}')
if payType == 4:
    print(f'O total será de {total+(total*0.05):.2f}, com 3 parcelas de {(total+(total*.05))/3:.2f}')
