import random
import os
os.system('cls')

n = int(input('Введите количество кустов: '))
x = [random. randint(0, 50) for _ in range(n)]
print(x)
x.extend([x[0], x[1]])
max_sum = 0
for i in range(len(x) - 2):
    triple_sum = x[i] + x[i + 1] + x[i + 2]
    if triple_sum > max_sum:
        max_sum = triple_sum
print(max_sum)
