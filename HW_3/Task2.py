#  Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#1 2 3 4 5
#6
#-> 5

from random import randint
n = int(input('Введите количество элементов массива: '))
lst = [randint (1, n) for _ in range(n)]
print(lst)

x = int(input('Введите число x: '))
b = []

for i in lst:
    j = abs( i - x)
    b.append(j)
print(b)
print(f'Ближайшее по величине значение к числу {x} = {lst[b.index(min(b))]}')
