estoque = {}
total = 0
op = int(input('Quantos produtos irá cadastrar?\n'))
for x in range(op):
    code = input('Código: ')
    nome = input('Nome: ')
    preco = float(input('Preço: '))
    qtd = int(input('Quantidade: '))
    lista = []
    lista.append(nome)
    lista.append(preco)
    lista.append(qtd)
    estoque.update({code: lista})
for code, lista in estoque.items():
    subtotal = estoque[code][1] * estoque[code][2]
    print(f'{lista[2]} {lista[0]}(s): R${subtotal}')
    total += subtotal
print(f'Total = {total}')