nums = []
for x in range(0,5):
    n = float(input('Digite um número real:\n'))
    nums.append(n)
nums.sort(reverse=True)
print(nums)
