#Возведение в степень
print(2 ** 0)
print(2 ** 1)
print(2 ** 2)
print(2 ** 3)
print(2 ** (-1))
print()
#Отрицательное число в степень и отрицательная степень
print(2**(-2))
print((-3)**3)
print()
print(2 ** 2 ** 3)     # 2 ** (2 ** 3) = 2 ** 8
print()
#Целочисленное деление
print(10 // 3)
print(10 // 4)
print(10 // 5)
print(10 // 6)
print(10 // 12)
print()
print(10 // 3) # округление в меньшую сторону
print(-10 // 3) # округление в меньшую сторону
print()
#Деление с остатком
print(10 % 3)
print(10 % 4)
print(10 % 5)
print(10 % 6)
print(10 % 12)
print(10 % 20)
print()
print(5 % 9)
print(3 % 13)
print(5 // 9)
print(3 // 13)

#Zadaniya
'''
b,q,n = int(input()), int(input()), int(input())
print(b*(q**(n-1)))
'''
'''
m = int(input())
print(m//100)
'''
'''
n, k = int(input()), int(input())
print(k//n)
print(k%n)
'''
'''
n = int(input())
print((n//2)+(n%2))
'''
'''
m = int(input())
print(m, 'мин - это', m//60, 'час', m%60, 'минут.')
'''
#POEZDDDDDDDDDDDDDDDDDDDDDDDDDDDD
'''
m = int(input())
print(((m-1)//4)+1)
'''
'''
#Задача 1. Напишите программу, определяющую число десятков и единиц в двузначном числе.
num = int(input())
last_digit = num % 10
first_digit = num // 10

print('Число десятков =', first_digit)
print('Число единиц =', last_digit)
'''
'''
#Задача 2. Напишите программу, в которой рассчитывается сумма цифр двузначного числа.
num = int(input())
last_digit = num % 10
first_digit = num // 10

print('Сумма цифр =', last_digit + first_digit)
'''
'''
#Задача 3. Напишите программу, которая печатает число, образованное при перестановке цифр двузначного числа.
num = int(input())
last_digit = num % 10
first_digit = num // 10

print('Искомое число =', last_digit * 10 + first_digit)
'''
'''
#Задача 4. Напишите программу, в которую вводится трехзначное число и которая выводит на экран его цифры (через запятую).
num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100

print(digit1, digit2, digit3, sep=',')
'''
'''
#Zadanie 
num = int(input())
a = num % 10
b = (num // 10) % 10
c = num // 100

print('Сумма цифр =', (a+b+c))
print('Произведение цифр =', (a*b*c))
'''
'''
#ZADANIE
num = int(input())
c = num % 10
b = (num // 10) % 10
a = num // 100
print(a,b,c, '\n', a,c,b, '\n' ,b,a,c, '\n', b,c,a, '\n', c,a,b, '\n', c,b,a, '\n', sep='')
'''
'''
#ZADANIE!!!
num = int(input())
a = num // 1 % 10
b = num // 10 % 10
c = num // 100 % 10
d = num // 1000 % 10

print('Цифра в позиции тысяч равна', d)
print('Цифра в позиции сотен равна', c)
print('Цифра в позиции десятков равна', b)
print('Цифра в позиции единиц равна', a)
'''


