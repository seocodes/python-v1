nome = str(input('Qual seu nome?\n'))
prod = str(input('Qual o produto comprado?\n'))
quant = int(input('Em qual quantidade\n'))
price = float(input('Qual o preço deste produto\n'))
compra = quant*price
print(f'{nome} o valor de {quant} de {prod} será de {compra}')