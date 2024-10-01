#1
'''
g = int(input())

a = g // 1 % 10
b = g //10 % 10

if a == 0 and b == 0:
    print('YES')
else:
    print ('NO')
'''

#2
'''
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 + x2 + y1 + y2) % 2 == 0:

    print('YES')
else:
    print('NO')
'''

#3
'''
v, p = int(input()), input()

if (10<=v<=15) and p == 'f':
    print('YES')
else: 
    print('NO')
'''

#4
'''
a = int(input())

if 1<=a<=10:   
    if a == 1:
        print('I')
    elif a == 2:
        print('II')
    elif a == 3:
        print('III')
    elif a == 4:
        print('IV')
    elif a == 5:
        print('V')
    elif a == 6:
        print('VI')
    elif a == 7:
        print('VII')
    elif a == 8:
        print('VIII')
    elif a == 9:
        print('IX')
    elif a == 10:
        print('X')
else:
    print('ошибка')
'''

#5
'''
a = int(input())

if a % 2 != 0:
    print('YES')
elif (a % 2 == 0) and 2<=a<=5:
    print('NO')
elif (a % 2 == 0) and 6<=a<=20:
    print('YES')
elif (a % 2 == 0) and a > 20:
    print('NO')
'''

#6
'''
x, y, x2, y2 = int(input()), int(input()), int(input()), int(input())

if ((x - x2) == (y - y2))or( (x - x2) == ((y - y2) * -1)) and x-x2!=0 and y-y2!=0 :
    print ('YES')
else:
    print('NO')
'''

#7
'''
x, y, x2, y2 = int(input()), int(input()), int(input()), int(input())

if ((x - x2) * (y - y2)) == 2 or ((x - x2) * (y - y2)) == - 2  :
    print ('YES')
else:
    print('NO')
'''

#8
'''
x, y, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (((x - x2) == (y - y2))or( (x - x2) == ((y - y2) * -1)) and x-x2!=0 and y-y2!=0) or (x==x2 or y==y2):
    print ('YES')
else:
    print('NO')
'''








