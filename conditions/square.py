# 1️⃣ Дано три сторони трикутника.
# Знайти його площу, якщо такий трикутник існує

import math

a = int(input("Введіть довжину першої сторони "))
b = int(input("Введіть довжину другої сторони "))
c = int(input("Введіть довжину третьої сторони "))

# a + b > c
# a + c > b
# b + c > a

isTriangleExists = (a + b > c) and (a + c > b) and (b + c > a)

if isTriangleExists:
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Площа =", s)
else:
    print("Трикутника не існує")

# a = 1, b = 2, c = 5