frutas = []
quant = []
preco = []

while True:
    frutera =  input('Digite a fruta: \n').lower().title()
    quantid = int(input('Qual a quantidade dessa fruta que temos?\n '))
    precos = float(input('Qual o preço para venda dessa fruta? \n'))
    frutas.append(frutera)
    quant.append(quantid)
    preco.append(precos)
    op = input('Quer parar? Digite S para parar\n').upper()
    if op == 'S':
        break
for x in range(0, len(frutas)):
    print(f'Fruta: {frutas[x]} -- Quantidade: {quant[x]} -- Preço: {preco[x]}')

maior_quantidade = quant.index(max(quant))
menor_quantidade = quant.index(min(quant))

print(f'E a  fruta com maior quantidade é a {frutas[maior_quantidade]}, com {max(quant)} unidades, ja a menor, {frutas[menor_quantidade]}, com {min(quant)} unidades. ')
print(f'Quantidade total: {sum(quant)}')