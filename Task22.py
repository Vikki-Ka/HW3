# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint

n = int(input("Длина первого множества: "))
m = int(input("Длина второго множества: "))

listOne = {randint(0,20) for _ in range(n)}
listTwo = {randint(0,20) for _ in range(m)}
print(listOne)
print(listTwo)
print("Результат: ")

result = listOne.intersection(listTwo)
sorted(result)
print(result)