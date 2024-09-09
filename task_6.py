def D(x):
    return x ** 3 - 3 * x ** 2 - 12 * x + 10


d = float(input('Введите максимально допустимый уровень опасности: '))
while d < 0:
    print('Введите положительное число: ')
    d = float(input())

l = 0
r = 4
d_min = d
x_min = 4
while True:
    x = (l + r) / 2
    if D(x) < -d:
        r = x
    elif D(x) > d:
        l = x
    elif r - l < 0.00000001:
        break
    else:
        l = x
        if abs(D(x)) < abs(d_min):
            x_min = x
            d_min = D(x)

print('Приблизительная глубина безопасной кладки ', x_min, 'м')
