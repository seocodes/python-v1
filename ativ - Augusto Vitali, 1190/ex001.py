funcionarios = []
salarios = []

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
        funcionario = input('Digite o nome do funcionário: ').lower().title()
        salario = float(input('Digite o salário desse funcionário: '))
        funcionarios.append(funcionario)     #adiciona os nomes e preços dados pelo user
        salarios.append(salario)
    elif escolha == 2:
        print(f'Lista de funcionários: {funcionarios}') 
        delete = int(input('Qual funcionário deve ser removido da lista? Comece pelo número 1: ')) - 1
        funcionarios.pop(delete)      #exclui pelo indice informado pelo usuario
        salarios.pop(delete)
    elif escolha == 3:
        funcionarios.sort(reverse=False)
        print(f'Funcionários cadastrados: {funcionarios}\n') 
        print(f'Maior salário: {max(salarios)}. Menor salário: {min(salarios)}\n')
        print(f'Soma dos salários: {sum(salarios)}\n')              #deixa as listas em ordem crescente/alfabética
        print(f'Número de funcionários cadastrados: {len(funcionarios)}.')
    else: 
        print('Operação inválida.')
        continue

