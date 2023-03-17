# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

namber = int(input("Ввидите длину массива: "))
findNamber = int(input("Ввидите искомое число: "))
list = [randint(0, 100) for _ in range(namber)]
print(*list)

blizkoMenshe = 0
blizkoBolshe = 100

for i in list:                                  #близкое меньшее
    if i < findNamber and i > blizkoMenshe:
        blizkoMenshe = i

for i in list:                                   #близкое большее
    if i > findNamber and i < blizkoBolshe:
        blizkoBolshe = i

if (findNamber - blizkoMenshe) <= (blizkoBolshe - findNamber):
    print(f"близкое к числу {findNamber} это {blizkoMenshe}")
else:
    print(f"близкое к числу {findNamber} это {blizkoBolshe}")

#print(blizkoMenshe, blizkoBolshe)