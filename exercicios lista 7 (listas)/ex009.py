nums = []
for x in range(0,5):
    n = int(input('Digite um número:\n'))
    nums.append(n)
m = min(nums)
ma = max(nums)
print(f'O maior número digitado foi {ma} e o menor, {m}')