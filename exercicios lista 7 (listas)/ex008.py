age = []
for x in range(0,10):
    idade = int(input('Digite sua idade:\n'))
    age.append(idade)
age.sort(reverse=False)
print(age)