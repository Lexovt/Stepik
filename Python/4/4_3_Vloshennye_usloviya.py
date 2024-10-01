# ТЕМА: Вложенные и каскадные условия

'''
grade = int(input('Введите вашу отметку по 100-балльной системе: '))

if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70:
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)
# В этом примере уровень вложенности настолько глубок, что код становится трудно понять.
'''

#Приведенный ниже фрагмент кода является примером каскадного условного оператораif-elif-else.
# Этот фрагмент кода работает так же, как предыдущий код, использующий вложенный условный оператор.

'''
grade = int(input('Введите вашу отметку: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)
'''
#В данном случае если будет введен некорректный сигнал светофора, программа ничего не выведет.
# Каждое условие будет проверено поочередно, и программа завершится без ошибок.
'''
traffic_light_signal = input('Введите сигнал светофора: ')

if traffic_light_signal == 'красный':
    print('Стой!')
elif traffic_light_signal == 'желтый':
    print('Приготовься...')
elif traffic_light_signal == 'зеленый':
    print('Иди!')
'''

#ПРИМЕРЫ ЗАДАЧ

#Задача 1. Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел:
#3
#3 (если все совпадают),
#2
#2 (если два совпадает) или
#0
#0 (если все числа различны).
'''
a, b, c = int(input()), int(input()), int(input())

if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)
'''
#2 способ. Использование каскадного условного оператора.
'''
a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b:
    print(2)
elif b == c:
    print(2)
elif a == c:
    print(2)
else:
    print(0)
'''
#3 способ. Использование каскадного условного оператора и логического оператора or.
'''
a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
'''

#ЗАДАНИЯ!!

#1
'''
n, k = int(input()), int(input())

if n > k:
    print('NO')
elif n<k:
    print('YES')
else:
    print("Don't know")
'''

#2
'''
a, b, c = int(input()), int(input()), int(input())

if a==b==c:
    print('Равносторонний')
elif a!=b and a!=c and b!=c:
    print('Разносторонний')
else: 
    print('Равнобедренный')
'''

#3
'''
a, b, c = int(input()), int(input()), int(input())
if (a>b and a<c) or (a<b and a>c):
    print(a)
elif (b>a and b<c) or (b<a and b>c):
    print(b)
else:
    print(c)
'''

#4
'''
m = int(input())

if m<=7 and m!=2:
    if m%2==0:
        print('30')
    else:
        print('31')
elif m>=8:
    if m%2==0:
        print('31')
    else:
        print('30')
else:
    print('28')
'''

#5
'''
v = int(input())

if v < 60:
    print('Легкий вес')
elif 60<=v<64:
    print('Первый полусредний вес')
elif 64<=v<69:
    print('Полусредний вес')
'''

#6
'''
a,b,z = int(input()), int(input()), input()

if z == '-' or z=='+' or z == '*' or z=='/':
    if z == '-':
        print(a-b)
    elif z == '+':
        print(a+b)
    elif z == '*':
            print(a*b)
    elif (z == '/') and b!=0:
        print(a/b)
    else:
        print('На ноль делить нельзя!')
else:
    print('Неверная операция')
'''
#7
'''
a, b = input(), input()

if a == 'красный' or a == 'синий' or a == 'желтый':
    if b == 'красный' or b == 'синий' or b == 'желтый':
        if a == 'красный' and b == 'красный':
            print('красный')
        elif a == 'желтый' and b == 'желтый':
            print('желтый')
        elif a == 'синий' and b == 'синий':
            print('синий')
        elif (a == 'синий' and b == 'красный') or (b == 'синий' and a == 'красный'):
            print('фиолетовый')
        elif (a == 'желтый' and b == 'красный') or (b == 'желтый' and a == 'красный'):
            print('оранжевый')
        elif (a == 'синий' and b == 'желтый') or (b == 'синий' and a == 'желтый'):
            print('зеленый')
    else:
        print('ошибка цвета')

else:
    print('ошибка цвета')
'''
#8
'''
a = int(input())

if 0 <= a <= 36:
    if a == 0:
        print('зеленый')
    elif 1 <=a <= 10 and a % 2 == 0:
        print('черный')
    elif 1 <=a <= 10 and a % 2 != 0:
        print('красный')
    elif 11 <=a <= 18 and a % 2 == 0:
        print('красный')
    elif 11 <=a <= 18 and a % 2 != 0:
        print('черный') 
    elif 19 <=a <= 28 and a % 2 == 0:
        print('черный')
    elif 19 <=a <= 28 and a % 2 != 0:
        print('красный')
    elif 29 <=a <= 36 and a % 2 == 0:
        print('красный')
    elif 29 <=a <= 36 and a % 2 != 0:
        print('черный')
else:
    print('ошибка ввода')
'''
#9
'''
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a==c and b==d:
    print(a,b)
elif c<b<d and a<c:
    print(c,b)
elif b==c and a<c:
    print(c)
elif a==c and c<b<d:
    print(a,b)
elif b==d and a<c:
    print(c,d)
elif c<a<d and b>d:
    print(a,d)
elif a==d and b>d:
    print(a)
elif c<a<d and b==d:
    print(a,b)
elif a==c and b>d:
    print(c,d)
elif a<c and d<b:
    print(c,d)
elif c<a<d and c<b<d:
    print(a,b)
else:
    print ('пустое множество')
'''


