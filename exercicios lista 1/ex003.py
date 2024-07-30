nome = str(input('Qual seu nome?\n'))
dis = str(input('Disciplina\n'))
nota1 = float(input('Nota 1:\n'))
nota2 = float(input('Nota 2:\n'))
nota3 = float(input('Nota 3:\n'))
med = (nota1+nota2+nota3)/3
print(f'{nome} você ficou com a média: {med} na disciplina {dis}')