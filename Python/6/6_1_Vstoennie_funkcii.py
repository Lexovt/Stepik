#Встроенные функции

#Функции min() и max()
'''
a = max(3, 8, -3, 12, 9)
b = min(3, 8, -3, 12, 9)
c = max(3.14, 2.17, 9.8)
print(a)
print(b)
print(c)
#Функция abs()

print(abs(10))
print(abs(-7))
print(abs(0))
print(abs(-17.67))
'''

###################################################################################
#ZADANIYA

#1
'''
d1, d2, d3, d4, d5 = int(input()), int(input()), int(input()), int(input()), int(input())
print('Наименьшее число =', min(d1, d2, d3, d4, d5))
print('Наибольшее число =', max(d1, d2, d3, d4, d5))
'''
#2
'''
d1, d2, d3 = int(input()), int(input()), int(input())
s = (d1+d2+d3) - (min(d1, d2, d3))- (max(d1, d2, d3)) 

print(max(d1, d2, d3))
print(s)
print(min(d1, d2, d3))
'''
#3
'''
g = int(input())

a = g // 1 % 10
b = g // 10 % 10
c = g // 100 % 10

mn = min(a,b,c)
mx = max(a,b,c)
sre = (a+b+c)-mn-mx

if mx - mn == sre:
    print('Число интересное')
else:
    print('Число неинтересное')
'''
#4
'''
d1, d2, d3, d4, d5 = abs(float(input())), abs(float(input())), abs(float(input())), abs(float(input())), abs(float(input()))

print(d1+d2+d3+d4+d5)
'''

#5
'''
p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
print((abs(p1-q1))+(abs(p2-q2)))
'''

