dic = {}

for i in range(3):
    name = input("Enter name: ")
    nota1 = int(input('nota1> '))
    nota2 = int(input('nota2> '))
    nota3 = int(input('nota3> '))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        dic[name] = 'aprovado'
        print('aprovado')
    elif media < 7 and media >= 5:
        dic[name] = 'rec'
        print('rec')
    if media < 5:
        dic[name] = 'reprovado'
        print('reprovado')