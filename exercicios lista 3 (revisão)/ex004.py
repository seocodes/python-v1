nome = str(input('Type your name:\n'))
salario  = int(input('Whats your current salary?\n'))
print('''Our departments are:
      V -  Vendas
      C - Compras
      P - Produção''')
cargo = str(input('Whats your department?\n'))

match (cargo):
    case "V":
        print(f'O seu novo salário será de: {salario+(salario*(10/100))}')
    case "C":
        print(f'O seu novo salário será de: {salario+(salario*(8/100))}')
    case 'P':
        print(f'O seu novo salário será de: {salario+(salario*(15/100))}')
