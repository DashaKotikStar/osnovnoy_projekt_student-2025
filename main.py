'''print('Hello, World!')
name = input("Скажи своё имя: ")
print(name)

age = int(input("Скажи свой возраст: "))
print("Тебе ", age, "Лет")  #функция print нужна для вывода данных в окно консоли

a = int(input("Введи первое число: ")) #только число
b = int(input("Введи второе число: "))
print("Идёт рассчет.")
s = a + b
print(a, '+', b, '=', a + b)
water = 4.5
print("Я пью ", water, " литра воды")

Функция tape Нужна для определения типов данных наших переменных
tape(а)
5*8/10

a = 5
b = 8
c = 10
q = (a*c)/c
print("Вычислите: (5*8)/10")
s= int(input("Введи ответ: "))

if q == s:
    print("Верный ответ! Поздравляю!")
else:
    print("Вашь ответ не верный. Верный ответ: ", q)

'''
# x^2+3x+6=0 D
import math

a = int(input("Введи число: ")) #1
b = int(input("Введи число: ")) #3
c = int(input("Введи число: ")) #6

D = int(b*b - 4*a*c)

if D < 0:
    print("Ответ: i-15")
else:
    r = 2 * a
    X = int((-b + math.sqrt(D)) / r)
    x = int((-b - math.sqrt(D)) / r)

    print('X1 = ', X, 'X2 = ', x)
