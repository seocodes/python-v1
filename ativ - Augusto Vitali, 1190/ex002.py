produtos = []
precos = []
produtocaro = 0
while True:
    print('''MENU DE OPÇÕES
    1 - Cadastrar
    2 - Excluir
    3 - Exibir
    4 - Sair''')
    escolha = int(input('Digite a operação escolhida: '))
    if escolha == 4:
        print('Saindo do sistema...')
        break
    elif escolha == 1:
        produto = input('Digite o nome do produto: ').lower().title()
        preco = float(input('Digite o preço do produto: '))
        produtos.append(produto)            #adiciona os nomes e preços dados pelo user
        precos.append(preco)
        if preco > 100:
            produtocaro = produtocaro + 1
    elif escolha == 2:
        print(f'Lista de produtos: {produtos}') 
        delete = int(input('Qual produto deve ser removido da lista? Comece pelo número 1: ')) - 1
        produtos.pop(delete)    #exclui pelo indice informado pelo usuario
        precos.pop(delete)
    elif escolha == 3:
        produtos.sort(reverse=False)  #deixa as listas em ordem crescente/alfabética
        precos.sort(reverse=False)
        print(f'Os produtos são: {produtos}.\n')
        print(f'Os preços (ordenados) são: {precos}\n')
        print(f'O total de produtos cadastrados foram: {len(produtos)}\n')
        print(f'{produtocaro} produto(s) custam mais que 100R$.')
    else: 
        print('Operação inválida.')
        continue