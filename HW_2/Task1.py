# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

coins = [randint(0, 1) for _ in range(int(input('Введите количество монет: ')))]
print(coins)
print(min(coins.count(1), coins.count(0)))
