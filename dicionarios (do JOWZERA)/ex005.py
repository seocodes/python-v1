dic = {}

for i in range(2):
    nome = input('nome ')
    tel = int(input('tel '))
    dic[nome] = tel

for i, o in dic.items():
    print(f'{i}> {o}')