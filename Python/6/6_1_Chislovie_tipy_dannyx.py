#ЧИСЛОВЫЕ ТИПЫ ДАННХ!!

'''
a = 13
b = 7

total = a + b
diff = a - b
prod = a * b
div1 = a / b
div2 = a // b
mod = a % b
exp = a ** b

print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div1)
print(a, '//', b, '=', div2)
print(a, '%', b, '=', mod)
print(a, '**', b, '=', exp)

'''

#Отличительной особенностью языка Python является неограниченность целочисленного типа данных.
'''
atom = 10 ** 80  # количество атомов во вселенной
print('Количество атомов =', atom)
'''

#ЧИСЛА С ПЛАВАЮЩЕЙ ТОЧКОЙ!
'''
a = 13.5
b = 2.0

total = a + b
diff = a - b
prod = a * b
div = a / b
exp = a ** b

print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div)
print(a, '**', b, '=', exp)
'''

###################################################################################################
#ZADACHI

#1
'''
a, b = float(input()), float(input())
s=((1/2)*a*b)
print(s)
'''
#2
'''
s, v1, v2 = float(input()), float(input()), float(input())
v=(v1+v2)
t = s / v
print(t)
'''
#3
'''
x = float(input())
if x == 0:
    print('Обратного числа не существует')
else:
    print(x**(-1))
'''

#4
'''
f= float(input())
t = (5/9)*(f-32)
print(t)
'''

#5
'''
age = float(input())
if age == 1:
    age = 10.5
elif age ==2:
    age = 21
elif age >= 3:
    age = (21 + (age -2)*4)
print(age)
'''

#6
'''
x = float(input())
print(int(x * 10) % 10)
'''

#7
'''
x = float(input())
print(x - (int(x)))
'''

