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



# n = int(input("Ввидите число: "))
# count = 0
# for i in range(n):
#     list_1.append(randint(1,10))
#     #list_2.add(list_1[i])

# #list_1 = [i for i in range(n)))] все ниже тоже самое
# list_1 = [randint(1,10) for _ in range(int(input("Ввидите число: ")))]
# list_1 = [int(input("ввидите число")) for _ in range(int(input("Ввидите число: ")))] #лист компликтейшен
# print(list_1)
# print(len(set(list_1)))


# #list =  [1, 1, 2, 0, -1, 3, 4, 4]
# list_1 = []
# #list_2 = set()