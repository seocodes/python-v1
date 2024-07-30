dict = {}

while True:
    print('''MENU DE OPÇÕES
    1 - Cadastrar (produto e preço)
    2 - Pesquisar
    3 - Alterar produto/preço
    4 - Excluir
    5 - Incluir NOVO
    6 - Sair''')
    op = int(input('Digite qual operação será feita > '))
    if op == 1:
        nome = input('NOME > ')
        preco = float(input('PREÇO > '))
        dict.update({nome: preco})
    if op == 2:
        print(f'Existe(m) {len(dict)} produto(s) na lista, que são:\n')
        for x, y in dict.items():
            print(f'{x}, R${y}')
        prodCaro = max(dict.values())
        prodBarato = min(dict.values())
        soma = sum(dict.values())
        print(f'Mais caro: {prodCaro}, mais barato: {prodBarato}, e soma dos preços = {soma}')
    if op == 3:
        for x, y in dict.items():
            print(f'{x}, R${y}')
        check = input('Digite o nome da fruta que terá o preço mudado > ')
        if check in dict.keys():
            newPrice = float(input('Novo preço > '))
            dict.update({check: newPrice})
        else:
            print('Produto não encontrado!')
            continue
    if op == 4:
        for x, y in dict.items():
            print(f'{x}, R${y}')
        delete = input('Qual produto deseja excluir > ')
        dict.pop(delete)
    if op == 5:
        newName = input('NOVO PRODUTO > ')
        newPrice = float(input('NOVO PREÇO > '))
        dict.update({newName: newPrice})
    if op == 6:
        print('SAINDO DO PROGRAMA...')
        break
    else:
        print('???')
    
