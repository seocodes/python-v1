dic = {}

for i in range(4):
    nome = input("digite seu nome ")
    dic[i] = nome

for i in dic.keys():
    print(i+1)

escolha = int(input("Escreva qual deseja excluir: "))
dic.pop(escolha - 1)
print(dic)