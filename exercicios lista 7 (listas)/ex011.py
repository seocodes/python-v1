medias = []
alunoaprovado = 0
for y in range(0,10):
    print(f'Notas do aluno {y+1}')
    n1 = int(input('Digite a nota:\n'))
    n2 = int(input('Digite a nota:\n'))
    n3 = int(input('Digite a nota:\n'))
    n4 = int(input('Digite a nota:\n'))
    media = (n1+n2+n3+n4)/4
    medias.append(media)
    if media >= 7:
        alunoaprovado = alunoaprovado + 1
print(f'As médias dos alunos foram: {medias}, e {alunoaprovado} foram aprovados (média >= 7)')