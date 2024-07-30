empresa = {}
for x in range(4):
    code = int(input('Digite seu código: '))
    nome = input('Digite seu nome: ')
    empresa.update({code: nome})
print(f'Usuários cadastrados: {empresa}')
dem = int(input('OOOOPS, VAI DEMITIR QUEM?\n')) - 1
empresa.pop(dem)
print(empresa)