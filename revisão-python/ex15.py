nums = []
pares = []
impares = []
primos = []


while True:
    print('''      1 - ADICIONAR
      2 - REMOVER
      3 - EXIBIR
      4 - EXIBIR PARES
      5 - EXIBIR ÍMPARES
      6 - EXIBIR NUMS PRIMOS
      7 - SAIR''')
    opcao = int(input('\nDigite sua escolha: '))
    if opcao == 1:
        add = int(input('Adicione número: '))
        nums.append(add)
        if add % 2 == 0:
            pares.append(add)
        else:
            impares.append(add)
        if add >= 1:
            for i in range(2, add):
                if add % i == 0: #aqui deu errado, depois ver pq
                    break
                else:
                    primos.append(add)
    if opcao == 2:
        remove = int(input('Número a remover: '))
        if remove in nums:
            nums.remove(remove)
        else:
            print('Esse número não está na lista.')
    if opcao == 3:
        print(nums)
    if opcao == 4:
        print(pares)
    if opcao == 5:
        print(impares)
    if opcao == 6:
        print(primos)
        if opcao == 7:
            break
    else:
        print('Operação não existente\n')
        continue
