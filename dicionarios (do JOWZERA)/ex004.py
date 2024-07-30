dic = {}

for i in range(4):
    livro = input('nome do livro> ')
    autor = input('autor> ')
    dic[livro] = autor

for i, o in dic.items():
    print(f'{i} - by: {o}')

