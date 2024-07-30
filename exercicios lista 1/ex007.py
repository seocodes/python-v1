name = str(input('Qual seu nome?\n'))
numhoras = float(input('Quantas horas você trabalha por dia?\n'))
valorhora = float(input('Qual o valor da hora trabalhada?\n'))
salariob = numhoras*valorhora*27
salario = salariob-(salariob*(2/100))
print(f'O seu salário após os descontos será de {salario}')