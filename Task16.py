# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint

namber = int(input("Ввидите длину массива: "))
findNamber = int(input("Ввидите число для поиска:"))
list = [randint(0,9) for _ in range(namber)]
print(*list)

counter = 0
for i in list:
    if i == findNamber:
        counter += 1

print(f"искомое число {findNamber}")
if counter == 0:
    print(f"Числа {findNamber} нет в массиве")
else:
    print(f"число {findNamber} встречается {counter} раз")
