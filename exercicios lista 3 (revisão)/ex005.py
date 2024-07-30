preco = float(input('Qual o valor de custo de produção deste produto?\n'))
taxa = float(input('Qual o valor da taxa de acréscimo em percentual?\n'))
valorf = preco+(preco*(taxa/100))
print(f'O valor de venda do seu produto será de: {valorf}')