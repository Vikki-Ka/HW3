# ; Напишите программу, которая принимает на вход
# ; строку, и отслеживает, сколько раз каждый символ
# ; уже встречался. Количество повторов добавляется к
# ; символам с помощью постфикса формата _n.
# ; Input: a a a b c a a d c d d
# ; Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# ; Для решения данной задачи используйте функцию
# ; .split()

# ; stroka = "a a a b c a a d c d d"
# ; stroka = stroka.split()

s ="She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
print(len(set(s.upper().split())))
