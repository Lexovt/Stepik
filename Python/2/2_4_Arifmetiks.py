num1 = 7                # num1 - это число
num2 = 10               # num2 - это число
num3 = num1 + num2      # num3 - это число

print(num3)

a = 3
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)

s = '1992'
year = int(s)
print(year)

#Задания
a = int(input())
b = a + 1
c = b + 1
print(a)
print(b)
print(c)

a, b, c = int(input()), int(input()), int(input())
print(a+b+c)

a = int(input())
v = a*a*a
s = 6*(a*a)
print('Объем =', v)
print('Площадь полной поверхности =', s)

a, b = int(input()), int(input())
c = 3*((a+b)*(a+b)*(a+b))+275*(b*b)-127*a-41
print(c)

a = int(input())
print('Следующее за числом', a, 'число:', a+1)
print('Для числа', a,  'предыдущее число:', a-1)

a, b, c, d= int(input()), int(input()), int(input()), int(input())
print((a+b+c+d)*3)

a, b = int(input()), int(input())
print(str(a), '+', str(b), '=', a+b)
print(str(a), '-', str(b), '=', a-b)
print(str(a), '*', str(b), '=', a*b)

a, d, n = int(input()), int(input()), int(input())
print(a+d*(n-1))

x = int(input())
print(x, 2*x, 3*x, 4*x, 5*x, sep='---')