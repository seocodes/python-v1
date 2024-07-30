n = str(input('''Digite um dia da semana:
              1 - Seg
              2 - Ter
              3 - Qua
              4 - Qui
              5 - Sex
              6 - Sab
              7 - Dom\n'''))
match (n):
    case '1':
        print('Segunda')
    case '2':
        print('Terça')
    case '3':
        print('Quarta')
    case '4':
        print('Quinta')
    case '5':
        print('Sexta')
    case '6':
        print('Sábado')
    case '7':
        print('Domingo')
    case _:
        print('Tu é troll nao existe.')
        
    

