'''
answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
'''

'''
num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, 'меньше чем', num2)
if num1 > num2:
    print(num1, 'больше чем', num2)

if num1 == num2:  # используем двойное равенство
    print(num1, 'равно', num2)
if num1 != num2:
    print(num1, 'не равно', num2)
'''
'''
age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок')
'''
'''
#Задача 1. Напишите программу, которая считывает одну строку. Если это строка «Python», программа выводит «ДА», в противном случае программа выводит «НЕТ».
word = input()

if word == 'Python':
    print('ДА')
else:
    print('НЕТ')
'''
'''
#Задача 2. Напишите программу, которая определяет, состоит ли двузначное число, введенное с клавиатуры, 
# из одинаковых цифр. Если состоит, то программа выводит «ДА», в противном случае программа выводит «НЕТ».
num = int(input())

last_digit = num % 10    # последняя цифра числа
first_digit = num // 10  # первая цифра числа

if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')
'''
'''
#Задача 3. Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.
num1, num2, num3 = int(input()), int(input()), int(input())

counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1

print(counter)
'''
'''
#1 Zadanie
pas, pas2 = input(), input()
if pas == pas2:
    print('Пароль принят')
else:
    print('Пароль не принят')
'''
'''
#2 Zadanie
num = int(input()) % 2
if num == 0:
    print('Четное')
else:
    print('Нечетное')
'''
#4 Zadanie
'''
num = int(input())
a = num // 1 % 10
b = num // 10 % 10
c = num // 100 % 10
d = num // 1000 % 10

if (a + d) == (c - b):
        print ('ДА')
else:
        print('НЕТ')
'''
'''
#5 Zadanie
v = int(input())
if v < 18:
    print('Доступ запрещен')
else:
    print('Доступ разрешен')
'''
'''
#6 Zadanie
a, b, c = int(input()), int(input()), int(input())
if ( b - a) + b == c:
    print('YES')
else:
    print('NO')
'''
'''
#7 Zadanie
a,b,c,d = int(input()), int(input()), int(input()), int(input())
ab=0
cd=0
if a<b:
    ab=a
else:
       ab=b
if c<d:
    cd=c
else:
       cd=d
if ab<cd:
    print(ab)
else:
    print(cd)
'''
'''
#8 Zadanie

v = int(input())
if v<=13:
    print('детство')
if 14 <= v <= 24:
    print('молодость')
if 25 <= v <= 59:
    print('зрелость')
if  v >= 60:
    print('старость')
'''
'''
#9 Zadanie
a,b,c = int(input()), int(input()), int(input())
d = 0
if a>0:
    d = d+a
if b > 0:
    d = d+b
if c > 0:
    d = d+c
print (d)
'''