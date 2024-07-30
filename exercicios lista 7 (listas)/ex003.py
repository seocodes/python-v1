nums = []

for y in range(0,4):
    x = int(input('Digite sua nota:\n'))
    nums.append(x)
media = sum(nums)/4
print(f'As notas foram {nums}, e a média geral foi de: {media}')