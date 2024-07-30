padaria  = { 1 : ["Pastel", 5.00, 10],  2 : ["Coxinha", 4.00,  5],  3 : ["Sonho", 3.50, 15]}
 
while True :
 
    print("---   MENU   ---")
    print("1 - cadastrar ")
    print("2 - pesquisar")
    print("3 - alterar")
    print("4 - excluir")
    print("5 - incluir novo produto")
    print("6 - sair")
 
    escolha = int(input("> "))
 
    if escolha == 1:
        produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o preco do produto: "))
        quantidade = int(input("Digite a quantidade de produtos: "))
        padaria[len(padaria)+1] = [produto, preco, quantidade]
 
    if escolha == 2:
        listanome = []
        listapreco = []
        listaquantidade = []
        for nome, preco, quantidade in padaria.values():
            listanome.append(nome)
            listapreco.append(preco)
            listaquantidade.append(quantidade)
            print(listanome, listapreco, listaquantidade)
        prodmaiscaro = max(listapreco)
        prodmaisbarato = min(listapreco)
        prodmaisquanti = max(listaquantidade)
        prodmenosquanti = min(listaquantidade)
        somaquantidade = sum(listaquantidade)
        somapreco = sum(listapreco)
        print("Produto mais caro: ", prodmaiscaro)
        print("Produto mais barato: ", prodmaisbarato)
        print("Produto com mais quantidade: ", prodmaisquanti)
        print("Produto com menos quantidade: ", prodmenosquanti)
        print("Quantidade: ", somaquantidade)
        print("Soma: ", somapreco)
    if escolha == 3:
        id = int(input('digite o id do produto: '))
        produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o preco do produto: "))
        quantidade = int(input("Digite a quantidade de produtos: "))
        padaria[id] = [produto, preco, quantidade]
    if escolha == 4:
        id = int(input('digite o id do produto: '))
        padaria.pop(id)
    if escolha == 5:
        produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o preco do produto: "))
        quantidade = int(input("Digite a quantidade de produtos: "))
        padaria[len(padaria)+1] = [produto, preco, quantidade]
    if escolha == 6:
        exit()  
