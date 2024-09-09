def rev(num_1, num_2):
    num_1 = num_1[::-1]
    num_2 = num_2[::-1]
    summ = int(num_1) + int(num_2)
    print(f'\nПервое число наоборот: {num_1}')
    print(f'Второе число наоборот: {num_2}')
    print('Сумма:', summ)
    x = str(summ)
    x = x[::-1]
    print('\nСумма наоборот:', x)


def main():
    num_1 = input('Введите первое число: ')
    num_2 = input('Введите второе число: ')
    rev(num_1, num_2)


if __name__ == '__main__':
    main()

