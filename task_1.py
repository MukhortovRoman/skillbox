def point(numbers):
    count = 0
    while numbers < 1:
        numbers *= 10
        count += 1
    print('Формат плавающей точки: x =', round(numbers, 1), '* 10 **', count * -1)


def point_1(numbers):
    count = 0
    while numbers > 10:
        numbers /= 10
        count += 1
    print('Формат плавающей точки: x =', numbers, '* 10 **', count * 1)


def point_2(numbers):
    count = 0
    while 1 <= numbers < 10:
        numbers /= 10
        count += 1
    print('Формат плавающей точки: x =', numbers, '* 10 **', count * 1)


def main():
    numbers = float(input('Введите число: '))
    if 0 < numbers < 1:
        point(numbers)
    elif numbers > 10:
        point_1(numbers)
    elif 1 <= numbers < 10:
        point_2(numbers)
    else:
        print('Введите число больше нуля')


if __name__ == '__main__':
    main()
