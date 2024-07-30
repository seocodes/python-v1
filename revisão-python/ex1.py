salario_hora = float(input('Qual seu salário por hora?\n'))
horasTrabalhadas = int(input('Quantas horas são trabalhadas no mês?\n'))

salario_bruto = salario_hora*horasTrabalhadas
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05

salario = salario_bruto - inss - ir - sindicato

print(f'''Salário bruto: {salario_bruto}R$
      Imposto de renda: {ir}R$
      INSS: {inss}R$
      Sindicato: {sindicato}R$
      Salário Líquido: {salario}R$''')