#ТЕМА: Логические операторы.
# Оператор and

'''
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
if age >= 12 and grade >= 7:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
'''

'''
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and city == 'Москва':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
'''

# Оператор or
'''
city = input('В каком городе вы живете?: ')
if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
'''

# Оператор not
'''
age = int(input('Сколько вам лет?: '))
if not (age < 12):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

# полностью эквивалентен коду:

age = int(input('Сколько вам лет?: '))
if age >= 12:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
'''

# Решение задач Примеры!!

# Задача 1. Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным.
'''
num = int(input())
if 100 <= num <= 999:     # num >= 100 and num <= 999
    print('Число является трёхзначным')
else:
    print('Число не является трёхзначным')
'''

# Задача 2. Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.
'''
num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')
'''

# Задача 3. Напишите программу, которая по координатам точки, не лежащей на осях координат, определяет номер координатной четверти, в которой она находится.
'''
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')
'''

# ЗАДАЧИ ТЕСТОВ

#1
'''
x = int(input())

if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')
'''
#2
'''
x = int(input())

if x<= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')
'''
#3
'''
x = int(input())

if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')
'''
#4
'''
x = int(input())

if (x //1000 % 10 > 0) and (x //10000 % 10 == 0):
    if (x % 7 == 0) or (x % 17 == 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
'''
#5
'''
a, b, c = int(input()), int(input()), int(input())
if a+b > c and a+c>b and b+c>a:
    print('YES')
else:
    print('NO')
'''

#6
'''
g = int(input())

if ((g % 4 == 0) and (g%100!=0)) or g % 400 == 0:
    print('YES')
else:
    print('NO')
'''

#7
'''
x, y, x1, y1 = int(input()), int(input()), int(input()), int(input())

if x==x1 or y==y1:
    print('YES')
else:
    print('NO')
'''

#8
'''
x, y, x2, y2 = int(input()), int(input()), int(input()), int(input())

if x-1<=x2<=x+1 and y-1<=y2<=y+1:
    print('YES')
else:
    print('NO')
'''