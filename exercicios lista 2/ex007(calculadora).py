n1 = float(input('Digite um número:\n'))
n2 = float(input('Digite outro\n'))
op = str(input('Digite a operação\n'))

def soma(a,b):
    print(a+b)


def sub(a,b):
    print(a-b)


def mult(a,b):
    print(a*b)


def div(a,b):
    print(a/b)


if op == "+":
    soma(n1,n2)
elif op == "x":
    mult(n1,n2)
elif op == "/":
    div(n1,n2)
elif op == '-':
    sub(n1,n2)

