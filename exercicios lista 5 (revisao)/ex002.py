nome = str(input('Qual seu nome?\n'))
print('''Seu estado civil é:
      S - SOLTEIRO
      C - CASADO
      V - VIÚVO
      D - DIVORCIADO''')

estado = str(input('Qual seu estado civil?\n')).upper()

match (estado):
    case "S":
        print(f'TU É SOLTEIRO')
    case "C":
        print(f'CASADO')
    case "V":
        print(f'VIUVO')
    case "D":
        print(f'DIVORCIADO')
    case __:
        print('VAI TI FUDE O')
