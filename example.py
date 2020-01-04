#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# noll = '000000'
# for i in range(1,6):
#     print(i, noll, sep = ' ')
'''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# a = 0
# for i in range(10):
#     answer = input('Введите число:')
#     answer = int(answer)
#     if answer == 5:
#       a = a + 1
# print(a)
'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# proizvedenie = 1
# for i in range(1,6):
#     proizvedenie*=i
# print(proizvedenie)
'''
Задача 5

Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

# в обратном порядке 1 вариант

# integer_number = 2129
# n2 = 0
# while integer_number > 0:
# 	digit = integer_number % 10 # находим остаток - последнюю цифру числа
# 	integer_number = integer_number // 10 # делим нацело - убираем из числа последнюю цифру
# 	n2 = n2 * 10 # увеличиваем разрядность второго числа
# 	n2 = n2 + digit # добавляем очередную цифру
#
# while n2>0:
#     print(n2%10)
#     n2 = n2//10

# В обратном порядке 2 вариант

# c = integer_number
# a = 0
# #print(integer_number%10,integer_number//10)
#
# while c>0:
#     # print(integer_number%10)
#     c = c//10
#     a+=1
# b = int(10**(a-1))
# while 1 <= b:
#     print(integer_number//b)
#     integer_number = int(integer_number%b)
#     b = int(b/10)

# integer_number = integer_number/b
# b = b/10

'''
Задача 6

Найти сумму цифр числа.
'''
# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
# a = 0
# while integer_number>0:
#     a = a + (integer_number%10)
#     integer_number = integer_number//10
# print(a)
'''
Задача 7

Найти произведение цифр числа.
'''

# integer_number = 2129
#
# a = 1
# while integer_number>0:
#     a = a * (integer_number%10)
#     integer_number = integer_number//10
# print(a)

'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9

Найти максимальную цифру в числе
'''
# integer_number = 8212712
#
# max = integer_number%10
# while integer_number>0:
#     integer_number = integer_number//10
#     if max < integer_number%10:
#         max = integer_number%10
# print(max)

'''
Задача 10

Найти количество цифр 5 в числе
'''
# integer_number = 8521552712
#
# count_five = 0
# while integer_number>0:
#     if integer_number%10 == 5:
#         count_five+=1
#     integer_number = integer_number//10
# print(count_five)