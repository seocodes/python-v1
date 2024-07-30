nome = str(input('Qual seu nome?\n'))
print('''Nossos curso são:
      A - ADMINISTRAÇÃO
      D - DIREITO
      C - CONTABILIDADE
      F - FISIOTERAPIA
      O - ODONTOLOGIA
      M - MEDICINA''')

cargo = str(input('Qual seu curso?\n')).upper()

match (cargo):
    case "A":
        print(f'O seu curso é ADM')
    case "D":
        print(f'O seu curso é Direito')
    case "C":
        print(f'O seu curso é Contabilidade')
    case "F":
        print(f'O seu curso é FISIOTERAPIA')
    case "O":
        print(f'O seu curso é ODONTOLOGIA')
    case "M":
        print(f'O seu curso é MEDICINA')
    case __:
        print('VAI TI FUDE O')

