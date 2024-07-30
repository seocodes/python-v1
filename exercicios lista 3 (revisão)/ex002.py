valor = int(input('Qual o valor depositado?\n'))
juros = float(input('Digite o percentual dos juros no mês:\n'))
rend = valor+(valor*(juros/100))
print(f'O rendimento dos {valor} depositados após um mês será de {rend}.')

